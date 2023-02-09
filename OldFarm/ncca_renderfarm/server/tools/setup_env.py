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


import sys, platform, re

if platform.system() == 'Linux':
    rnd_path = '/public/bin/ncca_renderfarm/'
else:
    rnd_path = '//bournemouth.ac.uk/Data/Student/Public/Schools/FMC/NCCA/Renderfarm/ncca_renderfarm/'

if not rnd_path in sys.path:
    sys.path.insert(0, rnd_path)

from loader import *
cc()


#==========================================================#


if using_linux_os():
    sys.path.append('/usr/local/pfx/qube/api/python')
else:
    sys.path.append('C:/Program Files/pfx/qube/api/python')

try:
    import qb
except:
    print "ERROR >> The Qube API was not found."
    print "         Please contact our IT support."


os.environ["QB_SUPERVISOR"] = "172.16.77.245"
os.environ["QB_DOMAIN"] = "ncca"

try:
    from callback import wrangle,openProjectDirectoryOnServer
    from scenefile_data import getSceneData
    from access_server import checkParamiko
    from online_project import findProjectInstances,resolveProjectDuplication,uploadProject
    from assert_quota import checkQuota
    from fix_vrscene import fixVRScene
except Exception as ex:
    terminate(ex)

