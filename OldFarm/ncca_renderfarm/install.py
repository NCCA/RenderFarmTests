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


from loader import *


print
print "-- Installing the NCCA RenderFarm tool --"
print


#==========================================================#


def readData(mainFile_, fixStr=True):
    file_data = None
    try:
        with open(mainFile_, 'r') as mf:
            file_data = mf.readlines()
    except:
        print "- failed"
        print "ERROR >> The main tool is not accessible!"
        print "         Please contact the Animation Demonstrators (w109)."
        return None

    data = None

    if fixStr == True:
        raw_data = []
        for line in file_data:
            rl = repr(line)
            if rl.startswith('"'):
                rl = rl.strip('""')
            else:
                rl = rl.strip("''")
            raw_data.append(rl)
        raw_data = ''.join(raw_data)
        raw_data = raw_data.replace('\"','\\\"')
        data = raw_data
    else:
        data = ''.join(file_data)

    return data


def mayaInstall(version_):
    mayaPath = USER_PATH+'/maya/'+version_
    if not os.path.exists(mayaPath):
        print "- failed"
        print "ERROR >> This version of Maya was not found."
        return
    
    rndrPrefFile = USER_PATH+'/maya/'+version_+'/prefs/shelves/shelf_Rendering.mel'
    if not os.path.exists(rndrPrefFile):
        print "- failed"
        print "ERROR >> The rendering shelf was not found."
        return
    
    imgFile = SERVER_PATH+"logo.png"
    
    newStr = '    shelfButton\n\
        -enableCommandRepeat 1\n\
        -enable 1\n\
        -width 38\n\
        -height 27\n\
        -manage 1\n\
        -visible 1\n\
        -preventOverride 0\n\
        -annotation "The NCCA render farm module"\n\
        -enableBackground 0\n\
        -align "center"\n\
        -label "'+TOOL_NAME+'"\n\
        -labelOffset 0\n\
        -rotation 0\n\
        -flipX 0\n\
        -flipY 0\n\
        -useAlpha 1\n\
        -font "plainLabelFont"\n\
        -overlayLabelColor 0.8 0.8 0.8\n\
        -overlayLabelBackColor 0 0 0 0.25\n\
        -image "'+imgFile+'"\n\
        -image1 "'+imgFile+'"\n\
        -style "iconOnly"\n\
        -marginWidth 1\n\
        -marginHeight 1\n\
        -command "'+readData(SERVER_PATH+'sceneData_maya.py',True)+'"\n\
        -sourceType "python"\n\
        -commandRepeatable 1\n\
        -flat 1\n\
    ;\n'
    
    if TOOL_NAME not in open(rndrPrefFile).read():
        num_lines = sum(1 for line in open(rndrPrefFile))
        try:
            with open(rndrPrefFile, 'r') as pfile:
                data = pfile.readlines()
        except:
			print "- failed"
			print "ERROR >> The rendering shelf is not accessible."
			print "         Please make sure that <",rndrPrefFile,"> exists and try again."
			return

        if data[num_lines-1].startswith("}"):
            prevLine = data[num_lines-2]
            data[num_lines-2] = prevLine + newStr

        try:
            with open(rndrPrefFile, 'w') as pfile:
                pfile.writelines( data )
            print "- ok"
        except:
			print "- failed"
			print "ERROR >> The rendering shelf is not accessible."
			print "         Please make sure that <",rndrPrefFile,"> exists and try again."
			return
    else:
        print "- already installed"


