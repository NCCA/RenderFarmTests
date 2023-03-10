#!/usr/bin/env python
# Below are required imports for the script to run
import os
import platform
# The next few lines attempt to import the Qube API. If the path to the qb module
# is not in $PATH or $PYTHONPATH, we will attempt to find it by looking in known
# locations   
import sys

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


# Below is the main function to run in this script
def main():
     

    # Below defines an empty list for combining all tasks in the dependancy chain
    task = []
    
    # Below creates an empty dictionary to be filled by the following lines of code 
    job = {}
    
    # Below defines a label for the dependancy to be used internally within this script
    job['label']= 'Arnold'
    
    # Below defines the name of the Qube! job 
    job['name'] = 'Arnold Render Test'
    
    # Below defines how many Instances/subjobs the job is to spawn
    job['cpus'] = 18
    job['hosts']="tete16"
    # Below defines the internal Qube! jobtype to be used to execute the job
    job['prototype'] = 'cmdrange'
    
    # The below parameters are explained further in the "Job submission with job package explained" page
    package = {}
    job['package'] = package
    package['shell']="/bin/bash"

    package['cmdline'] = 'Render  -ai:ltf 1 -ai:lve 3 -s QB_FRAME_NUMBER -e QB_FRAME_NUMBER -rd /render/jmacey/output  -im WM  -r arnold -proj /render/jmacey/FarmTest -cam persp /render/jmacey/FarmTest/scenes/ArnoldTest.ma '
    ARNOLD_LOCATION='/opt/software/autodesk/arnold/maya2020'
    MAYA_ROOT='/opt/software/autodesk/maya2020/'
    env={"HOME" :"/render/jmacey",  
                "PATH":f"/usr/bin:/usr/sbin:{MAYA_ROOT}/bin/",
                "MAYA_RENDER_DESC_PATH" :f"{ARNOLD_LOCATION}/",
                "LD_LIBRARY_PATH" : f"/usr/lib/:/usr/lib64:/render/jmacey/libs:{MAYA_ROOT}/lib/:{MAYA_ROOT}/plug-ins/xgen/lib/",
                "MAYA_PLUG_IN_PATH" :f"{ARNOLD_LOCATION}/plug-ins/",
                #"RLM_LICENSE" :"@wrangle.bournemouth.ac.uk",
                #  "MAYA_SCRIPT_PATH" :f"{VRAY_ROOT_MAYA}/scripts/",
                #  "VRAY_FOR_MAYA2023_MAIN" : f"{VRAY_ROOT}/",
                "ARNOLD_LICENSE_ORDER" : "network",
                "MAYA_DISABLE_CIP" : "1",
                "ADSKFLEX_LICENSE_FILE" : "@hamworthy.bournemouth.ac.uk",
                "ARNOLD_LICENSE_MANAGER" : "@hamworthy.bournemouth.ac.uk",
                "LM_LICENSE_FILE" : "@hamworthy.bournemouth.ac.uk",
                "RLM_LICENSE" : "@hamworthy.bournemouth.ac.uk",
                "solidangle_LICENSE" : "@hamworthy.bournemouth.ac.uk",
                "PYTHONPATH" : f"{ARNOLD_LOCATION}/scripts",
                
                }

    job['env']=env
	# Below defines the Agenda/Range of the job this will fill the Frames/Work section of the Qube! GUI
	# "0-60" is range 0-60
    agendaRange = '1-1x1'
    
    # Below defines the internal command required to generate the agenda 
    agenda =qb.genframes(agendaRange)
    
    # Below defines the job details for the agenda 
    job['agenda'] = agenda
    listOfJobsToSubmit = []
    listOfJobsToSubmit.append(job)
    
    # Below prints out a list of jobs that have been submitted by name 
    listOfSubmittedJobs = qb.submit(listOfJobsToSubmit)
    for job in listOfSubmittedJobs:
        print(job['id'])

# Below runs the "main" function
if __name__ == "__main__":
# This is the server to submit to
    if os.environ.get("QB_SUPERVISOR") is None :
        os.environ["QB_SUPERVISOR"]="tete.bournemouth.ac.uk"
        os.environ["QB_DOMAIN"]="ncca"

    main()
    sys.exit(0)
