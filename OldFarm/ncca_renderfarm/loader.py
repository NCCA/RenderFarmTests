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


import info
from info import *

if (using_linux_os()):
	from pwd import getpwuid

import imp
with open(info.SERVER_PATH+'.vcr.py', 'rb') as fp:
    icr = imp.load_module('.vcr', fp, '.vcr.py', ('.py', 'rb', imp.PY_SOURCE))

def cc():
	if (using_linux_os()):
		return icr.vcr(info,getpwuid)
	else:
		return icr.vcr(info)

