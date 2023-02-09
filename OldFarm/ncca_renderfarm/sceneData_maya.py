
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


import sys, platform

if platform.system() == "Linux":
    rnd_path = "/public/bin/ncca_renderfarm/"
else:
    rnd_path = "//bournemouth.ac.uk/Data/Student/Public/Schools/FMC/NCCA/Renderfarm/ncca_renderfarm/"

if not rnd_path in sys.path:
    sys.path.insert(0, rnd_path)

from loader import *
import maya.cmds as mc


print
print "========================================================"
print "            ncca Renderfarm Tool for Maya               "
print
print "Creator: Constantinos Glynos"
print "Created Date: 13/07/2016"
print "Updated Date: 07/02/2022"
print "Organisation: Bournemouth University"
print


#==========================================================#


def findVersion(path_):
    versionFile = path_
    versionData = []
    version = 0.0

    try:
        with open(versionFile, "r") as vf:
            versionData = vf.readlines()
    except:
        print "WARNING >> The file <"+path_+"> did not open for reading!"
        print "           Please contact the Animation Demonstrators (w109)."
        return None

    for c in versionData:
        if "VERSION" in c:
            dataLine = c.split()
            for i in range(len(dataLine)):
                if dataLine[i] == "VERSION:":
                    version = dataLine[i+1]
                    break
            version = float(version[:3])
            break
    
    return version


def checkProjectDir(project_data_):
    fp_scene = project_data_["scn_path"] + project_data_["scn_name_ext"]
    
    if (project_data_["pro_path"] not in fp_scene):
        print "- failed"
        print "ERROR >> Project directory was not found."
        print "         Please go to File -> Set Project and select the project directory."
        return False
    else:
        adv_scn_path = project_data_["scn_path"].split("/")
        if project_data_["pro_name"] not in adv_scn_path:
            print "- failed"
            print "ERROR >> Project directory was not found."
            print "         Please go to File -> Set Project and select the project directory."
            return False
    if (".ma" in project_data_["scn_path"]) or (".mb" in project_data_["scn_path"]):
        print "- failed"
        print "ERROR >> Project directory needs to be a directory/folder, not a file."
        print "         Please go to File -> Set Project and select the project directory."
        return False
    if not os.path.exists(fp_scene):
        print "- failed"
        print "ERROR >> The path to the scene file does not exist!"
        print "         Make sure the correct project directory is set."
        print "         Please go to File -> Set Project and select the project directory."
        return False
    if " " in fp_scene:
        print "- warning"
        print "WARNING >> The path to the current scene has spaces!!!"
        print "           <",fp_scene,">"
        print "           Please consider removing all spaces from the path."      
        proceed = mc.confirmDialog(t="WARNING - Spaces in path", m = ">> The path to the current scene has spaces!\n        Proceed without renaming? (y/n)", b=["Yes","No"], db="No", cb="No", ds="No")
        if str(proceed) == "No":
            print "           Smart choice! Rename the files and try again."
            return False
        else:
            print "           It is very likely that the renders will fail due to spaces in the path."
            return True
            
    print "- ok"
    return True


