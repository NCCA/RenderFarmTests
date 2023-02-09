
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


import sys

rnd_path = "/public/bin/ncca_renderfarm/"

if not rnd_path in sys.path:
    sys.path.insert(0, rnd_path)

from loader import *
from itertools import groupby
import re


print
print "=============================================================="
print "              ncca Renderfarm Tool for Houdini                "
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
    if (".hip" in project_data_["scn_path"]) or (".hipnc" in project_data_["scn_path"]):
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
        proceed = str(hou.ui.readInput(">> The path to the current scene has spaces!\n        Proceed without renaming? (y/n)")[1])
        if proceed == "n":
            print "           Smart choice! Rename the files and try again."
            return False
        else:
            print "           It is very likely that the renders will fail due to spaces in the path."
            return True
            
    print "- ok"
    return True


def findRenderer():
    list_renderers = [ i.name() for i in hou.node("/out").children() ]
    for i in range(len(list_renderers)):
        opType = None
        try:
            opType = str(hou.node("/out/"+list_renderers[i]).type())
        except:
            opType = ""
            
    len_list_renderers = len(list_renderers)
    if len_list_renderers == 0:
        print "- failed"
        print "ERROR >> No render node was found!"
        print "         Please create a render node and try again."
        terminate()
    elif len_list_renderers == 1:
        print "- ok"
        return list_renderers[0]
    else:
        print "- updating"
        msg = ">> Please select the prefered renderer:\n"
        for i in range(len_list_renderers):
            msg += "---- ("+str(i)+") : "+list_renderers[i]+"\n"
        print msg
        
        choice = int(hou.ui.readInput(msg+"\nSelect an option (0-"+str(len_list_renderers-1)+")")[1])
        if 0 <= choice <= (len_list_renderers-1):
            return list_renderers[choice]
        else:
            print "ERROR >> Unrecognized render node."
            terminate()


def calculate_relative_HIP(project_data_):
    relative_HIP = "$HIP/"
    if project_data_["pro_path"] != project_data_["scn_path"]:
        rsp = project_data_["scn_path"].split(project_data_["pro_path"])[-1]
        rsp = rsp.split("/")[:-1]
        relative_HIP += "../" * len(rsp)
    return relative_HIP


