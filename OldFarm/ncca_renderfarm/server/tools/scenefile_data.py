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


from get_os import *
import os, stat
from loader import *


#==========================================================#


def getSceneData(sceneInfoFile_):
    userMode = oct(os.stat(USER_PATH)[stat.ST_MODE])[3:]
    print ">> Checking user permissions:",userMode
    if int(userMode[2]) < 4:
        print "ERROR >> The tool cannot access your maya directory.."
        print "         Consider changing your permissions to 755 or simply allow others to Read"
        terminate()
    data = []
    with open(sceneInfoFile_, 'r') as sfile:
        data = sfile.readlines()
        sfile.close()
    
    data = data[0].split(",")
    
    if using_linux_os():
        try:
            os.system("rm -f "+sceneInfoFile_)
        except:
            print "WARNING >> rnd_info.txt was not deleted."
    else:
        sceneInfoFile_ = '\\'.join(sceneInfoFile_.split("/"))
        os.system("del /F "+sceneInfoFile_)
    
	#BUG: Find a better way to handle spaces in: OneDrive - Bournemouth University
	if (not using_linux_os()) and any("OneDrive" in d for d in data):
		if len(data) > 9: 
			data[1 : 5] = [' '.join(data[1 : 5])]
			data[2 : 6] = [' '.join(data[2 : 6])]
	
    return data



