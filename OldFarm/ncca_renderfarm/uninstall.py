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


import stat
from loader import *


print
print "-- Uninstalling the NCCA RenderFarm tool --"
print


#==========================================================#


def mayaUninstall(version_):
    mayaPath = USER_PATH+'/maya/'+version_
    if not os.path.exists(mayaPath):
        print "- failed"
        print "WARNING >> This version of Maya was not found."
        return
    
    rndrPrefFile = USER_PATH+'/maya/'+version_+'/prefs/shelves/shelf_Rendering.mel'
    if not os.path.exists(rndrPrefFile):
        print "- failed"
        print "WARNING >> The rendering shelf was not found."
        return
    
    imgFile = SERVER_PATH+"logo.png"

    if TOOL_NAME in open(rndrPrefFile).read():
        mainData = []
        try:
            with open(rndrPrefFile, 'r') as pfile:
                mainData = pfile.readlines()
        except:
            print "- failed"
            print "ERROR >> The rendering shelf is not accessible."
            print "         Please delete your preferences directory."
            return

        startArrayNum = endArrayNum = CONST_MAX
        for i in range(len(mainData)):
            if TOOL_NAME in mainData[i]:
                for j in range(i,0,-1):
                    if 'shelfButton' in mainData[j]:
                        startArrayNum = j
                        break
                for k in range(i,len(mainData)):
                    if ';\n' in mainData[k]:
                        endArrayNum = k+1
                        break
                break
        
        #print ">> (DEBUG) -------- Removing tool found between [",startArrayNum,":",endArrayNum,"]"
        del mainData[startArrayNum:endArrayNum]

        try:
            with open(rndrPrefFile, 'w') as pfile:
                pfile.writelines( mainData )
        except:
            print "- failed"
            print "ERROR >> The rendering shelf is not accessible."
            print "         Please delete your preferences directory."
            return
        
    print "- ok"
    
    print "   Removing renderfarm info text info from maya's directory",
    try:
        if using_linux_os():
            os.system("rm -f "+USER_PATH+"/maya/rnd_info.txt")
        else:
            dpath = USER_PATH+"/maya/rnd_info.txt"
            dpath = '\\'.join(dpath.split("/"))
            os.system("del /F "+dpath)
        print "- ok"
    except:
        print "- failed"
        print "WARNING >> Failed to remove renderfarm info from the maya directory."


def houdiniUninstall():
    houPath = USER_PATH+'/houdini'+HOUDINI_VERSION
    if not os.path.exists(houPath):
        print "- failed"
        print "WARNING >> The Houdini version <"+HOUDINI_VERSION+"> was not found."
        return

    rndrPrefFile = houPath+'/toolbar/default.shelf'
    if not os.path.exists(rndrPrefFile):
        print "- failed"
        print "WARNING >> The default shelf was not found."
        return
    
    imgFile = SERVER_PATH+"logo.png"

    if TOOL_NAME in open(rndrPrefFile).read():
        mainData = []
        try:
            with open(rndrPrefFile, 'r') as pfile:
                mainData = pfile.readlines()
        except:
            print "- failed"
            print "ERROR >> The rendering shelf is not accessible!"
            print "         Please delete your preferences directory."
            return
        
        toolShelf = CONST_MAX
        for i in range(len(mainData)):
            if 'toolshelf name="Rendering"' in mainData[i]:
                toolShelf = i-1
                #print ">> (DEBUG) -------- Removing tool shelf name between [",toolShelf,":",toolShelf+4,"]"
                del mainData[toolShelf:toolShelf+4]
                break

        startToolCommand = endToolCommand = CONST_MAX
        for i in range(len(mainData)):
            if TOOL_NAME in mainData[i]:
                startToolCommand = endToolCommand = i-1
            if i>endToolCommand and '</tool>' in mainData[i]:
                endToolCommand = i+1
                #print ">> (DEBUG) -------- Removing tool CDATA between [",startToolCommand,":",endToolCommand,"]"
                del mainData[startToolCommand:endToolCommand]
                break

        memberToolshelf = CONST_MAX
        for i in range(len(mainData)):
            if 'addMemberToolshelf name="Rendering"' in mainData[i]:
                memberToolshelf = i-2
                #print ">> (DEBUG) -------- Removing member tool shelf between [",memberToolshelf,":",memberToolshelf+4,"]"
                del mainData[memberToolshelf:memberToolshelf+4]
                break
        
        try:
            with open(rndrPrefFile, 'w') as pfile:
                pfile.writelines( mainData )
        except:
            print "- failed"
            print "ERROR >> The rendering shelf is not accessible."
            print "         Please delete your preferences directory."
            return
    
    print "- ok"
    
    print "   Removing renderfarm info text info from houdini's directory",
    try:
        os.system("rm -f "+USER_PATH+"/houdini"+HOUDINI_VERSION+"/rnd_info.txt")
    except:
        print "- failed"
        print "WARNING >> Failed to remove renderfarm info from the maya directory." 


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
        print "ERROR >> Please close down maya and/or houdini in order to uninstall this tool."
        if raw_input("Press Enter to quit.") == '':
            exit()
else:
    processes = subprocess.Popen("tasklist", stdout=subprocess.PIPE, shell=True)
    processes = processes.communicate()
    processes = processes[0]

    if 'maya' in processes:
        print "ERROR >> Please close down maya in order to uninstall this tool."
        if raw_input("Press Enter to quit.") == '':
            exit()


#==========================================================#


for VERSION in MAYA_VERSIONS:
	print ">> Uninstalling the tool for Maya",VERSION,
	mayaUninstall(VERSION)
print

if using_linux_os():
	print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
	print
	print ">> Uninstalling the tool for Houdini",
	houdiniUninstall()
	print


