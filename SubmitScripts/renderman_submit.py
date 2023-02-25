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
    job['label']= 'RibGenLabel'
    
    # Below defines the name of the Qube! job 
    job['name'] = 'Rib Test'
    
    # Below defines how many Instances/subjobs the job is to spawn
    job['cpus'] = 1
    
    # Below defines the internal Qube! jobtype to be used to execute the job
    job['prototype'] = 'cmdline'
    
    # The below parameters are explained further in the "Job submission with job package explained" page
    package = {}
    job['package'] = package
    package['shell']="/bin/bash"

    job['package']['cmdline'] = 'cd /render/jmacey/corn ;  prman -d file /render/jmacey/corn/corn.000.rib'
    job['env']={
        "RMANTREE":"/opt/software/pixar/RenderManProServer-24.1/",
        "PATH":"/opt/software/pixar/RenderManProServer-24.1/bin:/usr/bin:/usr/sbin"}

	# Below defines the Agenda/Range of the job this will fill the Frames/Work section of the Qube! GUI
	# "0-60" is range 0-60
    agendaRange = '0-10'
    
    # Below defines the internal command required to generate the agenda 
    agenda = [] #qb.genframes(agendaRange)
    for i in range(0,1) :
        agenda.append({"name" :f"Test.{i:04}.exr" })
    print(agenda)
    #agenda=[]
    #work=qb.Work()

    # Below defines the job details for the agenda 
    job['agenda'] = agenda
    
    # Below appends the details of this task to the job dictionary for later submission
    task.append(job)

    	# Below submits the task list to Qube! 
    listOfSubmittedJobs = qb.submit(task)
    
    # Below prints out a list of jobs that have been submitted by name 
    for job in listOfSubmittedJobs:
    	print ('%(name)15s: %(id)s' % job)



# Below runs the "main" function
if __name__ == "__main__":
# This is the server to submit to
    if os.environ.get("QB_SUPERVISOR") is None :
        os.environ["QB_SUPERVISOR"]="tete.bournemouth.ac.uk"
        os.environ["QB_DOMAIN"]="ncca"

    main()
    sys.exit(0)
