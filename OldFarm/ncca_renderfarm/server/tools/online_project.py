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
import os, re, getpass
from loader import *
if not using_linux_os():
    import smtplib


#==========================================================#


def findProjectInstances(userRemotePath_, local_projectDirName_, sftp_, paramiko_):
    print ">> Connecting to tete server."
    print colour.BLUE+"HINT >> You will not see any *, or another special character, while typing"
    print "        your password in the terminal."+colour.END
    transport = paramiko_.Transport(("tete", 22))
    pwd = getpass.getpass()
    
    try:
        transport.connect(username = USER_NAME, password = pwd)
    except:
        print "ERROR >> Cannot access the tete server."
        print "         Either the password is wrong or the machine's IP is blocked!"
        print "         Please try again or contact IT services to unblock this machine's IP."
        terminate()
    
    sftp_ = paramiko_.SFTPClient.from_transport(transport)
    try:
        sftp_.chdir(userRemotePath_)
        print "   Found home dir:",sftp_.getcwd()
    except IOError:
        print "ERROR >> Cannot find home directory on the renderfarm server."
        print "         Please contact IT to create a home directory for you on the tete server."
        terminate()
    
    print "\n>> Searching for similar project directories",
    instances = 0
    duplicateDirs = sftp_.listdir()
    for i in range(len(duplicateDirs)):
        version_num = 0
        try:
            version_num = map(int, re.findall(r'\d+', duplicateDirs[i]))[-1]
        except:
            pass
        if (duplicateDirs[i] == local_projectDirName_) or (duplicateDirs[i] == (local_projectDirName_+"_"+str(version_num))):
            instances += 1
    print "-",instances,"instances found", #adding , because of a following raw_input which adds an extra line.
    return instances,sftp_,transport


def dir_rm(sftp_, dirName_):
    file_list = sftp_.listdir(dirName_)
    for i in file_list:
        fp = dirName_+'/'+i
        try:
            sftp_.remove(fp)
        except IOError:
            dir_rm(sftp_,fp)
    sftp_.rmdir(dirName_)


def resolveProjectDuplication(project_instances_, local_project_data_, sftp_):
    remote_project_data = local_project_data_.copy()
    
    if project_instances_>0:
        if raw_input("   Would you like to overwrite the existing folder? (y/n): ") == 'n':
            new_remote_pro_name = local_project_data_['pro_name']+"_"+str(project_instances_)
            print "   Your current project will be renamed from <",local_project_data_['pro_name'],"> to <",new_remote_pro_name,">"
            if raw_input("   Continue? (y/n): ") == 'y':
                remote_project_data['pro_name'] = new_remote_pro_name
                count_instances = sum( 1 for _ in re.finditer(r'\b%s\b' % re.escape(local_project_data_['pro_name']), local_project_data_['pro_path']) )
                if (count_instances > 1):
                    base = '/'.join(local_project_data_['pro_path'].split('/')[:-1])
                    remote_project_data['pro_path'] = base+'/'+remote_project_data['pro_name']
                    baseScene = '/'.join(remote_project_data['scn_path'].split('/')[:-2])
                    remote_project_data['scn_path'] = baseScene+'/'+remote_project_data['pro_name']+'/'
                else:
                    remote_project_data['pro_path'] = local_project_data_['pro_path'].replace(local_project_data_['pro_name'],remote_project_data['pro_name'])
                    remote_project_data['scn_path'] = local_project_data_['scn_path'].replace(local_project_data_['pro_name'],remote_project_data['pro_name'])
                
                os.rename(local_project_data_['pro_path'],remote_project_data['pro_path'])

                if using_linux_os():
                    from renameIFDs import renameIFDsLocally
                    if renameIFDsLocally(remote_project_data['pro_path'],local_project_data_['pro_name'],remote_project_data['pro_name']) == True:
                        print ">> Successfully renamed ifd files to the remote path."
                
            else:
                print "ERROR >> Cannot proceed due to collisions in remote directory names!"
                terminate()
        
        else:
            if raw_input("   Continue with overwrite? (y/n): ") == 'y':
                try:
                    dir_rm(sftp_,remote_project_data['pro_name'])
                except:
                    print "ERROR >> Could not remove old project directory from the server!"
                    print "         Please login to tete and delete the project directory."
                    terminate()
            else:
                print "ERROR >> Cannot proceed due to collisions in remote directory names!"
                terminate()
    
    return remote_project_data


def uploadProject(remoteProject_, localProject_, server_, sftp_):
    print ">> Uploading project tree as:",remoteProject_['pro_name']
    print colour.WARNING+"   DO NOT interrupt this process."+colour.END
    sftp_.mkdir(remoteProject_['pro_name'])
    print "   Please wait for your files to be uploaded..."
    print
    
    try:
        if using_linux_os():
            os.system("sftp "+server_+" <<< $'put -r \""+remoteProject_["pro_path"]+"\"'")
        else:
            os.system('echo put -r "'+remoteProject_["pro_path"]+'" | sftp "'+server_+'/'+remoteProject_['pro_name']+'\"')
    except:
        print "ERROR >> Failed to upload files on the server! Please make sure you have enough space available."
        terminate()
    
    if not remoteProject_['pro_name'] == localProject_['pro_name']:
        print "   Reverting local changes",
        try:
            os.rename(remoteProject_['pro_path'],localProject_['pro_path'])
            if using_linux_os():
                from renameIFDs import renameIFDsLocally
                renameIFDsLocally(localProject_['pro_path'],remoteProject_['pro_name'],localProject_['pro_name'])
            print "- ok"
        except:
            print "- failed"
            print "WARNING >> Something went wrong when reverting the local changes."
            print "           Submission on the renderfarm will continue, but please make sure you fix the local changes manually."
        
        print "\n--- Upload complete!"



