import os
import platform
import subprocess
import sys
import tempfile

import maya.cmds as cmds
import maya.OpenMayaAnim as OMA
from PySide2 import QtCore, QtWidgets
from shiboken2 import wrapInstance


def get_main_window():
    """this returns the maya main window for parenting"""
    window = omui.MQtUtil.mainWindow()
    return wrapInstance(int(window), QtWidgets.QDialog)


class RenderFarmSubmitDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Move to Build mode
        # Set the GUI components and layout
        self.setWindowTitle("NCCA Renderfarm Submit Tool Renderman For Maya")
        self.resize(600, 280)
        # Main layout for form
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.home_dir=os.environ.get("HOME")
        self.user=os.environ.get("USER")
        time_line=OMA.MAnimControl()
        # convert to int here, do we render non int frames?
        self.min_frame=int(time_line.minTime().value())
        self.max_frame=int(time_line.maxTime().value())
        row=0
        label=QtWidgets.QLabel("Active Renderer")
        self.gridLayout.addWidget(label, row, 0, 1, 1)
        self.active_renderer=QtWidgets.QComboBox()
        self.active_renderer.addItems(["file","renderman","vray","arnold","sw","hw2","default"])
        self.active_renderer.setToolTip("Choose the active renderer, note is file is chose it will use the one set in the maya file")
        self.gridLayout.addWidget(self.active_renderer, row, 1, 1, 3)


        row+=1
        # row 0 project name
        label=QtWidgets.QLabel("Project Name")
        name=cmds.workspace(q=True,sn=True)
        self.gridLayout.addWidget(label,row,0,1,1)
        self.project_name = QtWidgets.QLineEdit(f"{self.user}_{name}", self)
        self.project_name.setToolTip("This is the name of the project as it will appear on the Qube GUI")
        self.gridLayout.addWidget(self.project_name, row, 1, 1, 5)

        # row 1 select camera
        row+=1
        label=QtWidgets.QLabel("Camera")
        self.gridLayout.addWidget(label,row,0,1,1)
        self.camera = QtWidgets.QComboBox(self)
        self.camera.addItems(cmds.listCameras( p=True ))
        self.camera.setToolTip("select camera to render")
        
        self.gridLayout.addWidget(self.camera, row, 1, 1, 5)

        # row 2
        row+=2
        label=QtWidgets.QLabel("Start Frame")
        self.gridLayout.addWidget(label,row,0,1,1)
        self.start_frame=QtWidgets.QSpinBox()
        self.start_frame.setToolTip("Start frame for rendering, set from ROP but can be changed here, this will override the ROP value on the farm")

        self.start_frame.setRange(self.min_frame,self.max_frame)
        self.start_frame.setValue(self.min_frame)
        self.gridLayout.addWidget(self.start_frame,row,1,1,1)
        
        label=QtWidgets.QLabel("End Frame")
        self.gridLayout.addWidget(label,row,2,1,1)
        self.end_frame=QtWidgets.QSpinBox()
        self.end_frame.setRange(self.min_frame,self.max_frame)
        self.end_frame.setValue(self.max_frame)
        self.end_frame.setToolTip("End frame for rendering, set from ROP but can be changed here, this will override the ROP value on the farm")

        self.gridLayout.addWidget(self.end_frame,row,3,1,1)

        label=QtWidgets.QLabel("By Frame")
        self.gridLayout.addWidget(label,row,4,1,1)
        self.by_frame=QtWidgets.QSpinBox()
        self.by_frame.setValue(1)
        self.by_frame.setToolTip("Frame Step for rendering, set from ROP but can be changed here, this will override the ROP value on the farm")

        self.gridLayout.addWidget(self.by_frame,row,5,1,1)

        # row 3 Scene file selection
        row+=1
        self.scene_button=QtWidgets.QPushButton("Scene File")
        self.scene_button.setToolTip("Select the file to render, not this must be on the farm mount")
        self.gridLayout.addWidget(self.scene_button,row,0,1,1)
        self.scene_button.clicked.connect(self.set_scene_location)
        try :
            base_path=cmds.file(q=True, sn=True).split("/")[-2]
        except IndexError :
            base_path="file not loaded"
        project_path=cmds.workspace(q=True,sn=True).split("/")[-1]

        location=f"/render/{self.user}/{project_path}/{base_path}/{cmds.file(q=True, sn=True, shn=True)}"
        self.scene_location = QtWidgets.QLineEdit(location, self)
        self.scene_location.setToolTip("""This is the full path to the maya file on the farm, you can enter this manually or press the button to select.
        If the farm is mounted on /render you can navigate to here and select the file. If not you must specify the full path and name manually. 
        If this is not correct the renders will fail""")
        self.gridLayout.addWidget(self.scene_location, row, 1, 1, 5)

        # row 4
        row+=1
        # Project location
        self.project_button=QtWidgets.QPushButton("Project Location")
        self.project_button.setToolTip("Select the maya project for the scene")
        self.gridLayout.addWidget(self.project_button,row,0,1,1)
        self.project_button.clicked.connect(self.set_project_location)
        base_path=cmds.workspace(q=True,sn=True).split("/")[-1]
        
        location=f"/render/{self.user}/{base_path}/"
        self.project_location = QtWidgets.QLineEdit(location, self)
        self.project_location.setToolTip("""This is the full path to the maya project on the farm, you can enter this manually or press the button to select.
        If the farm is mounted on /render you can navigate to here and select the file. If not you must specify the full path and name manually. 
        If this is not correct the renders will fail""")
        self.gridLayout.addWidget(self.project_location, row, 1, 1, 5)


        row +=1 
        self.override_output_dir = QtWidgets.QCheckBox("Set Output Directory")
        self.override_output_dir.setChecked(False)
        
        self.gridLayout.addWidget(self.override_output_dir,row,0,1,1)
        self.output_dir=QtWidgets.QLineEdit(f"/render/{self.user}/output/")
        self.output_dir.setReadOnly(True)
        self.override_output_dir.stateChanged.connect(lambda state : self.output_dir.setReadOnly(not state))
        self.output_dir.setToolTip("this folder must be on the farm")
        self.gridLayout.addWidget(self.output_dir,row,1,1,1)
        
        row +=1 
        self.override_filename = QtWidgets.QCheckBox("Output Filename")
        self.override_filename.setChecked(False)
        
        self.gridLayout.addWidget(self.override_filename,row,0,1,1)
        self.output_filename=QtWidgets.QLineEdit(f"CustomFilename")
        self.output_filename.setReadOnly(True)
        self.override_filename.stateChanged.connect(lambda state : self.output_filename.setReadOnly(not state))
        self.output_filename.setToolTip("Override Filename in Render Globals")
        self.gridLayout.addWidget(self.output_filename,row,1,1,1)


        row +=1 
        self.override_extension = QtWidgets.QCheckBox("Output Format")
        self.override_extension.setChecked(False)

        self.gridLayout.addWidget(self.override_extension,row,0,1,1)
        self.output_extension=QtWidgets.QComboBox()
        self.output_extension.addItems(["exr","png","tif","jpeg","deepexr","maya"])
        self.output_extension.setDisabled(True)
        self.override_extension.stateChanged.connect(lambda state : self.output_extension.setDisabled(not state))
        self.output_extension.setToolTip("Override image extension in Render Globals")
        self.gridLayout.addWidget(self.output_extension,row,1,1,1)

        row +=1 
        label=QtWidgets.QLabel("Extra Commands")
        self.gridLayout.addWidget(label,row,0,1,1)
        self.extra_commands=QtWidgets.QLineEdit()
        self.gridLayout.addWidget(self.extra_commands,row,1,1,5)
        
        row+=1
        # cancel button

        self.Cancel = QtWidgets.QPushButton("Cancel", self)
        self.Cancel.setToolTip("Close the submit dialog")
        self.Cancel.clicked.connect(self.close)
        self.gridLayout.addWidget(self.Cancel, row, 0, 1, 1)

        # Write script button
        self.export = QtWidgets.QPushButton("Export Script", self)
        self.export.setToolTip("Export Python Submit script")
        self.export.clicked.connect(self.export_script)
        self.gridLayout.addWidget(self.export, row, 1,1, 1)

        # Submit button

        self.submit = QtWidgets.QPushButton("Submit", self)
        self.submit.pressed.connect(self.submit_job)
        self.submit.setEnabled(True)
        self.submit.setToolTip("Submit job to the farm, you must select a ROP before this will activate")
        self.gridLayout.addWidget(self.submit, row, 5, 1, 1)

    def _generate_payload(self) :
        ARNOLD_LOCATION='/opt/software/autodesk/arnold/maya2023'
        MAYA_ROOT='/opt/software/autodesk/maya2023/'

        range=f"{self.start_frame.value()}-{self.end_frame.value()}x{self.by_frame.value()}"
        set_output_dir=""
        if self.override_output_dir.isChecked() :
            set_output_dir=f"-rd {self.output_dir.text()}"
        
        output_filename=""
        if self.override_filename.isChecked() :
            output_filename=f"-im {self.output_filename.text()}"
        
        image_ext=""
        if self.override_extension.isChecked() :
            image_ext=f"-of {self.output_extension.currentText()}"
        
        payload=f"""#!/usr/bin/python3 
import os
import sys
sys.path.insert(0,"/public/devel/2022/pfx/qube/api/python/")

import qb
if os.environ.get("QB_SUPERVISOR") is None :
    os.environ["QB_SUPERVISOR"]="tete.bournemouth.ac.uk"
    os.environ["QB_DOMAIN"]="ncca"


job = {{}}
job['name'] = f"{self.project_name.text()}"
job['prototype'] = 'cmdrange'
package = {{}}
package['shell']="/bin/bash"

render_command=f"Render -s QB_FRAME_NUMBER -e QB_FRAME_NUMBER -r {self.active_renderer.currentText()}  {set_output_dir} {output_filename} {image_ext}  -proj {self.project_location.text()}  -cam {self.camera.currentText()} {self.extra_commands.text()} {self.scene_location.text()} "


package['cmdline']=f"{{render_command}}"
        
job['package'] = package
job['cpus'] = 2

env={{"HOME" :f"/render/{self.user}",  
        "RMANTREE":"/opt/software/pixar/RenderManProServer-24.4/",
        "PATH":"/opt/software/pixar/RenderManProServer-24.4/bin:/usr/bin:/usr/sbin:/opt/software/autodesk/maya2023/bin/",
        "MAYA_RENDER_DESC_PATH" : "/opt/software/pixar/RenderManForMaya-24.4/etc/:{ARNOLD_LOCATION}/:/opt/software/autodesk/maya2023/vray/rendererDesc/",
        "PIXAR_LICENSE_FILE":"9010@talavera.bournemouth.ac.uk",        
        "LD_LIBRARY_PATH" : "/usr/lib/:/usr/lib64:/render/jmacey/libs:{MAYA_ROOT}/lib/:/opt/software/vray_builds/vray/lib:",
        "HOME" : "/render/{self.user}",
        "MAYA_PLUG_IN_PATH" : "/opt/software/pixar/RenderManForMaya-24.4/plug-ins:{ARNOLD_LOCATION}/plug-ins/",
        "MAYA_SCRIPT_PATH" : "/opt/software/pixar/RenderManForMaya-24.4/scripts:/opt/software/autodesk/maya2023/vray/scripts",
        "PYTHONPATH" : f"{ARNOLD_LOCATION}/scripts",
        "ADSKFLEX_LICENSE_FILE" : "wrangle.bournemouth.ac.uk",
        "RLM_LICENSE" : "5063@burton.bournemouth.ac.uk", 
        "ARNOLD_LICENSE_ORDER" : "network",  
        "VRAY_AUTH_CLIENT_FILE_PATH" : "/opt/software/",
        "VRAY_OSL_PATH" : "/opt/software/vray_builds/vray/opensl",
        "VRAY_PLUGINS" :"/opt/software/vray_builds/maya_vray/vrayplugins",
        "VRAY_OSL_PATH_MAYA2023":"/opt/software/vray_builds/vray/opensl" 
         
        }}
job['env']=env

agendaRange = f'{range}'  
agenda = qb.genframes(agendaRange)

job['agenda'] = agenda
        
listOfJobsToSubmit = []
listOfJobsToSubmit.append(job)
listOfSubmittedJobs = qb.submit(listOfJobsToSubmit)
id_list=[]
for job in listOfSubmittedJobs:
    print(job['id'])
    id_list.append(job['id'])

print(id_list)
"""
        return payload

    def export_script(self) :
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,"Select Filename Name","payload.py",
            ("Python Files (*.py)"))
        if filename != "" :
            payload=self._generate_payload()
            with open("/Users/jmacey/tmp/payload.py","w") as file :
                file.write(payload)


    def submit_job(self) :
        payload=self._generate_payload()
        with tempfile.TemporaryDirectory() as tmpdirname:
            with open(tmpdirname+"/payload.py","w") as fp :
                fp.write(payload)
            output=subprocess.run(["/usr/bin/python3",f"{tmpdirname}/payload.py"],capture_output=True,env={})
            j=output.stdout.decode("utf-8") 
            print(j)            
            #hou.ui.displayMessage(f"Job submitted to Qube, ID's {j}",buttons=("Ok",),title="Job Submitted")
        self.done(0)
    
    
    def set_scene_location(self) :
        basicFilter = "*.mb;*.ma"
        cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=1)
        # work around for weird bug where window hides behind main one
        self.raise_()            

    def set_project_location(self) :
        cmds.fileDialog2( dialogStyle=3)
        # work around for weird bug where window hides behind main one
        self.raise_()            


        
if os.environ.get("QB_SUPERVISOR") is None :
    os.environ["QB_SUPERVISOR"]="tete.bournemouth.ac.uk"
    os.environ["QB_DOMAIN"]="ncca"


# If we have a dialog open already close
try:
    dialog.close()
    dialog.deleteLater()
except:
    pass

dialog = RenderFarmSubmitDialog()
dialog.show()