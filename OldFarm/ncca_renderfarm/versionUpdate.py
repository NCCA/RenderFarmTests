#!/usr/bin/env python

import sys,os
from loader import *

print
print "-- Version Update of the NCCA RenderFarm tool --"
print

if not cc():
    exit()

if len(sys.argv) < 2:
    print "- Usage: versionUpdate <VERSION> <UPDATE DATE>"
    print "     ex. ./versionUpdate 1.0 13/07/1988"
    print 
    if raw_input("Press Enter to quit.") == '':
        exit()

vFiles = [  SERVER_PATH+"get_os.py",\
            SERVER_PATH+"info.py",\
            SERVER_PATH+"loader.py",\
            SERVER_PATH+"install.py",\
            SERVER_PATH+"uninstall.py",\
            SERVER_PATH+"update.py",\
            SERVER_PATH+"sceneData_maya.py",\
            SERVER_PATH+"sceneData_houdini.py",\
            SERVER_PATH+"quota_check.py",\
            SERVER_PATH+".vcr.py",\
            SERVER_PATH+"server/nrfm_HBatch_Mantra.py",\
            SERVER_PATH+"server/nrfm_HRender_Mantra.py",\
            SERVER_PATH+"server/nrfm_IFD_Mantra.py",\
            SERVER_PATH+"server/nrfm_VRay.py",\
            SERVER_PATH+"server/nrfm_Renderman.py",\
            SERVER_PATH+"server/nrfm_Arnold.py",\
            SERVER_PATH+"server/tools/callback.py",\
            SERVER_PATH+"server/tools/access_server.py",\
            SERVER_PATH+"server/tools/assert_quota.py",\
            SERVER_PATH+"server/tools/fix_vrscene.py",\
            SERVER_PATH+"server/tools/online_project.py",\
            SERVER_PATH+"server/tools/renameIFDs.py",\
            SERVER_PATH+"server/tools/scenefile_data.py",\
            SERVER_PATH+"server/tools/setup_env.py" ]

for rndFile in vFiles:
    file = open(rndFile,'r')
    dataFile = file.readlines()

    for l in range(len(dataFile)):
        if '# VERSION' in dataFile[l]:
            data = dataFile[l].split()     
            print "-- Updating Tool Version in ",rndFile," from <",data[2],"> to <",str(sys.argv[1]),">"
            dataFile[l] = dataFile[l].replace(data[2],str(sys.argv[1]))

        if '# UPDATED DATE' in dataFile[l]:
            data = dataFile[l].split()     
            print "-- Changing Tool Update Date in ",rndFile," from <",data[3],"> to <",str(sys.argv[2]),">"
            dataFile[l] = dataFile[l].replace(data[3],str(sys.argv[2]))

        if 'print "Updated Date:' in dataFile[l]:
            data = dataFile[l].split()    
            print "-- Ammending Tool Date in ",rndFile," from <",data[3],"> to <",str(sys.argv[2]),">"
            dataFile[l] = dataFile[l].replace(data[3],str(sys.argv[2]+'"'))

    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    file.close()

    with open(rndFile, 'w') as f:
        for i in dataFile:
            f.write(i)

print


