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
print "               ncca Renderfarm Tool for Arndold                "
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

jobInstances=1
if jobNumFrames < 40:
    jobInstances = jobNumFrames
else:
    jobInstances = 40
jobFrameRange = startFrame+"-"+endFrame

jobProjectPath = "/render/"+userName+"/"+remote_project_data['pro_name']+"/"

countProjDirnameInstances = sum( 1 for _ in re.finditer(r'\b%s\b' % re.escape(remote_project_data['pro_name']), remote_project_data['scn_path']) )
jobSceneFile = "/render/"+userName+"/"+remote_project_data['scn_path'][remote_project_data['scn_path'].find(remote_project_data['pro_name']):len(remote_project_data['scn_path'])]+extNameOfScene
if (countProjDirnameInstances > 1):
    jobSceneFile = jobProjectPath + extNameOfScene

jobRenderEXEpath = "/opt/software/autodesk/maya"+MAYA_VERSION_ON_SERVER+"/bin/Render"

print ">> Searching for the render images directory",
# BUG: sftp cannot automatically change into a dir with spaces. 
#       ex >> sftp.listdir(variable_of_dir_with_spaces)
img_dir = "images"
sftp.chdir(remote_project_data['pro_name'])
if img_dir not in sftp.listdir():
    sftp.mkdir(img_dir)
    print "- created"
else:
    print "- found"
    if raw_input("   Would you like to use the default directory for the rendered images (y/n): ") == 'n':
        img_dir = raw_input("   Please enter a new name for the directory of the rendered images (NO SPACES): ")
        try:
            sftp.mkdir(img_dir)
        except IOError:
            print "   Cannot create <",img_dir,">"
            terminate()
        print "   Updated successfully to <",img_dir,">"
jobRdImages = jobProjectPath + img_dir
sftp.chdir("..")

jobCmdLine = jobRenderEXEpath+" -renderer arnold -rd \""+jobRdImages+"\" -s QB_FRAME_START -e QB_FRAME_END -proj \""+jobProjectPath+"\" \""+jobSceneFile+"\""

print
print "-- Job Info:"
print "  > Name:",jobName
print "  > Priority:",jobPriority
print "  > Number of frames:",jobNumFrames
print "  > Instances:",jobInstances
print "  > Frame range:",jobFrameRange
print "  > Project path:",jobProjectPath
print "  > Scene file:",jobSceneFile
print "  > Render EXE path:",jobRenderEXEpath
print "  > Rd Images path:",jobRdImages
print "  > Cmd Line:",jobCmdLine
print


# submit job to qube using the correct data strings.
print ">> Submitting job to Qube!"
job = qb.Job()
job['name']                     = jobName
job['prototype']                = 'cmdrange'
job['cpus']                     = jobInstances
job['priority']                 = jobPriority
job['hostorder']                = '+host.processor.avail'

package = {}
package['cmdline']                              = jobCmdLine
package['range']                                = jobFrameRange
package['validate_fileMinSize']                 = '2'
package['frameCount']                           = jobNumFrames

job['package']                  = package
job['agenda']                   = qb.genframes(package['range'])
job['flagsstring']              = 'auto_mount,convert_path'

environmentVars = { \
                    'MAYA_LOCATION' : '/opt/software/autodesk/maya'+MAYA_VERSION_ON_SERVER, \
                    'PYTHONPATH' : '/opt/software/autodesk/arnold/maya'+MAYA_VERSION_ON_SERVER+'/scripts', \
                    'MAYA_DISABLE_CIP' : '1', \
                    'LD_LIBRARY_PATH' : '$LD_LIBRARY_PATH:/opt/software/lib:/opt/software/autodesk/maya'+MAYA_VERSION_ON_SERVER+'/lib:/opt/software/autodesk/maya'+MAYA_VERSION_ON_SERVER+'/plug-ins/xgen/lib', \
                    'HOME' : '/render/'+userName, \
                    'PATH' : '$PATH:/bin:/usr/bin', \
                    'AW_LOCATION' : '/opt/software/autodesk', \
                    'ADSKFLEX_LICENSE_FILE' : '@'+MAYA_LICENSE_SERVER, \
                    'MAYA_RENDER_DESC_PATH' : '/opt/software/autodesk/arnold/maya'+MAYA_VERSION_ON_SERVER, \
                    'MAYA_PLUG_IN_PATH' : '/opt/software/autodesk/arnold/maya'+MAYA_VERSION_ON_SERVER+'/plug-ins' \
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


