#!/usr/bin/env python
# Below are required imports for the script to run
import os, sys
# The next few lines attempt to import the Qube API. If the path to the qb module
# is not in $PATH or $PYTHONPATH, we will attempt to find it by looking in known
# locations   
import sys
sys.path.insert(0,"/usr/local/pfx/qube/api/python/")
import qb
 
# Below is the main function to run in this script 
def main():
    
    # ----------------Start creation of Parent Job----------------------------------------
    
    # Below defines an empty list for combining all tasks in the dependancy chain
    task = []
    
    # Below creates an empty dictionary to be filled by the following lines of code 
    job = {}
    
    # Below defines a label for the dependancy to be used internally within this script
    job['label']= 'VRayTest'
    
    # Below defines the name of the Qube! job 
    job['name'] = 'Testing VRAY Export'
    
    # Below defines how many Instances/subjobs the job is to spawn
    job['cpus'] = 1
    
    # Below defines the internal Qube! jobtype to be used to execute the job
    job['prototype'] = 'cmdrange'
    
    # The below parameters are explained further in the "Job submission with job package explained" page
    package = {}
    job['package'] = package
    job['package']['cmdline'] = '/opt/software/vray_builds/maya_vray/bin/vray.bin -sceneFile=/render/jmacey/jmacey/FarmTest/VRayExport/TestVray_0001.vrscene -display=0 -frames=QB_FRAME_NUMBER'

    



    job['package']['simpleCmdType'] = 'VRay Batch'
    job['package']['env']={"HOME" :"/render/jmacey",  "LD_LIBRARY_PATH" : "/opt/software/vray_builds/vray/lib/", "VRAY_AUTH_CLIENT_FILE_PATH" : "/opt/software/", "VRAY_OSL_PATH" : "/opt/software/vray_builds/vray/opensl", "VRAY_PLUGINS" :"/opt/software/vray_builds/maya_vray/vrayplugins"}

	# Below defines the Agenda/Range of the job this will fill the Frames/Work section of the Qube! GUI
	# "0-60" is range 0-60
    agendaRange = '0-10'
    
    # Below defines the internal command required to generate the agenda 
    agenda = qb.genframes(agendaRange)
    
    # Below defines the job details for the agenda 
    job['agenda'] = agenda
    
    # Below appends the details of this task to the job dictionary for later submission
    task.append(job)
	
	# # ----------------Start creation of Child Job----------------------------------------
	
	
	# # Below creates an empty dictionary to be filled by the following lines of code
    # job = {}
    
    # # Below defines a label for the dependancy to be used internally within this script
    # job['label']= 'VRayTest'
    
    # # Below defines the dependancy of this job see below for possible dependancy strings
    # job['dependency'] = 'link-complete-job-RibGenLabel'
    
    # # Below defines the name of the Qube! job
    # job['name'] = 'Renderman Render Job TUTORIAL'
    
    # # Below defines how many Instances/subjobs the job is to spawn
    # job['cpus'] = 2
    
    # # Below defines how many Instances/subjobs the job is to spawn
    # job['prototype'] = 'renderman'
    
    # # The below parameters are explained further in the "Job submission with job package explained" page
    # package = {}
    # job['package'] = package
    # job['package']['cmdline'] = 'prman --version'
    # job['package']['simpleCmdType'] = 'Renderman Job'
    # job['env']={
    #     "RMANTREE":"/opt/software/pixar/RenderManProServer-24.1/",
    #     "LD_LIBRARY_PATH":"/usr/lib:/usr/lib64:/opt/software/pixar/RenderManProServer-24.1/lib",
    #     "PATH":"$RMANTREE/bin"}
    # # Below appends the details of this task to the job dictionary for later submission
    # task.append(job)

	# Below submits the task list to Qube! 
    listOfSubmittedJobs = qb.submit(task)
    
    # Below prints out a list of jobs that have been submitted by name 
    for job in listOfSubmittedJobs:
    	print ('%(name)15s: %(id)s' % job)


# Below runs the "main" function
if __name__ == "__main__":
    main()
    sys.exit(0)