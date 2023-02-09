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


from loader import *
from stat import S_ISDIR


#==========================================================#


def bytes2gigabytes(sizeInBytes_):
    return "%4.2f" % (((float(sizeInBytes_)/1024.0)/1024.0)/1024.0)


def kilobytes2gigabytes(sizeInKiloBytes_):
    return "%4.2f" % ((float(sizeInKiloBytes_)/1024.0)/1024.0)


def humanReadableBytes(sizeInBytes_):
    for s in ['B','K','M','G']:
        if sizeInBytes_ < 1024.0:
            return "%4.2f%s" % (sizeInBytes_, s)
        sizeInBytes_ /= 1024.0
    return "%4.2f%s" % (sizeInBytes_, 'T')


def calculateLocalQuota(path_):
	percentage = 0

	if using_linux_os():
		if (USER_PATH in path_):
			diskLimit = subprocess.Popen("quota -u "+USER_NAME+" | tail -1 | awk '{print $3}'", shell=True, stdout=subprocess.PIPE)
			diskSpace = subprocess.Popen("quota -u "+USER_NAME+" | tail -1 | awk '{print $1}'", shell=True, stdout=subprocess.PIPE)
		else:
			diskLimit = subprocess.Popen("df "+path_+" | tail -1 | awk '{print $2}'", shell=True, stdout=subprocess.PIPE)
			diskSpace = subprocess.Popen("df "+path_+" | tail -1 | awk '{print $3}'", shell=True, stdout=subprocess.PIPE)

		diskLimit = int(diskLimit.communicate()[0])
		diskLimit = float(kilobytes2gigabytes(diskLimit))

		diskSpace = int(diskSpace.communicate()[0])
		diskSpace = float(kilobytes2gigabytes(diskSpace))
	else:
		#BUG: Cannot find quota from: OneDrive - Bournemouth University
		if "OneDrive" in path_:
			print "\nWARNING >> Disk Quota cannot be retrieved when using OneDrive!"
			return None
		else:
			capacity_bytes = ctypes.c_ulonglong(0)
			free_bytes = ctypes.c_ulonglong(0)
			
			if (USER_PATH in path_):
				ctypes.windll.kernel32.GetDiskFreeSpaceExA(USER_PATH, None, ctypes.pointer(capacity_bytes), ctypes.pointer(free_bytes))
			else:
				ctypes.windll.kernel32.GetDiskFreeSpaceExA(path_, None, ctypes.pointer(capacity_bytes), ctypes.pointer(free_bytes))

			diskLimit = float(bytes2gigabytes(capacity_bytes.value))
			diskSpace = float(bytes2gigabytes(capacity_bytes.value - free_bytes.value))
		
	percentage = (diskSpace/diskLimit)*100.0
	percentage = round(percentage,2)
	return percentage


def walk(sftp_, path_):
    files = []
    dirs = []

    for itr in sftp_.listdir_iter(path_):
        if S_ISDIR(itr.st_mode):
            dirs.append(itr.filename)
        else:
            files.append(itr.filename)

    if files:
        for f in files:
            yield path_+'/'+f

    for itr in dirs:
        path = path_+'/'+itr
        for j in walk(sftp_,path):
            yield j


def calculateServerQuota(path_, sftp_):
    print ">> Checking the server disk quota at tete for ",path_
    print "   Please wait... (This may take a while)"

    diskLimit = 10.0
    
    try:
        quota_file = sftp_.open(".render_quota")
        diskLimit = quota_file.readline().strip()
        quota_file.close()
        diskLimit = float(diskLimit)
    except:
        print "WARNING >> The remote Quota file was not found!"
        print "           The default disk limit on tete is 10.0 Gb per user."
    
    diskSpace = 0
    for itr in walk(sftp_, path_):
        sftp_.lstat(itr).st_size
        diskSpace += sftp_.lstat(itr).st_size
    diskSpace = float(bytes2gigabytes(diskSpace))
    percentage = (diskSpace/diskLimit)*100.0
    
    print "   Disk quota is at:",percentage,"%"
    return [diskSpace,percentage]


