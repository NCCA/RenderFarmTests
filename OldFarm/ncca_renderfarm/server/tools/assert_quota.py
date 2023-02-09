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


def checkQuota(userRemotePath_, sftp_):
    print ">> Disk Quota Check (Recommended)"
    if raw_input(">> Would you like to check your disk quota before rendering? (y/n): ") == 'y':
        from quota_check import calculateServerQuota    
        serverQuota = calculateServerQuota(userRemotePath_,sftp_)
        if (serverQuota[1] > 90.0):
            print "WARNING >> High Quota!!!"
            print "           Your disk quota on the tete server at <",userRemotePath_,"> is very high!!! This means"
            print "           that you will soon run out of disk space and you won't be able to see any output"
            print "           renders. Please backup and remove old projects from the server. If you proceed,"
            print "           there is a high chance of corrupting your files!"
            print "           It is NOT recommended to proceed until you sort this out."
    else:
        print ">> Skipped disk quota check."


