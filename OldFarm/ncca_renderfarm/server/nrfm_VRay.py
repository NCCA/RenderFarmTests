#!/usr/bin/env python


#=========================================================================================#
# ncca_RenderFarm
#
# AUTHOR:           Constantinos Glynos
#                   (cglynos@bournemouth.ac.uk)
#
# Copyright (C) 2016-2019 Constantinos Glynos
#
# CREATION DATE:    13/07/2016
#
# UPDATED DATE:     07/02/2022
#
# VERSION:          8.2
#
# DESCRIPTION:      This is the ncca_Renderfarm tool. It allows the ncca students to
#                   render their sequence using the renderfarm by clicking on the
#                   ncca_RenderFarm icon under the Rendering shelf in Maya and Houdini.
#                   The tool works under Linux and Windows.
#
# HOW TO USE:       Install and click on the icon in the rendering shelf, follow the 
#                   instructions and wrangle. The user is responsible for retrieving the
#                   completed renders from his/her home directory on the server.      
#
#=========================================================================================#


print
print "---------------------------------------------------------------"
print "                 ncca Renderfarm Tool for V-Ray                "
print
print "Creator: Constantinos Glynos"
print "Created Date: 13/07/2016"
print "Updated Date: 07/02/2022"
print "Organisation: Bournemouth University"
print
print


import sys, platform

if platform.system() == 'Linux':
    tools_path = '/public/bin/ncca_renderfarm/server/tools/'
else:
    tools_path = '//bournemouth.ac.uk/Data/Student/Public/Schools/FMC/NCCA/Renderfarm/ncca_renderfarm/server/tools/'

if not tools_path in sys.path:
    sys.path.append(tools_path)

# importing necessary libs and paths to this script.
from setup_env import *
cc()


#==========================================================#


# reading from rnd_info.txt file the passed data.
sceneData = getSceneData(USER_PATH+'/maya/rnd_info.txt')

# reading from file and stripping the leading and final spaces
userLocalPath = (sceneData[0]).strip()
userName = (os.path.basename(userLocalPath)).strip()
userRemotePath = "/home/"+userName
local_project_path = (sceneData[1]).strip()
local_project_name = (os.path.basename(local_project_path[:-1])).strip()
local_scene_path = (sceneData[2]).strip()
local_project_data = {'pro_path':local_project_path,'pro_name':local_project_name,'scn_path':local_scene_path}
extNameOfScene = (sceneData[3]).strip()
justNameOfScene = (sceneData[4]).strip()
startFrame = (sceneData[5]).strip()
endFrame = (sceneData[6]).strip()
framePadding = (sceneData[7]).strip()
rendererNode = (sceneData[8]).strip()
try:
    animFrames = (sceneData[9]).strip()
except:
    animFrames = None
server = userName+"@tete:"+userRemotePath
sftp = None

print
print "-- Scene Info:"
print "  > User local path:",userLocalPath
print "  > User remote path:",userRemotePath
print "  > User name:",userName
print "  > Project directory path:",local_project_data['pro_path']
print "  > Project directory name:",local_project_data['pro_name']
print "  > Current local scene path:",local_project_data['scn_path']
print "  > Scene name with extension:",extNameOfScene
print "  > Scene name:",justNameOfScene
print "  > Renderer:",rendererNode
print "  > Start frame:",startFrame
print "  > End frame:",endFrame
print "  > Frame padding:",framePadding
print "  > Anim frames (Vray specific):",animFrames
print "  > Server:",server
print
print colour.BOLD+colour.WARNING+"*****"
print "PLEASE DO NOT CONTINUE TO WORK ON YOUR PROJECT WHILE RUNNING THE RENDERFARM TOOL"
print "*****"+colour.END
print


# find and import paramiko. checkParamiko will exit the tool if paramiko is not loaded.
try:
    paramiko = checkParamiko(local_project_data['pro_path'])
except Exception as ex:
    terminate(ex)
print

# check for the duplicated project dirs on the server.
try:
    project_instances,sftp,transport = findProjectInstances(userRemotePath,local_project_data['pro_name'],sftp,paramiko)
except Exception as ex:
    terminate(ex)
print

# rename or overwrite duplicated project directory on server.
try:
    remote_project_data = resolveProjectDuplication(project_instances,local_project_data,sftp)
