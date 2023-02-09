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
import os


#==========================================================#


def fixVRScene(projectPath_, local_projectDirPath_, remote_projectDirPath_, justNameOfScene_):
	print ">> Fixing .vrscene",
	vrsceneFilePath = remote_projectDirPath_+"/"+justNameOfScene_+".vrscene"
	if os.path.exists(vrsceneFilePath):
		vrSceneData = []
		with open(vrsceneFilePath, 'r') as vrsfile:
			vrSceneData = vrsfile.readlines()
			vrsfile.close()
		
		for i in range(len(vrSceneData)):
			if (local_projectDirPath_ in vrSceneData[i]):
				#print "(DEBUG) -------- replacing base path:",vrSceneData[i]," > ",projectPath_
				vrSceneData[i] = vrSceneData[i].replace(local_projectDirPath_,projectPath_)
				#print "(DEBUG) -------- vrSceneData[i]:",vrSceneData[i]
			if (remote_projectDirPath_ in vrSceneData[i]):
				#print "(DEBUG) -------- replacing base path:",vrSceneData[i]," > ",projectPath_
				vrSceneData[i] = vrSceneData[i].replace(remote_projectDirPath_,projectPath_)
				#print "(DEBUG) -------- vrSceneData[i]:",vrSceneData[i]

		with open(vrsceneFilePath, 'w') as vrsfile:
			vrsfile.writelines(vrSceneData)
			vrsfile.close()
		print "- ok"
		del vrSceneData
	else:
		print "- failed"
		print "ERROR >> The .vrscene was not found in the project directory!"
		terminate()

