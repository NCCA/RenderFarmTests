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


def vcr(info_, uiproc_ = None):
	c = None
	if (info_.using_linux_os()):
		c = uiproc_(info_.os.stat(info_.SERVER_PATH).st_uid).pw_name
	else:
		f = info_.os.path.abspath(info_.SERVER_PATH).split("\\")[-1].split("_")[0]
		u = info_.os.stat(info_.SERVER_PATH).st_uid
		g = info_.os.stat(info_.SERVER_PATH).st_gid
		c  = int(str(len(f))+str(len(f)-1)+str(g)+str(u))
	cn = 0
	if isinstance(c,str):
		for i in c:
			cn += ord(i)+88
		cn += 2917
	else:
		cn = c
	if (cn!=info_._):
		info_.terminate("This is not the authentic ncca renderfarm tool.")
		return False
	return True