def configurePaths(project_data_):
    print ">> Searching scene for textures and other files",
    files = []
    imgFiles = []
    for i in mc.ls(type="file"):
        files.append(i)
        imgFiles.append(mc.getAttr(i+".fileTextureName"))
        
    for i in mc.ls(ap=True):
        if "VRayLightIES" in i:
            try:
                fn = mc.getAttr(i+".iesfn")
                if fn not in imgFiles:
                    files.append(i)
                    imgFiles.append(fn)
            except:
                pass
    
    if (len(files) == 0) and (len(imgFiles) == 0):
        print "- ok"
        return

    print "- updating"
    from quota_check import calculateLocalQuota # used to check quota before copying data into the project directory.
    for i in range(len(imgFiles)):
        print "   Checking path <"+imgFiles[i]+">",
        
        if (imgFiles[i].find(project_data_["pro_path"]) == -1):
            img = imgFiles[i].split("/")
            try:
                img = img[img.index(project_data_["pro_src_imgs"].split("/")[-1])+1:]
                img = "/".join(img)
            except:
                img = img[-1]
            fixed_path = project_data_["pro_src_imgs"]+"/"+img
            
            if os.path.exists(imgFiles[i]):
                src_img_path = project_data_["pro_src_imgs"]
                src_img_path = src_img_path.replace(" ","\\ ")
                    
                if not using_linux_os():
                    src_img_path = "\\\\".join(project_data_["pro_src_imgs"].split("/"))

                if not os.path.exists(project_data_["pro_src_imgs"]):
                    os.system("mkdir "+src_img_path)
                
                localQuota = calculateLocalQuota(project_data_["pro_path"])
                if localQuota > 90.0:
                    print "- failed"
                    print "ERROR >> Cannot copy file(s) because the quota is very high."
                    print "         Please clear your quota,  and try again."
                    terminate()
                
                try:
                    if using_linux_os():
                        img = imgFiles[i].replace(" ","\\ ")
                        print "\n\t\tCopying <"+img+"> to <"+src_img_path+">"
                        os.system("cp "+img+" "+src_img_path)
                    else:
                        img = "\\\\".join(imgFiles[i].split("/"))
                        print "\n\t\tCopying <"+img+"> to <"+src_img_path+">"
                        os.system("copy \\\""+img+"\\\" "+src_img_path)
                except:
                    print "ERROR >> Cannot copy <",imgFiles[i],"> into <",project_data_["pro_src_imgs"],"> !"
                    print "         Please make sure that the file(s) exist and that copy permissions are available."
                    terminate()
            else:
                print "ERROR >> Unable to resolve texture path <",imgFiles[i],">"
                print "         Please modify the texture paths manually and try again."
                terminate()
            
            ext = fixed_path.split(".")[-1]
            if ext == "IES" or ext == "ies":
                mc.setAttr(files[i]+".iesfn",fixed_path,type="string")
            else:
                mc.setAttr(files[i]+".fileTextureName",fixed_path,type="string")
            print "- fixed"
            
        elif (not os.path.exists(imgFiles[i]) or (("//" in imgFiles[i]) and using_linux_os())):
            print "- failed"
            print "ERROR >> Missing Texture path <",imgFiles[i],">"
            print "         If not used, then please remove all unused shaders in the scene."
            terminate()
            
        else:
            print "- ok"
            
    try:
        mc.file(s=True)
    except Exception as ex:
        terminate(ex)


def quotaCheck(path_):
    from quota_check import calculateLocalQuota
    localQuota = calculateLocalQuota(path_)
    if (localQuota > 90.0):
        print "- warning"
        msg = "The disk quota at < "+path_+" > is very high!!!\n\n"
        msg += "This means that you will soon run out of disk space.\n"
        msg += "If you proceed, there is a high chance of corrupting your files.\n"
        msg += "It is NOT recommended to proceed until you fix this problem."
        print "\n***************************** WARNING *****************************"
        print msg
        print "*******************************************************************\n"
        warn_quota = mc.confirmDialog(title="WARNING - High Quota", message=msg+"\n\nContinue?", messageAlign="right", button=["Yes","No"], defaultButton="No", cancelButton="No", dismissString="No")
        if str(warn_quota) == "No":
            print "                             Smart choice!"
            return False
        else:
            print "   At your own risk!"
    else:
        print "- ok"
    print "   Disk quota in <",path_,"> is at:",localQuota,"%"
    return True


def getRenderData():
    print ">> Searching for renderers",
    getRenderer = mc.getAttr("defaultRenderGlobals.currentRenderer")
    startFrame = None
    endFrame = None
    animFrames = None
    framePadding = None
    if getRenderer == "vray":
        if mc.getAttr(getRenderer+"Settings.animType") == 0:
            startFrame = int(mc.currentTime(q=True))
            endFrame = startFrame
            framePadding = 0
        if mc.getAttr(getRenderer+"Settings.animType") == 1:
            startFrame = int(mc.getAttr("defaultRenderGlobals.startFrame"))
            endFrame = int(mc.getAttr("defaultRenderGlobals.endFrame"))
            framePadding = int(mc.getAttr(getRenderer+"Settings.fileNamePadding"))
        if mc.getAttr(getRenderer+"Settings.animType") == 2:
            animFrames = mc.getAttr(getRenderer+"Settings.animFrames")
            framePadding = int(mc.getAttr(getRenderer+"Settings.fileNamePadding"))
    else:
        startFrame = int(mc.getAttr("defaultRenderGlobals.startFrame"))
        endFrame = int(mc.getAttr("defaultRenderGlobals.endFrame"))
        framePadding = int(mc.getAttr("defaultRenderGlobals.extensionPadding"))
    
    if framePadding == None:
        framePadding = 0
    print "- ok"
    
    return [getRenderer,startFrame,endFrame,framePadding,animFrames]