# The limitation is that files with heavy_ext cannot be copied. These files HAVE to be in the project directory. Whereas
# textures with the ext can be copied relatively safely. This function needs to perform a quota check after each copy.
def configurePaths(nodeSearch_, project_data_):
    print ">> Searching node <",nodeSearch_,">",
    list_nodes = map(hou.Node.path, hou.node("/"+nodeSearch_).children())
    if len(list_nodes) == 0:
        print "- ok"
        return
        
    external_files = hou.hscript("opextern -gR %s" % (" ".join(list_nodes)))[0]
    external_files = external_files.split("\n")[:-1]
    if external_files[0] == "No external references found":
        print "- ok"
        return
    
    print "- updating"
    from quota_check import calculateLocalQuota # used to check quota before copying data into the project directory.
    heavy_ext = (".bgeo",".sc",".sim",".obj")
    ext = (".jpeg",".jpg",".tif",".tiff",".png",".exr",".bmp",".rgb",".gif",".pbm",".pgm",".ppm",".rast",".xbm",".picnc",".rat") + heavy_ext
    reject_paths = ("$HOME",USER_PATH,"/transfer")
    relative_HIP = calculate_relative_HIP(project_data_)
    
    for f in external_files:
        pair = f.split("\t")
        pair[0] = pair[0][:-1]
        nodeParam = pair[0]
        
        for parm in hou.node(nodeParam).parms():
            paramName = parm.name()
            try:
                paramPath = parm.unexpandedString()
                paramPathExpanded = parm.evalAsString()
            except:
                paramPath = paramPathExpanded = ""
                
            if (paramPath.startswith(reject_paths) or paramPath.endswith(ext)) and len(paramPath.split("/")) > 1:
                print "   Checking path in <"+nodeParam+"/"+paramName+">",
                #print
                #print "(DEBUG) -------- paramPath         = ",paramPath
                #print "(DEBUG) -------- paramPathExpanded = ",paramPathExpanded
                #print "(DEBUG) -------- nodeParam type    = ",hou.nodeType(nodeParam).name()
                
                # $JOB needs to be converted into a path that is relative to $HIP because the renderfarm 
                # cannot evaluate $JOB properly and points to the local path insteas of tete. This can be
                # removed when IT fix $JOB on the renderfarm.
                if paramPath.startswith("$JOB"):
                    if (hou.nodeType(nodeParam).name() == "filecache") or (hou.nodeType(nodeParam).name() == "output") or \
                       (hou.nodeType(nodeParam).name() == "ifd"):
                        fixed_path = paramPath.split("$JOB/")[-1]
                    else:
                        fixed_path = paramPathExpanded.split(project_data_["pro_path"])[-1]
                    fixed_path = relative_HIP + fixed_path
                    hou.parm(nodeParam+"/"+paramName).set(fixed_path)
                    paramPath = parm.unexpandedString()
                    paramPathExpanded = parm.evalAsString()
                    print "- ok"
                
                if paramPath.startswith("$HIP"):
                    if not os.path.exists(paramPathExpanded):
                        if (hou.nodeType(nodeParam).name() == "filecache") or (hou.nodeType(nodeParam).name() == "output") or \
                           (hou.nodeType(nodeParam).name() == "ifd"):
                            print "- ok"
                        else:
                            fixed_path = paramPathExpanded.split(project_data_["scn_path"])[-1]
                            fixed_path_expanded = project_data_["pro_path"]+fixed_path
                            
                            if not os.path.exists(fixed_path_expanded):
                                print "- failed"
                                print "ERROR >> The file was not found in either of the following paths:"
                                print "         <",paramPathExpanded,">"
                                print "         <",fixed_path_expanded,">"
                                terminate()
                                
                            fixed_path = relative_HIP+fixed_path
                            hou.parm(nodeParam+"/"+paramName).set(fixed_path)
                            print "- ok"
                    else:
                        print "- ok"
                else:
                    if not os.path.exists(paramPathExpanded):
                        if (hou.nodeType(nodeParam).name() == "filecache") or (hou.nodeType(nodeParam).name() == "output") or \
                           (hou.nodeType(nodeParam).name() == "ifd"):
                            if paramPathExpanded.startswith(project_data_["pro_path"]):
                                fixed_path = paramPathExpanded.split(project_data_["pro_path"])[-1]
                                fixed_path = relative_HIP+fixed_path
                                hou.parm(nodeParam+"/"+paramName).set(fixed_path)
                                print "- ok"
                            else:
                                print "- failed"
                                print "ERROR >> An output path should be set in the project directory."
                                print "         Please use $HIP in the output path."
                                terminate()
                        else:
                            print "- failed"
                            print "ERROR >> The file at <",paramPathExpanded,"> was not found!"
                            terminate()
                    else:
                        fixed_path = ""
                        if paramPathExpanded.startswith(project_data_["scn_path"]):
                            fixed_path = paramPathExpanded.split(project_data_["scn_path"])[-1]
                            fixed_path = "$HIP/"+fixed_path
                            hou.parm(nodeParam+"/"+paramName).set(fixed_path)
                            print "- ok"
                        elif paramPathExpanded.startswith(project_data_["pro_path"]):
                            fixed_path = paramPathExpanded.split(project_data_["pro_path"])[-1]
                            fixed_path = relative_HIP+fixed_path
                            hou.parm(nodeParam+"/"+paramName).set(fixed_path)
                            print "- ok"
                        else:
                            if paramPathExpanded.endswith(heavy_ext):
                                if paramPathExpanded.startswith("/opt/"):
                                    print "- ok"
                                else:
                                    print "- failed"
                                    print "ERROR >> Copying 'bgeo','sc','sim' and 'obj' sequences may bloat your quota."
                                    print "         Please make sure that these files are inside your project directory before submitting your job to the renderfarm."
                                    terminate()
                            else:
                                localQuota = calculateLocalQuota(project_data_["pro_path"])
                                if localQuota > 90.0:
                                    print "- failed"
                                    print "ERROR >> Cannot copy file(s) because the quota is very high."
                                    print "         Please clear your quota,  and try again."
                                    terminate()
                                    
                                rnd_aux = project_data_["pro_path"]+"rnd_aux"
                                src_path = paramPathExpanded.replace(" ","\\ ")
                                dst_path = rnd_aux.replace(" ","\\ ")
                                if not os.path.exists(rnd_aux):
                                    os.system("mkdir "+dst_path)
                                print "\n\t\tCopying <"+src_path+"> to <"+dst_path+">"
                                try:
                                    os.system("cp "+src_path+" "+dst_path)
                                except:
                                    print "ERROR >> Cannot copy file."
                                    terminate()
                                    
                                fixed_path = paramPathExpanded.split("/")[-1]
                                fixed_path = relative_HIP+"rnd_aux/"+fixed_path
                                hou.parm(nodeParam+"/"+paramName).set(fixed_path)
                                print "      - ok"
    try:
        hou.hipFile.save()
    except Exception as ex:
        terminate(ex)

                
