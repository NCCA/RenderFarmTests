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
import os, sys, time


#==========================================================#


def wrangle(userName_, qb_):
    allJobs = qb_.jobinfo(filters={'user':userName_}, subjobs=True)

    jobMainFrameStatus = None

    if len(allJobs) > 0:
        latestId = int(max([i['id'] for i in allJobs]))

        print
        print ">> Wrangling the latest job in Qube!\n"

        numOfInstances = 0
        framesRunning = [None]
        while ( (jobMainFrameStatus != 'complete') and (jobMainFrameStatus != 'failed') and (jobMainFrameStatus != 'killed') and \
                (jobMainFrameStatus != 'blocked') and (jobMainFrameStatus != 'suspended') and (jobMainFrameStatus != 'unknown') and \
                (jobMainFrameStatus != 'badlogin') ):

            job = qb_.jobinfo(filters={'id':str(latestId)}, agenda=True, subjobs=True)[0]

            jobMainId = job['id']
            jobMainName = job['name']
            jobMainFrameStatus = job['status']
            jobMainInstanceStatus = job['subjobstatus']

            jobWorkers = []
            for k in job['agenda']:
                jobWorkers.append([k['id'],k['status']])
            jobInstances = []
            for k in job['subjobs']:
                jobInstances.append([k['id'],k['status']])

            numOfInstances = len(jobInstances)
            sys.stdout.write( "\r---- id( %d ) : name( %s )    \n" % (jobMainId,jobMainName) )
            if len(jobWorkers) > 40:
                framesRunning = [[w[0],w[1]] for w in jobWorkers if w[1]!="complete"]

                if len(framesRunning) < numOfInstances:
                    framesRunning.extend([[0,None]]*(numOfInstances-len(framesRunning)))
                for i in range(numOfInstances):
                    sys.stdout.write( "\r    |-worker< %02d > --> %s   |-instance< %02d > --> %s   \n" % (framesRunning[i][0],framesRunning[i][1],jobInstances[i][0],jobInstances[i][1]))
            else:
                for w,i in zip(jobWorkers,jobInstances):
                    sys.stdout.write( "\r   |-worker< %02d > --> %s   |-instance< %02d > --> %s   \n" % (w[0],w[1],i[0],i[1]))

            sys.stdout.write( "\r----- final frames( %s ) : final instances( %s )    \n" % (jobMainFrameStatus,jobMainInstanceStatus) )
            sys.stdout.write( "\033[%dA" % (numOfInstances+2) )
            sys.stdout.flush()

            del job,jobMainId,jobMainName,jobMainInstanceStatus,jobWorkers,jobInstances
            time.sleep(2)

        sys.stdout.write( "\033[%dB" % (numOfInstances+1) )
        sys.stdout.flush()

        del framesRunning,numOfInstances
        
        print
        print
        print ">> Rendering is",jobMainFrameStatus,"!"
    else:
        print
        print ">> No jobs found under this user <",userName_,"> !"

    return jobMainFrameStatus


def openProjectDirectoryOnServer(userName_, projectDirPath_):
    if (raw_input("---- Open project directory on the server? (y/n) ") == 'y'):
        try:
            os.system("nautilus \""+projectDirPath_+"\"")
        except:
            print "ERROR >> Project directory not found on server!"
            os.system("nautilus sftp://tete/home/"+userName_)


