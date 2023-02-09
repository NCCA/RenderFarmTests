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


import os, re


#==========================================================#


def renameIFDsLocally(projectDir_,localName_,remoteName_):
    ifdFileList = []

    for root, dirs, files in os.walk(projectDir_):
        for name in files:
            if name.endswith(".ifd"):
                Root = root.strip("/")
                ifdFileList.append('/'+Root+'/'+name)

    if not ifdFileList:
        return

    for ifdFile in ifdFileList:
        data = []

        with open(ifdFile, 'r') as f:
            data = f.readlines()
            f.close()

        for i in range(len(data)):
            if localName_ in data[i]:
                varElement = data[i].split('/')
                for k in range(len(varElement)):
                    if localName_ in varElement[k]:
                        num = None
                        try:
                            num = re.findall(r'\d',varElement[k])[0]
                        except:
                            num = 9999

                        if (varElement[k] == localName_) or (varElement[k] == localName_+'_'+str(num)):
                            varElement[k] = remoteName_

                joinedElements = "/".join(varElement)
                data[i] = joinedElements

        with open(ifdFile, 'w') as f:
            f.writelines(data)
            f.close()

        del data
