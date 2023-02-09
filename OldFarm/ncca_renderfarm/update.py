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
print "-- Updating the NCCA RenderFarm tool --"
print


#==========================================================#


def readData(mainFile_, fixStr=True):
    file_data = None
    try:
        with open(mainFile_, 'r') as mf:
            file_data = mf.readlines()
    except:
        print "- failed"
        print "ERROR >> The main tool is not accessible."
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


def mayaUpdate(version_):
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
    
    if TOOL_NAME in open(rndrPrefFile).read():
        mainData = []
        try:
            with open(rndrPrefFile, 'r') as mf:
                mainData = mf.readlines()
        except:
            print "- failed"
            print "ERROR >> The rendering shelf is not accessible."
            print "         Please make sure that <",rndrPrefFile,"> exists and try again."
            return        

        arrayNum = CONST_MAX
        for i in range(len(mainData)):
            if TOOL_NAME in mainData[i]:
                arrayNum = i
            if i>arrayNum and '-command' in mainData[i]:
                arrayNum = i
                #print ">> (DEBUG) -------- legacy command found at [",arrayNum,"]"
                break

        mainData[arrayNum] = '        -command "'+readData(SERVER_PATH+"sceneData_maya.py")+'"\n'

        try:
            with open(rndrPrefFile, 'w') as pfile:
                pfile.writelines( mainData )
            print "- ok"
        except:
			print "- failed"
			print "ERROR >> The rendering shelf is not accessible."
			print "         Please make sure that <",rndrPrefFile,"> exists and try again."
			return


def houdiniUpdate():
    houPath = USER_PATH+'/houdini'+HOUDINI_VERSION
    if not os.path.exists(houPath):
        print "- failed"
        print "ERROR >> The Houdini version <"+HOUDINI_VERSION+"> was not found."
        return

    rndrPrefFile = houPath+'/toolbar/default.shelf'
    if not os.path.exists(rndrPrefFile):
        print "- failed"
        print "ERROR >> The rendering shelf was not found."
        return
    
    if TOOL_NAME in open(rndrPrefFile).read():
        mainData = []
        try:
            with open(rndrPrefFile, 'r') as mf:
                mainData = mf.readlines()
        except:
            print "- failed"
            print "ERROR >> The rendering shelf is not accessible."
            print "         Please make sure that <",rndrPrefFile,"> exists and try again."
            return

        startArrayNum = CONST_MAX
        endArrayNum = CONST_MAX
     
        for i in range(len(mainData)):
            if TOOL_NAME in mainData[i]:
                startArrayNum = endArrayNum = i
            if i>startArrayNum and '<![CDATA[' in mainData[i]:
                startArrayNum = i+1
            if i>endArrayNum and ']]></script>' in mainData[i]:
                endArrayNum = i
                break

        #print ">> (DEBUG) -------- legacy command found between [",startArrayNum,":",endArrayNum,"]"
        del mainData[startArrayNum:endArrayNum]
        
        mainData.insert(startArrayNum,readData(SERVER_PATH+"sceneData_houdini.py",False))
        mainData[startArrayNum] = mainData[startArrayNum][1:]
        
        try:
            with open(rndrPrefFile, 'w') as pfile:
                pfile.writelines( mainData )
            print "- ok"
        except:
            print "- failed"
            print "ERROR >> The rendering shelf is not accessible."
            print "         Please make sure that <",rndrPrefFile,"> exists and try again."
            return


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
        print "ERROR >> Please close down maya and/or houdini in order to update this tool."
        if raw_input("Press Enter to quit.") == '':
            exit()
else:
    processes = subprocess.Popen("tasklist", stdout=subprocess.PIPE, shell=True)
    processes = processes.communicate()
    processes = processes[0]

    if 'maya' in processes:
        print "ERROR >> Please close down maya in order to update this tool."
        if raw_input("Press Enter to quit.") == '':
            exit()


#==========================================================#


for VERSION in MAYA_VERSIONS:
    print ">> Updating the tool for Maya",VERSION,
    mayaUpdate(VERSION)
print

if using_linux_os():
    print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print
    print ">> Updating the module for Houdini",
    houdiniUpdate()
    print