def setFramePadding(renderName_):
    padding = renderName_.find("$F")
    padding = renderName_[padding:]
    padding = padding.replace("$F","")
    if padding == "":
        padding = 0
    else:
        numbers_pad = ""
        for i in padding:
            if i.isdigit() == True:
                numbers_pad += i
            else:
                numbers_pad = "0"
                break
        padding = int(numbers_pad)
    return padding


def analyzeFramePadding(rendererNode_):
    framePadding = None
    pathToVMpictures = hou.parm("/out/"+rendererNode_+"/vm_picture")
    if pathToVMpictures == None:
        return

    renderFrameName = pathToVMpictures.unexpandedString().split("/")[-1]        
    if "$F" in renderFrameName:
        renderFrameName = renderFrameName.split(".")
        if len(renderFrameName) > 2:
            renderFrameName = renderFrameName[:-1]
            for i in renderFrameName:
                if "$F" in i:
                    framePadding = setFramePadding(i)
                    break
        else:
            renderFrameName = renderFrameName[0]
            framePadding = setFramePadding(renderFrameName)
            
    return framePadding


def checkRenderOutPaths(rendererNode_, projectDirName_):
    pathToOutputRenders = hou.parm("/out/"+rendererNode_+"/vm_picture")
    if pathToOutputRenders == None:
        print "- ok"
        return

    outputRenders = pathToOutputRenders.unexpandedString()
    pathToRenders = outputRenders.split("/")
    pathToRenders = pathToRenders[:-1]
    for i in range(len(pathToRenders)):
        if "$HIP" in pathToRenders[i]:
            pathToRenders[i] = str(hou.getenv("HIP"))
            
    pathToRenders = "/".join(pathToRenders)
    
    if not os.path.exists(pathToRenders):
        fixed_path = pathToRenders.replace(" ","\\ ")
        try:
            os.system("mkdir "+fixed_path)
            print "- ok"
        except Exception as ex:
            print "- failed"
            terminate(ex)
    else:
        print "- ok"

            