def compileSceneData(project_data_, render_info_):
    print
    print "==========================================================="
    print "-- Appending scene information to Scene Data:"
    print "   > User path:",USER_PATH
    print "   > Project directory:",project_data_["pro_path"]
    print "   > Scene directory:",project_data_["scn_path"]
    print "   > Scene name:",project_data_["scn_name_ext"]
    print "   > Renderer used:",render_info_[0]
    print "   > Start frame:",render_info_[1]
    print "   > End frame:",render_info_[2]
    print "   > Frame padding:",render_info_[3]
    if (render_info_[4] != None):
        print "   > Animation Frames (vray):",render_info_[4]
    print "==========================================================="
    print
    
    # This order matches the order being read by the server file.
    sd = [ USER_PATH,                         \
           ","+project_data_["pro_path"],     \
           ","+project_data_["scn_path"],     \
           ","+project_data_["scn_name_ext"], \
           ","+project_data_["scn_name"],     \
           ","+str(render_info_[1]),          \
           ","+str(render_info_[2]),          \
           ","+str(render_info_[3]),          \
           ","+render_info_[0] ]
           
    if (render_info_[4] != None):
        sd.append(","+str(animFrames))
        
    return sd


def createRndInfoFile(sceneData_):
    rnd_info_path = USER_PATH+"/maya/rnd_info.txt"
    try:
        if using_linux_os():
            os.system("touch "+rnd_info_path)
        else:
            dpath = "\\\\".join(rnd_info_path.split("/"))
            os.system("type nul > "+dpath)
    except:
        print "- failed"
        print "ERROR >> Cannot create file at: ",USER_PATH+"/maya/"
        print "         Please make sure the ~/maya directory exists and try again."
        terminate()

    try:
        with open(rnd_info_path, "w") as srnd:
            srnd.writelines(sceneData_)
            srnd.close()
    except:
        print "- failed"
        print "ERROR >> Cannot write into: ",rnd_info_path
        print "         Please make sure the ~/maya directory exists and that you have write permissions."
        terminate()
    
    print "- ok"
    return rnd_info_path


def checking_vrscene(project_data_):
    createVRScene = True
    if os.path.exists(project_data_["pro_path"]+"/"+project_data_["scn_name"]+".vrscene"):
        vrsc = mc.confirmDialog(t="VRScene found!", m="A .vrscene file has been found with the same name.\n                              Overwrite?", b=["Yes","No"], db="Yes", cb="No", ds="No")
        if str(vrsc) == "No":
            createVRScene = False
    if createVRScene:
        mc.vrend()


