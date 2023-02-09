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


import sys, os, stat
from os.path import expanduser
from get_os import *

if using_linux_os():
    sys.path.append('/usr/lib64/python2.7/lib-dynload')

import subprocess, inspect

### GET ALL ENVIRONMENT VARS
#import pprint
#env_var = os.environ
#print("User's Environment variable:") 
#pprint.pprint(dict(env_var), width = 1) 


#==========================================================#


CONST_MAX = 99999999999999999999
TOOL_NAME = 'nccaRenderFarm'

# Could search for currently used versions of maya/houdini/prman instead of hardcoding, but f*** it!
MAYA_VERSIONS = ['2020','2019','2018']
MAYA_VERSION_ON_SERVER = MAYA_VERSIONS[0]
PRMAN_VERSIONS = ['24.1','22.5','21.5']
PRMAN_VERSION_ON_SERVER = PRMAN_VERSIONS[0]
_ = int(str(len("MAYA"))+str(len("HOU"))+"00")
HOUDINI_LICENSE_SERVER = "hamworthy.bournemouth.ac.uk"
MAYA_LICENSE_SERVER = "wrangle.bournemouth.ac.uk"
PIXAR_LICENSE_SERVER = "9010@talavera.bournemouth.ac.uk"

if using_linux_os():
    import commands
    SERVER_PATH = "/public/bin/ncca_renderfarm/"
    USER_PATH = expanduser("~")
    USER_NAME = USER_PATH.split("/")[-1]
    HOUDINI_VERSION = '18.5'
    HOUDINI_SUBVERSION = '596'
else:
    import ctypes
    SERVER_PATH = "//bournemouth.ac.uk/Data/Student/Public/Schools/FMC/NCCA/Renderfarm/ncca_renderfarm/"
    USER_NAME = os.getenv('username')
    if USER_NAME == None:
        USER_NAME = os.getenv('VIEWCLIENT_BROKER_USERNAME')
    USER_NAME = USER_NAME.lower()
    USER_DOMAIN = os.getenv('userdomain')
    if USER_DOMAIN == None:
        USER_DOMAIN = os.getenv('VIEWCLIENT_BROKER_DOMAINNAME')
    USER_DOMAIN = USER_DOMAIN.lower()
    USER_PATH = "//bournemouth.ac.uk/data/"+USER_DOMAIN+"/home/"+USER_NAME
    if USER_DOMAIN == "student":
        USER_PATH = "//bournemouth.ac.uk/data/"+USER_DOMAIN+"/home/FMC/"+USER_NAME

class colour:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAILED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def terminate(msg_=None):
    global SERVER_PATH
    
    who_is_calling = inspect.getframeinfo(sys._getframe(1)).filename
    on_server = False
    if SERVER_PATH+"server/" in who_is_calling:
        on_server = True

    if (msg_ != None):
        print "ERROR >>",msg_
    print
    print "--- Closing the ncca renderfarm tool ---"
    print "========================================================"

    if (on_server == True):
        if raw_input("Press Enter to exit.") == '':
            exit()
    try:
        exit()
    except:
        return