def analyzeIFDs(projectDir_):
    ifdsFilePath = False
    ifdFileList = []
    numF=0
    for root, dirs, files in os.walk(projectDir_):
        ifdFileList.append([root,[]])
        for name in files:
            if name.endswith(".ifd"):
                name = name.rsplit(".",1)[:-1]
                name = "".join(name)
                ifdFileList[numF][1].append(name) 
                ifdsFilePath = True
        numF+=1
    del numF
    
    if ifdsFilePath == False:
        print ">> No IFD files found!"
        return None
    else:
        print ">> IFD files found!"
        print "   Analyzing files and sequences..."
        
        ifdFiles = []
        for f in ifdFileList:
            lngth = len(f[1])
            if lngth != 0: # for each ifd file in the folder
                #print "(DEBUG) -------- ifd files in <",f[0],">"
                #print "(DEBUG) --------",f[1]
                
                try:
                    numsInFileNames = []
                    numsFoundInName = 0
                    for i in range(lngth):
                        foundInName=[]
                        f[1][i] = f[1][i].replace(".",". ").split(".")
                        
                        for spl in f[1][i]:
                            foundInName += re.findall("\d+", spl)
                        
                        numsFoundInName += len(foundInName)
                        f[1][i] = "".join(f[1][i]).replace(" ",".")
                        
                        if numsFoundInName > 0:
                            for n in range(len(foundInName)):
                                numsInFileNames.append(foundInName[n])
                    
                    if numsFoundInName == 0:
                        for i in range(lngth):
                            ifdFiles.append([f[0],f[1][i],""])
                    
                    elif numsFoundInName > 0:
                        numPartOfName = []
                        numPartOfPadding = []
                        
                        numSet = sorted(set(numsInFileNames))
                        for k in numSet:
                            if numsInFileNames.count(k) == 1:
                                numPartOfPadding.append(k)
                            if numsInFileNames.count(k) > 1:
                                numPartOfName.append(k)
                            
                        #print "(DEBUG) -------- numbers part of filenames: ",numPartOfName
                        #print "(DEBUG) -------- numbers part of padding: ",numPartOfPadding
                        
                        tmpName = f[1][0]
                        
                        for i in numPartOfPadding:
                            if i in tmpName:
                                tmpName = re.sub(i,"%@", tmpName)
                        
                        tmpName = tmpName.split("%")
                        
                        numPartOfPaddingAsInts = map(int,numPartOfPadding)
                        numPartOfPaddingAsInts = sorted(numPartOfPaddingAsInts)
                        
                        ifdFileRange = ""
                        for i in range(len(tmpName)):
                            if tmpName[i] == "@":
                                ifdFileRange = "<"+str(numPartOfPaddingAsInts[0])+"-"+str(numPartOfPaddingAsInts[-1])+">"
    
                        tmpName = "".join(tmpName)
                        ifdFiles.append([f[0],tmpName,ifdFileRange,str(len(numPartOfPadding[0]))])
                                                                           
                    else:
                        print "ERROR >> Cannot resolve ifd file name!"
                        return None
                except:
                    print "ERROR >> Cannot resolve ifd file name!"
                    return None
        
        msg = ">> Please select the ifd file(s) for rendering:\n"
        lngth = len(ifdFiles)
        for i in range(lngth):
            msg += "---- ("+str(i)+") : "+ifdFiles[i][1][:-1]+ifdFiles[i][2]+" @ <"+ifdFiles[i][0]+">\n"
        msg += "---- ("+str(lngth)+") : Ignore existing ifds and regenerate.\n"
        print msg
        
        choice = int(hou.ui.readInput(msg+"\nSelect an option (0-"+str(lngth)+")")[1])
        if choice < 0 or choice > lngth:
            print ">> Unrecognized option!"
            return None

        ifdInfo = "@IGNORE"

        if choice == lngth:
            print ">> Ignoring the existing ifd files and regenerating them online."
        else:
            print ">> Sending ",ifdFiles[choice][1][:-1]+ifdFiles[choice][2]," for rendering!"
            ifdInfo = [ifdFiles[choice][0]+"/"+ifdFiles[choice][1],ifdFiles[choice][3]]

        return ifdInfo

      
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
        warn_quota = hou.ui.displayMessage(msg+"\n\nContinue?",title="WARNING - High Quota", buttons=("Yes", "No"),default_choice=1)
        if warn_quota == 1:
            print "- failed"
            print "                             Smart choice!"
            return False
        else:
            print "- ok ...at your own risk!"
    else:
        print "- ok"
    print "   Disk quota in <",path_,"> is at:",localQuota,"%"
    return True


def getRenderData(projectDirName_):
    print ">> Searching for renderers",
    renderer = mantraNode = wedgeNode = findRenderer()
    if renderer == None:
        return
        
    nodeIsWedge = False if hou.parm("/out/"+wedgeNode+"/wedgemethod") == None else True
    if (nodeIsWedge):
        renderOption = hou.parm("/out/"+wedgeNode+"/driver").eval()
        mantraNode = renderOption.split("/")[-1]
    
    renderOption = hou.parm("/out/"+mantraNode+"/trange").eval()
    if renderOption == 0:
        startFrame = endFrame = int(hou.frame())
    else:
        frameRange = hou.parmTuple("/out/"+mantraNode+"/f").eval()
        startFrame = int(frameRange[0])
        endFrame = int(frameRange[1])        
    imgFramePadding = analyzeFramePadding(mantraNode)
    if imgFramePadding == None:
        imgFramePadding = ""
    
    print ">> Checking render output paths",    
    checkRenderOutPaths(mantraNode,projectDirName_)
    
    return [renderer,startFrame,endFrame,imgFramePadding]
  