except Exception as ex:
    terminate(ex)
print

# fixing .vrscene file
try:
    jobProjectPath = "/render/"+userName+"/"+remote_project_data['pro_name']+"/"
    fixVRScene(jobProjectPath,local_project_data['pro_path'],remote_project_data['pro_path'],justNameOfScene)
    jobVRScene_file_path = jobProjectPath+justNameOfScene+".vrscene"
except Exception as ex:
    terminate(ex)
print

# create a project dir and upload all the contents.
try:
    uploadProject(remote_project_data,local_project_data,server,sftp)
except Exception as ex:
    terminate(ex)
print

# check the server quota before rendering.
try:
    checkQuota(userRemotePath,sftp)
except Exception as ex:
    terminate(ex)
print



# access qube and setup all variables to match the renderfarm's standard.
print
print ">> Accessing Qube."

jobName = userName+"_"+justNameOfScene+"_Pro("+remote_project_data['pro_name']+")"
jobPriority = 9999
jobNumFrames = int(endFrame) - int(startFrame) + 1
if animFrames != None:
    jobNumFrames = 0
    ranges = animFrames.split(",")
    for i in ranges:
        nums = i.split("-")
        jobNumFrames += (int(nums[1])-int(nums[0]))+1
        #print "(DEBUG) --------",type(i),":",nums,":",jobNumFrames

jobInstances=1
if jobNumFrames < 40:
    jobInstances = jobNumFrames
else:
    jobInstances = 40
jobFrameRange = startFrame+"-"+endFrame
if animFrames != None:
    jobFrameRange = animFrames

jobCmdLine = "/opt/software/vray_builds/maya_vray/bin/vray.bin -sceneFile=\""+jobVRScene_file_path+"\" -display=0 -frames=QB_FRAME_NUMBER"
jobFramePadding = framePadding

print
print "-- Job Info:"
print "  > Name:",jobName
print "  > Priority:",jobPriority
print "  > Number of frames:",jobNumFrames
print "  > Instances:",jobInstances
print "  > Frame range:",jobFrameRange
print "  > Project path:",jobProjectPath
print "  > Scene file:",extNameOfScene
print "  > Cmd Line:",jobCmdLine
print

# submit job to qube using the correct data strings.
print "-- Submitting job to Qube!"
job = qb.Job()
job['name']                     = jobName
job['prototype']                = 'cmdrange'
job['cpus']                     = jobInstances
job['priority']                 = jobPriority

package = {}
package['shell']                = '/bin/bash'
package['padding']              = jobFramePadding
package['cmdline']              = jobCmdLine
package['range']                = jobFrameRange
package['frameCount']           = jobNumFrames

job['package']                  = package
job['agenda']                   = qb.genframes(package['range'])
job['flagsstring']              = 'auto_mount'

environmentVars = { \
                    'HOME':"/render/"+userName, \
                    'VRAY_AUTH_CLIENT_FILE_PATH' : '/opt/software/', \
                    'VRAY_OSL_PATH' : '/opt/software/vray_builds/vray/opensl', \
                    'LD_LIBRARY_PATH' : '/opt/software/vray_builds/vray/lib', \
                    'VRAY_PLUGINS' : '/opt/software/vray_builds/maya_vray/vrayplugins' \
                  }
job['env']                      = environmentVars
job['cwd']                      = userRemotePath
job['mail_address']             = userName

if raw_input(">> Continue? (y/n): ") == 'y':
    qb.submit(job)
    
    print
    print "-------------------------------------------------------------"
    
    # wrangle renders from terminal using the callback script.
    try:
        status = wrangle(userName,qb)
        if using_linux_os():
            openProjectDirectoryOnServer(userName,"sftp://tete/home/"+userName+"/"+remote_project_data['pro_name'])
        else:
            print ">> The ncca renderfarm tool cannot access tete from Windows."
            print "   Please use FileZilla or WinSCP to find the project directory on the server."
    except:
        print "ERROR >> Ooops! Something went wrong.."
        print "         Please wrangle your renders from Qube instead."


# close the connection and delete qb, sftp and transport objects.
del qb
sftp.close()
transport.close()
del sftp, transport
terminate()