def houdiniInstall():
    houPath = USER_PATH+'/houdini'+HOUDINI_VERSION
    if not os.path.exists(houPath):
		print "- failed"
		print "ERROR >> The Houdini version <"+HOUDINI_VERSION+"> was not found."
		return
    
    rndrPrefFile = USER_PATH+'/houdini'+HOUDINI_VERSION+'/toolbar/default.shelf'
    if not os.path.exists(rndrPrefFile):
        default = '<?xml version="1.0" encoding="UTF-8"?>\n<shelfDocument>\n\n\n<shelfSetEdit name="custom_shelf_set" fileLocation="/opt/hfs'+HOUDINI_VERSION+'.'+HOUDINI_SUBVERSION+'/houdini/toolbar/ShelfDefinitions.shelf"/>\n</shelfDocument>'
        try:
            with open(rndrPrefFile, 'w') as pfile:
                pfile.writelines( default )
        except:
			print "- failed"
			print "ERROR >> Could not create the default shelf."
			print "         Please make sure that <",rndrPrefFile,"> exists and try again."
			return 

    imgFile = SERVER_PATH+"logo.png"

    newStr = '\n    <toolshelf name="Rendering" label="Rendering">\n\
                        <memberTool name="The NCCA render farm module"/>\n\
                    </toolshelf>\n\
                    \n\
                    <tool name="The NCCA render farm module" label="'+TOOL_NAME+'" icon="'+imgFile+'">\n\
                        <script scriptType="python"><![CDATA[\n'+readData(SERVER_PATH+"sceneData_houdini.py",False)+']]></script>\n\
                    </tool>\n\
                    \n\
                    <shelfSetEdit name="shelf_set_1" fileLocation="/opt/hfs'+HOUDINI_VERSION+'.'+HOUDINI_SUBVERSION+'/houdini/toolbar/ShelfDefinitions.shelf">\n\
                        <addMemberToolshelf name="Rendering" inPosition="13"/>\n\
                    </shelfSetEdit>\n'
    
    if TOOL_NAME not in open(rndrPrefFile).read():
        num_lines = sum(1 for line in open(rndrPrefFile))
        try:
            with open(rndrPrefFile, 'r') as pfile:
                data = pfile.readlines()
        except:
			print "- failed"
			print "ERROR >> The rendering shelf is not accessible."
			print "         Please make sure that <",rndrPrefFile,"> exists and try again."
			return

        if data[num_lines-1].startswith("</shelfDocument>"):
            prevLine = data[num_lines-2]
            data[num_lines-2] = prevLine + newStr

        try:
            with open(rndrPrefFile, 'w') as pfile:
                pfile.writelines( data )
	        print "- ok"
        except:
			print "- failed"
			print "ERROR >> The rendering shelf is not accessible."
			print "         Please make sure that <",rndrPrefFile,"> exists and try again."
			return
    else:
        print "- already installed"


#==========================================================#


if not cc():
    exit()

userMode = oct(os.stat(USER_PATH)[stat.ST_MODE])[3:]
print ">> Checking user permissions:",userMode

if int(userMode[2]) < 4:
    print "ERROR >> The tool cannot access your home directory.."
    print "         Consider changing your permissions to 755."
    if using_linux_os():
        print "         chmod -R 755 /home/<your student login number>"
    else:
        print "         On Windows you have to contact IT to fix your permissions problem."
    print "--------------------------------------------------------"
    if raw_input("Press Enter to quit.") == '':
        exit()
print

if using_linux_os():
    if 'maya' in commands.getoutput('ps -A') or 'houdini-bin' in commands.getoutput('ps -A'):
        print "ERROR >> Please close down maya and/or houdini in order to install this tool."
        if raw_input("Press Enter to quit.") == '':
            exit()
else:
    processes = subprocess.Popen("tasklist", stdout=subprocess.PIPE, shell=True)
    processes = processes.communicate()
    processes = processes[0]

    if 'maya' in processes:
        print "ERROR >> Please close down maya in order to install this tool."
        if raw_input("Press Enter to quit.") == '':
            exit()


#==========================================================#


for VERSION in MAYA_VERSIONS:
    print ">> Installing the tool for Maya",VERSION,
    mayaInstall(VERSION)
print

if using_linux_os():
    print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print
    print ">> Installing the tool for Houdini",
    houdiniInstall()
    print