def compileSceneData(project_data_, renderInfo_):
    print
    print "==========================================================="
    print "-- Appending scene information to Scene Data:"
    print "   > User path:",USER_PATH
    print "   > Project directory:",project_data_["pro_path"]
    print "   > Scene directory:",project_data_["scn_path"]
    print "   > Scene name:",project_data_["scn_name_ext"]
    print "   > Renderer used:",renderInfo_[0]
    print "   > Start frame:",renderInfo_[1]
    print "   > End frame:",renderInfo_[2]
    print "   > Frame padding:",renderInfo_[3]
    print "==========================================================="
    print
    
    # This order matches the order being read by the server file.
    return [USER_PATH,\
            ","+project_data_["pro_path"],\
            ","+project_data_["scn_path"],\
            ","+project_data_["scn_name_ext"],\
            ","+project_data_["scn_name"],\
            ","+str(renderInfo_[1]),\
            ","+str(renderInfo_[2]),\
            ","+str(renderInfo_[3]),\
            ","+renderInfo_[0]]

    
def createRndInfoFile():
    rnd_info_path = USER_PATH+"/houdini"+HOUDINI_VERSION+"/rnd_info.txt"
    try:
        os.system("touch "+rnd_info_path)
    except:
        print "- failed"
        print "ERROR >> Cannot create file at: ",USER_PATH+"/houdini"+HOUDINI_VERSION
        print "         Please make sure the ~/houdini"+HOUDINI_VERSION+" directory exists and try again."
        terminate()
    return rnd_info_path


def writeToFile(sceneData_, rnd_info_):
    try:
        with open(rnd_info_, "w") as srnd:
            srnd.writelines(sceneData_)
            srnd.close()
    except:
        print "- failed"
        print "ERROR >> Cannot write into: ",rnd_info_
        print "         Please make sure the ~/houdini"+HOUDINI_VERSION+" directory exists and that you have write permissions."
        terminate()


def usingIFDs(renderInfo_):
    ifdData = None
    try:
        usingIfds = bool(hou.parm("/out/"+renderInfo_[0]+"/soho_outputmode").eval())
    except:
        usingIfds = False
    
    if usingIfds == True:
        try:
            driver = hou.parm("/out/"+renderInfo_[0]+"/soho_diskfile").unexpandedString()
            padSplit = driver.split("$F")[-1]
            padNumber = map(int, re.findall(r"\d+", padSplit))
            if not padNumber:
                padNumber = 1
            else:
                padNumber = padNumber[0]
            ifdData = [","+str(usingIfds),","+str(padNumber)]
        except:
            ifdData = [","+str(usingIfds),",1"]
    else:
        ifdData = [","+str(usingIfds),","]
        
    return ifdData


