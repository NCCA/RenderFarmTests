import os
import platform
import sys

import hou
from PySide2 import QtCore, QtWidgets

try :
    import qb
except ImportError :
    if platform.system() == "Linux" :
       # Here I assume the NCCA Lab location
       sys.path.insert(0,"/public/devel/2022/pfx/qube/api/python/")
    elif platform.system() == "Darwin" :
        # On my mac here 
        sys.path.insert(0,"/Applications/pfx/qube/api/python")
    else :
        # For now no Windows!
        print("can't find Qube Python API")
        sys.exit()


import qb


class RenderFarmSubmitDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Move to Build mode
        # Set the GUI components and layout
        self.setWindowTitle("NCCA Renderfarm Submit Tool")
        self.resize(600, 280)
        # Main layout for form
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.home_dir=os.environ.get("HOME")
        self.user=os.environ.get("USER")
        name=hou.hipFile.basename()
        name=name[0:name.find('.')]
        frames=hou.playbar.frameRange()
        self.min_frame=frames[0]
        self.max_frame=frames[1]

        # row 0 project name
        label=QtWidgets.QLabel("Project Name")
        self.gridLayout.addWidget(label,0,0,1,1)
        self.project_name = QtWidgets.QLineEdit(f"{self.user}_{name}", self)
        self.project_name.setToolTip("This is the name of the project as it will appear on the Qube GUI")
        self.gridLayout.addWidget(self.project_name, 0, 1, 1, 5)

        # row 1 select output drive
        self.select_output=QtWidgets.QPushButton("Select ROP")
        self.select_output.setToolTip("Select the output ROP to render, these will be either in the /shop or /stage level")
        self.select_output.clicked.connect(self.select_output_driver)
        self.gridLayout.addWidget(self.select_output,1,0,1,1)
        self.output_driver = QtWidgets.QLineEdit(self)
        self.output_driver.setReadOnly(True)
        self.gridLayout.addWidget(self.output_driver, 1, 1, 1, 5)

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
        base_path=hou.hipFile.path().split("/")[-2]
        location=f"/render/{self.user}/{base_path}/{hou.hipFile.basename()}"
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
        self.submit.setEnabled(False)
        self.submit.setToolTip("Submit job to the farm, you must select a ROP before this will activate")
        self.gridLayout.addWidget(self.submit, 4, 5, 1, 1)


    def submit_job(self) :
        job = {}
        job['name'] = self.project_name.text()
        
        # In the last example, we used the prototype 'cmdline' which implied a single
        # command being run on the farm.?? This time, we will use the 'cmdrange' prototype
        # which tells Qube that we are running a command per agenda item.
        job['prototype'] = 'cmdrange'
 
        package = {}
        package['shell']="/bin/bash"
        pre_render="cd /opt/software/hfs19.5.303/; source houdini_setup_bash; "
        render_command=f"hython $HB/hrender.py -e -F QB_FRAME_NUMBER -R -d {self.output_driver.text()} {self.farm_location.text()} "
        package['cmdline']=f" {pre_render} {render_command}"
        
        
        job['package'] = package
        
        env={"HOME" :f"/render/{self.user}",  
                    "SESI_LMHOST" : "hamworthy.bournemouth.ac.uk",
                    "PIXAR_LICENSE_FILE" : "9010@talavera.bournemouth.ac.uk",            
                    }
        job['env']=env

        agendaRange = f'{self.start_frame.value()}-{self.end_frame.value()}x{self.by_frame.value()}'  # will evaluate to 0,10,20,30,40,50,60

        # Using the given range, we will create an agenda list using qb.genframes
        agenda = qb.genframes(agendaRange)
    
        # Now that we have a properly formatted agenda, assign it to the job
        job['agenda'] = agenda
        
        
        # As before, we create a list of 1 job, then submit the list.  Again, we
        # could submit just the single job w/o the list, but submitting a list is
        # good form.
        listOfJobsToSubmit = []
        listOfJobsToSubmit.append(job)
        listOfSubmittedJobs = qb.submit(listOfJobsToSubmit)
        id_list=[]
        for job in listOfSubmittedJobs:
            print(job['id'])
            id_list.append(job['id'])
        hou.ui.displayMessage(f"Job submitted to Qube, ID's {id_list}",buttons=("Ok",),title="Job Submitted")

        self.done(0)
    
    def closeEvent(self,event) :    
        super(RenderFarmSubmitDialog, self).closeEvent(event)

    def set_farm_location(self) :
        file_and_path=hou.ui.selectFile(None,"Choose file on Farm",False,hou.fileType.Hip,"","",False,False,hou.fileChooserMode.Write)
        if file_and_path == "" :
                return
        if "$HOME" in file_and_path :
                file_and_path=file_and_path.replace("$HOME",str(hou.getenv("HOME"))) 
        elif "$HIP" in file_and_path :
                file_and_path=file_and_path.replace("$HIP",str(hou.getenv("HIP"))) 
        elif "$JOB" in file_and_path :
                file_and_path=file_and_path.replace("$JOB",str(hou.getenv("JOB"))) 
        self.farm_location.setText(file_and_path)



    def select_output_driver(self) :
        output=hou.ui.selectNode(node_type_filter=hou.nodeTypeFilter.Rop)
        # work around for weird bug where window hides behind main one
        self.raise_()            

        if output != None :
            self.submit.setEnabled(True)
            self.output_driver.setText(output)
            frame_values=hou.node(output).parmTuple("f").eval()    
            
            if len(frame_values) == 3 :
                self.start_frame.setValue(int(frame_values[0]))
                self.end_frame.setValue(int(frame_values[1]))
                self.by_frame.setValue(int(frame_values[2]))
        
if os.environ.get("QB_SUPERVISOR") is None :
    os.environ["QB_SUPERVISOR"]="tete.bournemouth.ac.uk"
    os.environ["QB_DOMAIN"]="ncca"
dialog = RenderFarmSubmitDialog()
dialog.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.WindowStaysOnTopHint)
dialog.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
dialog.show()
