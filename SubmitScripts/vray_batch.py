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

    job = {}
    job['name'] = 'Multi frame vray'
    # This time, we will request 4 instances (previously known as subjobs).
    # By requesting 4 instances, assuming there are 4 open slots on the farm,
    # up to 4 agenda items will be processed simultaneously. 
    job['cpus'] = 4

    # In the last example, we used the prototype 'cmdline' which implied a single
    # command being run on the farm.  This time, we will use the 'cmdrange' prototype
    # which tells Qube that we are running a command per agenda item.
    job['prototype'] = 'cmdrange'

    package = {}

    # Just like the last example, we create a package parameter called 'cmdline'.
    # This is the command that will be run for every agenda item.  QB_FRAME_NUMBER,
    # however, is unique to cmdrange.  The text QB_FRAME_NUMBER will be replaced with
    # the actual frame number at run time.
    package['cmdline'] = '/opt/software/vray_builds/maya_vray/bin/vray.bin -sceneFile=/render/jmacey/jmacey/FarmTest/scenes/SingleFileVrrayExport.vrscene   -display=0 -frames=QB_FRAME_NUMBER'

    job['package'] = package
 
    job['env']={"HOME" :"/render/jmacey",  
                "LD_LIBRARY_PATH" :"/opt/software/vray_builds/vray/lib/",
                "VRAY_AUTH_CLIENT_FILE_PATH" : "/opt/software/",
                "VRAY_OSL_PATH" : "/opt/software/vray_builds/vray/opensl",
                "VRAY_PLUGINS" :"/opt/software/vray_builds/maya_vray/vrayplugins",
                "VRAY_OSL_PATH_MAYA2020":"/opt/software/vray_builds/vray/opensl" }
   

    # Now we must create our agenda list.  This is an absolutely essential part of
    # submitting jobs with agenda items (i.e. frames).
    # First we define a range.  The range is in typical number range format where:
    #  1-5 means frames 1,2,3,4,5
    #  1,3,5 means frames 1,3, and 5
    #  1-5,7 means frames 1,2,3,4,5,7
    #  1-10x3 means frames 1,4,7,10
    agendaRange = '0-120x10'  # will evaluate to 0,10,20,30,40,50,60

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
