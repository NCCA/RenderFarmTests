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
     
    # Below creates an empty dictionary to be filled by the following lines of code
    job = {}
     
    # Below defines the name of the Qube! job.  This is the name that will be
    # displayed in the GUI and through the command line tools
    job['name'] = 'Prman Test'
    # Below defines how many Instances/subjobs the job is to spawn.  Because we
    # will be running only a single command, there is no need to request more than 1. 
    job['cpus'] = 1
     
    # Below defines the internal Qube! jobtype to be used to execute the job.
    # 'cmdline' tells Qube that on the backend, we will execute a single command line
    # command.  This will be the same as opening a terminal/command prompt and typing
    # out a command.
    job['prototype'] = 'cmdline'
    job['env']={
        "RMANTREE":"/opt/software/pixar/RenderManProServer-24.1/",
        "LD_LIBRARY_PATH":"/usr/lib:/usr/lib64:/opt/software/pixar/RenderManProServer-24.1/lib",
        "PATH":"/opt/software/pixar/RenderManProServer-24.1/bin:/opt/software/autodesk/maya/bin:/usr/bin",
        "MAYA_LOCATION":"/opt/software/autodesk/maya/"}
     
    # The below parameters are explained further in the "Job submission with job
    # package explained" page
    package = {}
    package['cmdline'] = 'ls -al /opt/software/autodesk/arnold' #'Render  TestMaya.ma'

    job['package'] = package
     
    # Below creates an empty list filled by the following lines of code.
    listOfJobsToSubmit = []
     
    # Below evaluates the jobs to be submitted and adds the to the above list
    listOfJobsToSubmit.append(job)
     
    # Below calls the list of jobs to be submitted and then prints the job IDs for each
    # While it is not strictly necessary that one submits a list of jobs, it is a good
    # habit to start, so we will only submit lists of jobs.  It is, however, perfectly
    # acceptable to qb.submit(job)
    listOfSubmittedJobs = qb.submit(listOfJobsToSubmit)
    for job in listOfSubmittedJobs:
        print(job['id'])
# Below runs the "main" function
if __name__ == "__main__":
    main()
    sys.exit(0)
