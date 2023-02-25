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

        # row 0 project name
        label=QtWidgets.QLabel("Project Name")
        name=cmds.workspace(q=True,sn=True)
        self.gridLayout.addWidget(label,0,0,1,1)
        self.project_name = QtWidgets.QLineEdit(f"{self.user}_{name}", self)
        self.project_name.setToolTip("This is the name of the project as it will appear on the Qube GUI")
        self.gridLayout.addWidget(self.project_name, 0, 1, 1, 5)

        # row 1 select output drive
        self.select_output=QtWidgets.QPushButton("Camera")
        self.select_output.setToolTip("select camera to render")
        self.gridLayout.addWidget(self.select_output,1,0,1,1)
        self.camera = QtWidgets.QComboBox(self)
        self.camera.addItems(cmds.listCameras( p=True ))
        
        self.gridLayout.addWidget(self.camera, 1, 1, 1, 5)

        # row 2
        label=QtWidgets.QLabel("Start Frame")
        self.gridLayout.addWidget(label,2,0,1,1)
        self.start_frame=QtWidgets.QSpinBox()
        self.start_frame.setToolTip("Start frame for rendering, set from ROP but can be changed here, this will override the ROP value on the farm")

        self.start_frame.setRange(self.min_frame,self.max_frame)
        self.start_frame.setValue(self.min_frame)
        self.gridLayout.addWidget(self.start_frame,2,1,1,1)
        
        label=QtWidgets.QLabel("End Frame")
        self.gridLayout.addWidget(label,2,2,1,1)
        self.end_frame=QtWidgets.QSpinBox()
        self.end_frame.setRange(self.min_frame,self.max_frame)
        self.end_frame.setValue(self.max_frame)
        self.end_frame.setToolTip("End frame for rendering, set from ROP but can be changed here, this will override the ROP value on the farm")

        self.gridLayout.addWidget(self.end_frame,2,3,1,1)

        label=QtWidgets.QLabel("By Frame")
        self.gridLayout.addWidget(label,2,4,1,1)
        self.by_frame=QtWidgets.QSpinBox()
        self.by_frame.setValue(1)
        self.by_frame.setToolTip("Frame Step for rendering, set from ROP but can be changed here, this will override the ROP value on the farm")

        self.gridLayout.addWidget(self.by_frame,2,5,1,1)

        # row 3
        self.location_button=QtWidgets.QPushButton("Farm Location")
        self.location_button.setToolTip("Select the file to render, not this must be on the farm mount")
        self.gridLayout.addWidget(self.location_button,3,0,1,1)
        self.location_button.clicked.connect(self.set_farm_location)
        base_path=cmds.file(q=True, sn=True).split("/")[-2]
        
        location=f"/render/{self.user}/{base_path}/{cmds.file(q=True, sn=True, shn=True)}"
        self.farm_location = QtWidgets.QLineEdit(location, self)
        self.farm_location.setToolTip("""This is the full path to the hip file on the farm, you can enter this manually or press the button to select.
        If the farm is mounted on /render you can navigate to here and select the file. If not you must specify the full path and name manually. 
        If this is not correct the renders will fail""")
        self.gridLayout.addWidget(self.farm_location, 3, 1, 1, 5)
   

        # row 4
        # cancel button

        self.Cancel = QtWidgets.QPushButton("Cancel", self)
        self.Cancel.setToolTip("Close the submit dialog")
        self.Cancel.clicked.connect(self.close)
        self.gridLayout.addWidget(self.Cancel, 4, 0, 1, 1)

        # Screen Shot button

        self.submit = QtWidgets.QPushButton("Submit", self)
        self.submit.pressed.connect(self.submit_job)
        self.submit.setEnabled(True)
        self.submit.setToolTip("Submit job to the farm, you must select a ROP before this will activate")
        self.gridLayout.addWidget(self.submit, 4, 5, 1, 1)


    def submit_job(self) :
        range=f"{self.start_frame.value()}-{self.end_frame.value()}x{self.by_frame.value()}"
        payload=f"""
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

render_command=f"Render -s QB_FRAME_NUMBER -e QB_FRAME_NUMBER -r renderman -proj {self.project.text()} -cam {self.camera.currentText()} {self.farm_location.text()} "


package['cmdline']=f"{{render_command}}"
        
job['package'] = package
job['cpus'] = 2
   
env={{"HOME" :f"/render/{self.user}",  
        "RMANTREE":"/opt/software/pixar/RenderManProServer-24.4/",
        "PATH":"/opt/software/pixar/RenderManProServer-24.4/bin:/usr/bin:/usr/sbin:/opt/software/autodesk/maya2023/bin/",
        "MAYA_RENDER_DESC_PATH" : "/opt/software/pixar/RenderManForMaya-24.4/etc/",
        "PIXAR_LICENSE_FILE":"9010@talavera.bournemouth.ac.uk",        
        "LD_LIBRARY_PATH" : "/usr/lib/:/usr/lib64:/render/jmacey/libs",
        "HOME" : "/render/jmacey",
        "MAYA_PLUG_IN_PATH" : "/opt/software/pixar/RenderManForMaya-24.4/plug-ins",
        "MAYA_SCRIPT_PATH" : "/opt/software/pixar/RenderManForMaya-24.4/scripts"
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
        with tempfile.TemporaryDirectory() as tmpdirname:
            with open(tmpdirname+"/payload.py","w") as fp :
                fp.write(payload)
            output=subprocess.run(["/usr/bin/python3",f"{tmpdirname}/payload.py"],capture_output=True,env={})
            j=output.stdout.decode("utf-8") 
            
            hou.ui.displayMessage(f"Job submitted to Qube, ID's {j}",buttons=("Ok",),title="Job Submitted")
        self.done(0)
    
    
    def set_farm_location(self) :
        basicFilter = "*.mb;*.ma"
        cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=1)
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

    