def exec_renderfarm():
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
    
    print ">> Retreiving scene and user information",
    try:
        project_path = str(hou.getenv("JOB"))
        project_name = os.path.basename(project_path)
        scene_path = str(hou.getenv("HIP"))
        scene_name_ext = str(hou.hipFile.name()).split("/")[-1]
        scene_name = os.path.splitext(scene_name_ext)[0]
        project_data = { "pro_path":project_path,\
                         "pro_name":project_name,\
                         "scn_path":scene_path,\
                         "scn_name_ext":scene_name_ext,\
                         "scn_name":scene_name }
        # Some versions of Houdini include a / at the end of $HIP. Others don't.
        # The if-statement will assure that a / is always added at the end of $HIP.
        if not project_data["pro_path"].endswith("/"):
            project_data["pro_path"] += "/"
        if not project_data["scn_path"].endswith("/"):
            project_data["scn_path"] += "/"
        #print
        #for k,v in project_data.items():
        #    print "(DEBUG) --------", k, " : ", v
        #print
        print "- ok"
    except:
        print "- failed"
        print "ERROR >> Cannot retrieve project data."
        terminate()

    print ">> Verifying project directory",
    if not checkProjectDir(project_data):
        return
    
    print ">> Verifying local disk quota:",
    qta = hou.ui.displayMessage(">> Would you like to check your disk quota?",title="Disk Quota Check (Recommended)", buttons=("Yes", "Skip"), default_choice=1)
    if qta == 0:
        if quotaCheck(project_data["pro_path"]) == False:
            terminate()
    else:
        print "- skipped"
    
    configurePaths("ch",project_data)
    configurePaths("img",project_data)
    configurePaths("mat",project_data)
    configurePaths("obj",project_data)
    configurePaths("out",project_data)
    configurePaths("shop",project_data)
    configurePaths("stage",project_data)
    configurePaths("tasks",project_data)
    configurePaths("vex",project_data)
    
    msg = ">> Please select the prefered method of rendering:\n"
    msg += "---- (0) : HBatch\n"
    msg += "---- (1) : HRender\n"
    msg += "---- (2) : Generate and Render Mantra IFDs\n"
    print msg
    
    getRenderer = int(hou.ui.readInput(msg+"\nSelect an option (0-2)")[1])
    if getRenderer < 0 or getRenderer > 2:
        print "ERROR >> Unrecognized renderer."
        terminate()
    
    renderInfo = getRenderData(project_data["pro_name"])
    sceneData = compileSceneData(project_data,renderInfo)
    
    print ">> Connecting to the server",
    if getRenderer == 0:
        #print "(DEBUG) -------- nrfm_HBatch_Mantra"
        sceneData.extend(usingIFDs(renderInfo))
        rnd_info = createRndInfoFile()
        writeToFile(sceneData, rnd_info)
        rfmod = SERVER_PATH+"server/nrfm_HBatch_Mantra.py"
        print "- ok"
        
    elif getRenderer == 1:
        #print "(DEBUG) -------- nrfm_HRender_Mantra"
        sceneData.extend(usingIFDs(renderInfo))
        rnd_info = createRndInfoFile()
        writeToFile(sceneData, rnd_info)
        rfmod = SERVER_PATH+"server/nrfm_HRender_Mantra.py"
        print "- ok"
        
    elif getRenderer == 2:
        #print "(DEBUG) -------- nrfm_IFD_Mantra"
        print "- updating"
        print "   Checking for existing IFD files",
        ifdData = analyzeIFDs(project_data["pro_path"]) #returns [ifd_path,ifd_padding] or @IGNORE or None
        
        if ifdData == None or ifdData == "@IGNORE":
            print "- not found"
            driver = hou.parm("/out/"+renderInfo[0]+"/soho_diskfile").unexpandedString()
            padSplit = driver.split("$F")[-1]
            padNumber = map(int, re.findall(r"\d+", padSplit))
            if not padNumber:
                padNumber = 1
            else:
                padNumber = padNumber[0]
            ifdData = [","+str(False)+",",driver+",",str(padNumber)]
        else:
            print ">> found"
            ifdData = [","+str(True)+",",ifdData[0]+",",ifdData[1]]

        print "   Amending scene data",
        sceneData.extend(ifdData)
        rnd_info = createRndInfoFile()
        writeToFile(sceneData, rnd_info)
        rfmod = SERVER_PATH+"server/nrfm_IFD_Mantra.py"
        print "- ok"

    else:
        print "- failed"
        print "ERROR >> Unrecognized renderer! Please check your render settings!"
        return

    print ">> Loading the NCCA Renderfarm terminal session"
    print "---------------------------------------------------------------"
    os.system("gnome-terminal --window -- python '"+rfmod+"'")
    

#==========================================================#


cc()
localVersion = findVersion(USER_PATH+"/houdini"+HOUDINI_VERSION+"/toolbar/default.shelf")
onlineVersion = findVersion(SERVER_PATH+"sceneData_houdini.py")

if localVersion != None:
    print ">> Checking for tool updates",
    update = True
    if localVersion < onlineVersion:
        print "- update found"
        msg = ">> A NEW VERSION WAS FOUND (" + str(onlineVersion) + ")!!!\n\n"
        msg += "   Updating the tool is highly recommended.\n" 
        msg += "   Please save your scene and close Maya.\n"
        msg += "   In your terminal, execute:\n"
        msg += "/public/bin/ncca_renderfarm/update.py"
        print msg
        upd = hou.ui.displayMessage(msg, title="ncca Renderfarm Update", buttons=("OK", "Cancel"), default_choice=0)
        if upd == 0:
            update = False
        else:
            print "   Please proceed with caution..."
    elif localVersion == onlineVersion:
        print "- ok"
    else:
        print "- failed"
        print "   Please run the update again!"
        print "   In your terminal, execute:"
        print "/public/bin/ncca_renderfarm/update.py"
        update = False
    print
    if update == True:
        exec_renderfarm()

terminate()
