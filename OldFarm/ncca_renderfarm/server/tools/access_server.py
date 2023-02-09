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
import os, sys
from loader import *


#==========================================================#


def checkParamiko(local_projectDirPath_):
	print ">> Importing paramiko",
	try:
		import paramiko
		print "- ok"
	except:
		print "- searching"
		#BUG: Handle no permissions to create a file in tmpParamikoPath: OneDrive - Bournemouth University
		if (not using_linux_os()) and ("OneDrive" in local_projectDirPath_):
			idx = local_projectDirPath_.index("OneDrive")
			local_projectDirPath_ = local_projectDirPath_[:idx-1]
		
		tmpParamikoPath = local_projectDirPath_+".tmp_pLoc.log"
		if using_linux_os():
			os.system("locate paramiko > \""+tmpParamikoPath+"\"")
		else:
			search_paramiko_file = "sftp.py"
			os.system("where /r C:\ "+search_paramiko_file+" > \""+tmpParamikoPath+"\"")
		
		paramikoLoc = []
		try:
			with open(tmpParamikoPath, "r") as pl:
				paramikoLoc = pl.readlines()
				pl.close()
		except Exception as ex:
			terminate(ex)
		
		paths = []
		if using_linux_os():
			os.system("rm -f \""+tmpParamikoPath+"\"")
			for i in paramikoLoc:
				if i.split("/")[-1] == "paramiko\n":
					paths.append(i[:-1])
		else:
			tmpParamikoPath = '\\'.join(tmpParamikoPath.split("/"))
			os.system("del /F \""+tmpParamikoPath+"\"")
			for i in paramikoLoc:
				i = '/'.join(i.split("\\"))
				if ("paramiko" in  i) and (i.startswith("C:/Program Files/")):
					paths.append(i[0:i.find("paramiko")])
		
		if len(paths) == 0:
			print "   Paramiko was not found."
			print "   Installing paramiko",
			try:
				os.system("pip install paramiko")
				try:
					import paramiko
					print "- ok"
				except:
					print "- failed"
					print "ERROR >> Unable to import Paramiko!"
					print "         Please contact our IT support or a Demonstrator to assist you with this problem."
					terminate()
			except:
				print "ERROR >> Paramiko failed to install."
				print "         Please contact our IT support or a Demonstrator to assist you with this problem."
				terminate()
		else:
			print "   Paramiko was found."
			print "   Re-importing paramiko",
			for p in paths:
				if using_linux_os():
					p = p.split("/")[:-1]
					p = '/'.join(p)
				#print "(DEBUG) ------ <"+p+">"
				sys.path.append(p)
			try:
				import paramiko
				print "- ok"
			except:
				print "- failed"
				print "ERROR >> Unable to import Paramiko!"
				print "         Please contact our IT support or a Demonstrator to assist you with this problem."
				terminate()
		
	return paramiko

