#!/usr/bin/env python
import argparse
import os
import pathlib
import platform
# The next few lines attempt to import the Qube API. If the path to the qb module
# is not in $PATH or $PYTHONPATH, we will attempt to find it by looking in known
# locations   
import sys
from typing import List
from ProcessCommandLine import *

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

"""This is the entry point to submit a job to the farm. All the parameters are passed from the command line parser.

Parameters :
    project_name : str 
        the name of the project used in the submission
    cpus : int 
        the number of cpus for the job to use

Returns :
    None
"""

def main(project_name  :str , cpus : int, scene_file : str, start_frame : int , end_frame : int, by_frame : int, project_root :str,extra_env , image_file : str,remap : List[str] ,mode : str):

    home_dir=os.environ.get("HOME")
    user=os.environ.get("USER")

    job = {}
    job['name'] = project_name
    # This time, we will request 4 instances (previously known as subjobs).
    # By requesting 4 instances, assuming there are 4 open slots on the farm,
    # up to 4 agenda items will be processed simultaneously. 
    job['cpus'] = cpus

    # In the last example, we used the prototype 'cmdline' which implied a single
    # command being run on the farm.  This time, we will use the 'cmdrange' prototype
    # which tells Qube that we are running a command per agenda item.
    job['prototype'] = 'cmdrange'

    package = {}
    package['shell']="/bin/bash"
    # Just like the last example, we create a package parameter called 'cmdline'.
    # This is the command that will be run for every agenda item.  QB_FRAME_NUMBER,
    # however, is unique to cmdrange.  The text QB_FRAME_NUMBER will be replaced with
    # the actual frame number at run time.
    #scene=f"/render/{user}/{project_root}/{scene_file}"
    scene=scene_file
    print(f"submitting to {scene}")
    print(f"{project_root}")

    remap_path=""
    if len(remap) !=0  :
        remap_path=f'-remapPath "{remap[0]}={remap[1]}"'

    package['cmdline'] = f'/opt/software/vray_builds/maya_vray/bin/vray.bin -sceneFile={scene} {remap_path} -display=0 -frames=QB_FRAME_NUMBER -imgFile={image_file}'

    job['package'] = package
    
    env={"HOME" :f"/render/{user}",  
                "LD_LIBRARY_PATH" :"/opt/software/vray_builds/vray/lib/",
                "VRAY_AUTH_CLIENT_FILE_PATH" : "/opt/software/",
                "VRAY_OSL_PATH" : "/opt/software/vray_builds/vray/opensl",
                "VRAY_PLUGINS" :"/opt/software/vray_builds/maya_vray/vrayplugins",
                "VRAY_OSL_PATH_MAYA2020":"/opt/software/vray_builds/vray/opensl" }
    if extra_env != None :
        for en in extra_env :
            env[en[0]]=en[1]

    job['env']=env
    
    
   

    # Now we must create our agenda list.  This is an absolutely essential part of
    # submitting jobs with agenda items (i.e. frames).
    # First we define a range.  The range is in typical number range format where:
    #  1-5 means frames 1,2,3,4,5
    #  1,3,5 means frames 1,3, and 5
    #  1-5,7 means frames 1,2,3,4,5,7
    #  1-10x3 means frames 1,4,7,10
    agendaRange = f'{start_frame}-{end_frame}x{by_frame}'  # will evaluate to 0,10,20,30,40,50,60

    # Using the given range, we will create an agenda list using qb.genframes
    agenda = qb.genframes(agendaRange)

    # Now that we have a properly formatted agenda, assign it to the job
    job['agenda'] = agenda
        
    # As before, we create a list of 1 job, then submit the list.  Again, we
    # could submit just the single job w/o the list, but submitting a list is
    # good form.
    listOfJobsToSubmit = []
    listOfJobsToSubmit.append(job)
    if mode  :
        print(extra_env)
        print("*"*80)
        for key,value in job["env"].items() :
            print(f"[{key}] [{value}]")
        print("*"*80)
        print(job["package"]["cmdline"])
        print("*"*80);

    else :
        listOfSubmittedJobs = qb.submit(listOfJobsToSubmit)
        for job in listOfSubmittedJobs:
            print(job['id'])

# Below runs the "main" function
if __name__ == "__main__":

    # This is the server to submit to
    if os.environ.get("QB_SUPERVISOR") is None :
        os.environ["QB_SUPERVISOR"]="tete.bournemouth.ac.uk"
        os.environ["QB_DOMAIN"]="ncca"

    args=ProcessCommandLine()

    # now do some check to ensure command lines work ok and the user is not an idiot
    if args.start_frame > args.end_frame :
        print(f"start frame must be less then end frame  {args.start_frame} {args.end_frame}")
        print(f"For a single frame set -s 1 -e 1 \n")
        sys.exit(-1)

    if args.by_frame > (args.end_frame-args.start_frame) and args.by_frame !=1:
        print(f"Warning frame step of {args.by_frame} is greater than number of frames")
    # now check to see if file exist and is perhaps valid
    with open(args.scene_file) as scene:
        file_ok=False
        header = [next(scene) for x in range(5)]
        for h in header :
            if "V-Ray" in h :
                file_ok=True
        if not file_ok :    
            print(f"this doesn't look like a valid vray file")
            print("will attempt to use it but be warned")
    # We are going to auto setup the scene file to be on the farm for ease.
    # p=pathlib.Path(args.project_root)
    # if p.exists() :    
    #     project_root=p.parts[-1]
    #     print(f"{project_root}")
    # else :
    #     print(f"Project path is not valid \n")
    #     sys.exit()
    

    main(args.name,args.cpus,args.scene_file,args.start_frame,args.end_frame,args.by_frame,args.project_root,args.env,args.image_dir,args.remap,args.debug)