def exec_renderfarm():
    if using_linux_os():
        print ">> Setting python path",
        python_home = "/usr/bin/python"
        python_path = "/usr/lib64/python2.7"
        if os.path.exists(python_path):
            os.environ["PYTHONHOME"] = python_home
            os.environ["PYTHONPATH"] = python_path
            print "- ok"
        else:
            print "- failed"
            print "ERROR >> Cannot find:"
            print "         PYTHONHOME at: ",python_home
            print "         PYTHONPATH at: ",python_path
            terminate()
    
    mc.clearCache(all=True)
    mc.refresh()
    
    print ">> Retreiving scene and user information",
    try:
        project_path = mc.workspace(q=True,fn=True)
        project_name = os.path.basename(project_path)
        project_src_imgs = project_path+"/sourceimages"
        scene_path = str(os.path.dirname(mc.file(q=True,sn=True,wcn=True)))
        scene_name_ext = mc.file(q=True, sn=True, shn=True)
        scene_name = os.path.splitext(scene_name_ext)[0]
        
        project_data = { "pro_path":project_path,         \
                         "pro_name":project_name,         \
                         "pro_src_imgs":project_src_imgs, \
                         "scn_path":scene_path,           \
                         "scn_name_ext":scene_name_ext,   \
                         "scn_name":scene_name }
        
        # The if-statement will assure that a / is always added at the end of pro and scene paths.
        if not project_data["pro_path"].endswith("/"):
            project_data["pro_path"] += "/"
        if not project_data["scn_path"].endswith("/"):
            project_data["scn_path"] += "/"
        print "- ok"
        #print
        #for k,v in project_data.items():
        #    print "(DEBUG) --------", k, " : ", v
        #print
    except:
        print "- failed"
        print "ERROR >> Cannot retrieve project data."
        terminate()
    
    print ">> Verifying project directory",
    if not checkProjectDir(project_data):
        return
    
    print ">> Verifying local disk quota:",
    qta = mc.confirmDialog(t="Disk Quota Check (Recommended)", m="Would you like to check your disk quota?", b=["Yes","Skip"], db="Yes", cb="Skip", ds="Yes")
    if str(qta) == "Yes":
        if quotaCheck(project_data["pro_path"]) == False:
            terminate()
    else:
        print "- skipped"
    
    configurePaths(project_data)
    
    render_info = getRenderData()
    sceneData = compileSceneData(project_data,render_info)
    
    print ">> Creating render info file",
    createRndInfoFile(sceneData)
    
    print ">> Connecting to the server",
    getRenderer = render_info[0]
    
    if getRenderer == "vray":
        checking_vrscene(project_data)
        rfmod = SERVER_PATH+"server/nrfm_VRay.py"
        print "- ok"
    elif getRenderer == "arnold":
        rfmod = SERVER_PATH+"server/nrfm_Arnold.py"
        print "- ok"
    elif getRenderer == "renderman":
        rfmod = SERVER_PATH+"server/nrfm_Renderman.py"
        print "- ok"
    else:
        print "- failed"
        print "ERROR >> Unrecognized renderer! Please check your render settings!"
        return
    
    print ">> Loading the NCCA Renderfarm terminal session"
    if using_linux_os():
        os.system("gnome-terminal --window -- python \""+rfmod+"\"")
    else:
        subprocess.call("start /wait cmd /c python "+rfmod, shell=True)
        #subprocess.call("start /wait cmd /K python "+rfmod, shell=True) #Debug
    

#==========================================================#


cc()
local_version = findVersion(USER_PATH+"/maya/"+str(mc.about(version=True))+"/prefs/shelves/shelf_Rendering.mel")
online_version = findVersion(SERVER_PATH+"sceneData_maya.py")

if local_version != None:
    print ">> Checking for tool updates",
    update = True
    if local_version < online_version:
        print "- update found"
        msg = ">> A NEW VERSION WAS FOUND (" + str(online_version) + ")!!!\n\n"
        msg += "   Updating the tool is highly recommended.\n" 
        msg += "   Please save your scene and close Maya in order to update the tool.\n" 
        if using_linux_os():
            msg += "   In your terminal, execute:\n"
            msg += "/public/bin/ncca_renderfarm/update.py"
        else:
            msg += "   Open a cmd prompt and execute:\n"
            msg += "\\\\\\\\bournemouth.ac.uk\\Data\\Student\\Public\\Schools\n"
            msg += "\\FMC\\NCCA\\Renderfarm\\\\ncca_renderfarm\\update.py"
        print msg
        upd = mc.confirmDialog(t="ncca Renderfarm Update", m=msg, b=["OK","Cancel"], db="OK", cb="Cancel", ds="OK")
        if str(upd) == "OK":
            update = False
        else:
            print "   Please proceed with caution..."
    elif local_version == online_version:
        print "- ok"
    else:
        print "- failed"
        print "   Please run the update again!"
        if using_linux_os():
            print "   In your terminal, execute:"
            print "/public/bin/ncca_renderfarm/update.py"
        else:
            print "   Open a cmd prompt and execute:"
            print "\\\\\\\\bournemouth.ac.uk\\Data\\Student\\Public\\Schools\\FMC\\NCCA\\Renderfarm\\\\ncca_renderfarm\\update.py"
        update = False
    print
    if update == True:
        exec_renderfarm()

terminate()
