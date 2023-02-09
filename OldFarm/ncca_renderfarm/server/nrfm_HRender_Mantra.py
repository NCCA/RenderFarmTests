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
print "            ncca Renderfarm Tool for HRender Mantra            "
print
print "Creator: Constantinos Glynos"
print "Created Date: 13/07/2016"
print "Updated Date: 07/02/2022"
print "Organisation: Bournemouth University"
print
print


import sys

tools_path = '/public/bin/ncca_renderfarm/server/tools/'

if not tools_path in sys.path:
    sys.path.append(tools_path)

# importing necessary libs and paths to this script.
from setup_env import *
cc()


#==========================================================#


# reading from rnd_info.txt file the passed data.
sceneData = getSceneData(USER_PATH+'/houdini'+HOUDINI_VERSION+'/rnd_info.txt')

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
ifdInfo = [(sceneData[9]).strip(),(sceneData[10]).strip()]
server = userName+"@tete:"+userRemotePath
sftp = None

print
print "-- Scene Info:"
print "  > User local path:",userLocalPath
print "  > User remote path:",userRemotePath
print "  > User name:",userName
print "  > Project directory path:",local_project_data['pro_path']
print "  > Project directory name:",local_project_data['pro_name']
print "  > Current Local Scene Path:",local_project_data['scn_path']
print "  > Scene Ext:",extNameOfScene
print "  > Scene Name:",justNameOfScene
print "  > Start Frame:",startFrame
print "  > End Frame:",endFrame
print "  > Frame Padding:",framePadding
print "  > Renderer Node:",rendererNode
print "  > Ifd info:",ifdInfo
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
print ">> Accessing Qube.."

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
#if " " in jobProjectPath:
#    jobProjectPath = jobProjectPath.replace(" ","\\ ")

countProjDirnameInstances = sum( 1 for _ in re.finditer(r'\b%s\b' % re.escape(remote_project_data['pro_name']), remote_project_data['scn_path']) )
jobSceneFile = "/render/"+userName+"/"+remote_project_data['scn_path'][remote_project_data['scn_path'].find(remote_project_data['pro_name']):len(remote_project_data['scn_path'])]+extNameOfScene
#if " " in jobSceneFile:
#    jobSceneFile = jobSceneFile.replace(" ","\\ ")
if (countProjDirnameInstances > 1):
    jobSceneFile = jobProjectPath + extNameOfScene

jobFramePadding = 0
if ifdInfo[0] == "True":
    jobFramePadding = ifdInfo[1]
else:
    jobFramePadding = framePadding

# BUG: HRender cannot evaluate paths with spaces even when in quotes. The same code in HBatch works fine.
jobShell = "/bin/bash"
jobRenderEXEpath = "/opt/software/hfs"+HOUDINI_VERSION+'.'+HOUDINI_SUBVERSION+"; source houdini_setup_bash;"
cmd_flags = "-e -f QB_FRAME_START QB_FRAME_END -i QB_FRAME_STEP"
jobCmdTmpl = "cd "+jobRenderEXEpath+" %(csh)s \"%(hrender)s\" "+cmd_flags+" %(driver_cop_arg)s %(driver_cop_value)s %(argv)s %(scenefile)s"
jobCmdLine = "cd "+jobRenderEXEpath+" \"hrender\" "+cmd_flags+" -d /out/"+rendererNode+" -R \"QB_CONVERT_PATH("+jobSceneFile+")\""

print
print "-- Job Info:"
print "  > job Name:",jobName
print "  > job Priority:",jobPriority
print "  > job Number of Frames:",jobNumFrames
print "  > job Instances:",jobInstances
print "  > job Frame Range:",jobFrameRange
print "  > job Frame Padding:",jobFramePadding
print "  > job Project Path:",jobProjectPath
print "  > job Scene File:",jobSceneFile
print "  > job Render EXE path:",jobRenderEXEpath
print "  > job Shell:",jobShell
print "  > job Cmd Tmpl:",jobCmdTmpl
print "  > job Cmd Line:",jobCmdLine
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
package['shell']                                = jobShell
package['log_output_file']                      = "\""+jobProjectPath+"/log.txt\""
package['cmdTemplate']                          = jobCmdTmpl
package['cmdline']                              = jobCmdLine
package['scenefile']                            = "\""+jobSceneFile+"\""
package['padding']                              = jobFramePadding
package['-R']                                   = 1
package['simpleCmdType']                        = "Houdini (hrender)"
package['frameCount']                           = jobNumFrames
package['driver_cop_arg']                       = "-d"
package['driver_cop_value']                     = "/out/"+rendererNode
package['range']                                = jobFrameRange
package['outputLogfile']                        = "\""+jobProjectPath+"/log.txt\""

job['package']                  = package
job['agenda']                   = qb.genframes(package['range'])
job['flagsstring']              = 'auto_mount,convert_path'

environmentVars =   { \
                            'HOUDINI_USE_HFS_PYTHON':'1', \
                            'SESI_LMHOST':HOUDINI_LICENSE_SERVER \
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
        openProjectDirectoryOnServer(userName,"sftp://tete/home/"+userName+"/"+remote_project_data['pro_name'])
    except:
        print "ERROR >> Ooops! Something went wrong.."
        print "         Please wrangle your renders from Qube instead."


# close the connection and delete qb, sftp and transport objects.
del qb
sftp.close()
transport.close()
del sftp, transport
terminate()


