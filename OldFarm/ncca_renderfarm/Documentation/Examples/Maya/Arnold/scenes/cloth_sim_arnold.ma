//Maya ASCII 2020 scene
//Name: cloth_sim_arnold.ma
//Last modified: Tue, Jan 18, 2022 02:36:47 PM
//Codeset: UTF-8
requires maya "2020";
requires "stereoCamera" "10.0";
requires -nodeType "VRaySettingsNode" -dataType "VRaySunParams" -dataType "vrayFloatVectorData"
		 -dataType "vrayFloatVectorData" -dataType "vrayIntData" "vrayformaya" "5";
requires -nodeType "rmanDisplay" -nodeType "rmanDisplayChannel" -nodeType "rmanGlobals"
		 -nodeType "PxrPathTracer" -nodeType "d_openexr" -nodeType "rmanBakingGlobals" "RenderMan_for_Maya.py" "24.1 @ 2180697";
requires -nodeType "aiOptions" -nodeType "aiAOVDriver" -nodeType "aiAOVFilter" -nodeType "aiSkyDomeLight"
		 -nodeType "aiPhysicalSky" -nodeType "aiStandard" "mtoa" "4.0.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2020";
fileInfo "version" "2020";
fileInfo "cutIdentifier" "201911140446-42a737a01c";
fileInfo "osv" "Linux 3.10.0-1062.18.1.el7.x86_64 #1 SMP Wed Feb 12 14:08:31 UTC 2020 x86_64";
fileInfo "license" "education";
fileInfo "vrayBuild" "5.00.22 87cf50b";
fileInfo "UUID" "3B4BCC80-0000-2A9C-61E6-D07F000003F1";
createNode transform -s -n "persp";
	rename -uid "F5BAF900-0000-E0F6-5A85-7F5700001D47";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 4.9415870429360762 19.840260169996775 36.393582925825697 ;
	setAttr ".r" -type "double3" -24.338352729598036 -352.99999999998363 -2.0027750574898392e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "F5BAF900-0000-E0F6-5A85-7F5700001D48";
	setAttr -k off ".v" no;
	setAttr ".ovr" 1.3;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 41.359300895065061;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".dr" yes;
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -s -n "top";
	rename -uid "F5BAF900-0000-E0F6-5A85-7F5700001D49";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "F5BAF900-0000-E0F6-5A85-7F5700001D4A";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "F5BAF900-0000-E0F6-5A85-7F5700001D4B";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "F5BAF900-0000-E0F6-5A85-7F5700001D4C";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "F5BAF900-0000-E0F6-5A85-7F5700001D4D";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "F5BAF900-0000-E0F6-5A85-7F5700001D4E";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -n "pPlane1";
	rename -uid "F5BAF900-0000-E0F6-5A85-7FBA00001D5F";
	setAttr ".rp" -type "double3" 0 12 0 ;
	setAttr ".sp" -type "double3" 0 12 0 ;
createNode mesh -n "pPlaneShape1" -p "pPlane1";
	rename -uid "F5BAF900-0000-E0F6-5A85-7FBA00001D5E";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 225 ".uvst[0].uvsp[0:224]" -type "float2" 0 0 0.071428575 0
		 0.14285715 0 0.21428573 0 0.2857143 0 0.35714287 0 0.42857146 0 0.5 0 0.5714286 0
		 0.64285719 0 0.71428573 0 0.78571433 0 0.85714293 0 0.92857146 0 1 0 0 0.071428575
		 0.071428575 0.071428575 0.14285715 0.071428575 0.21428573 0.071428575 0.2857143 0.071428575
		 0.35714287 0.071428575 0.42857146 0.071428575 0.5 0.071428575 0.5714286 0.071428575
		 0.64285719 0.071428575 0.71428573 0.071428575 0.78571433 0.071428575 0.85714293 0.071428575
		 0.92857146 0.071428575 1 0.071428575 0 0.14285715 0.071428575 0.14285715 0.14285715
		 0.14285715 0.21428573 0.14285715 0.2857143 0.14285715 0.35714287 0.14285715 0.42857146
		 0.14285715 0.5 0.14285715 0.5714286 0.14285715 0.64285719 0.14285715 0.71428573 0.14285715
		 0.78571433 0.14285715 0.85714293 0.14285715 0.92857146 0.14285715 1 0.14285715 0
		 0.21428573 0.071428575 0.21428573 0.14285715 0.21428573 0.21428573 0.21428573 0.2857143
		 0.21428573 0.35714287 0.21428573 0.42857146 0.21428573 0.5 0.21428573 0.5714286 0.21428573
		 0.64285719 0.21428573 0.71428573 0.21428573 0.78571433 0.21428573 0.85714293 0.21428573
		 0.92857146 0.21428573 1 0.21428573 0 0.2857143 0.071428575 0.2857143 0.14285715 0.2857143
		 0.21428573 0.2857143 0.2857143 0.2857143 0.35714287 0.2857143 0.42857146 0.2857143
		 0.5 0.2857143 0.5714286 0.2857143 0.64285719 0.2857143 0.71428573 0.2857143 0.78571433
		 0.2857143 0.85714293 0.2857143 0.92857146 0.2857143 1 0.2857143 0 0.35714287 0.071428575
		 0.35714287 0.14285715 0.35714287 0.21428573 0.35714287 0.2857143 0.35714287 0.35714287
		 0.35714287 0.42857146 0.35714287 0.5 0.35714287 0.5714286 0.35714287 0.64285719 0.35714287
		 0.71428573 0.35714287 0.78571433 0.35714287 0.85714293 0.35714287 0.92857146 0.35714287
		 1 0.35714287 0 0.42857146 0.071428575 0.42857146 0.14285715 0.42857146 0.21428573
		 0.42857146 0.2857143 0.42857146 0.35714287 0.42857146 0.42857146 0.42857146 0.5 0.42857146
		 0.5714286 0.42857146 0.64285719 0.42857146 0.71428573 0.42857146 0.78571433 0.42857146
		 0.85714293 0.42857146 0.92857146 0.42857146 1 0.42857146 0 0.5 0.071428575 0.5 0.14285715
		 0.5 0.21428573 0.5 0.2857143 0.5 0.35714287 0.5 0.42857146 0.5 0.5 0.5 0.5714286
		 0.5 0.64285719 0.5 0.71428573 0.5 0.78571433 0.5 0.85714293 0.5 0.92857146 0.5 1
		 0.5 0 0.5714286 0.071428575 0.5714286 0.14285715 0.5714286 0.21428573 0.5714286 0.2857143
		 0.5714286 0.35714287 0.5714286 0.42857146 0.5714286 0.5 0.5714286 0.5714286 0.5714286
		 0.64285719 0.5714286 0.71428573 0.5714286 0.78571433 0.5714286 0.85714293 0.5714286
		 0.92857146 0.5714286 1 0.5714286 0 0.64285719 0.071428575 0.64285719 0.14285715 0.64285719
		 0.21428573 0.64285719 0.2857143 0.64285719 0.35714287 0.64285719 0.42857146 0.64285719
		 0.5 0.64285719 0.5714286 0.64285719 0.64285719 0.64285719 0.71428573 0.64285719 0.78571433
		 0.64285719 0.85714293 0.64285719 0.92857146 0.64285719 1 0.64285719 0 0.71428573
		 0.071428575 0.71428573 0.14285715 0.71428573 0.21428573 0.71428573 0.2857143 0.71428573
		 0.35714287 0.71428573 0.42857146 0.71428573 0.5 0.71428573 0.5714286 0.71428573 0.64285719
		 0.71428573 0.71428573 0.71428573 0.78571433 0.71428573 0.85714293 0.71428573 0.92857146
		 0.71428573 1 0.71428573 0 0.78571433 0.071428575 0.78571433 0.14285715 0.78571433
		 0.21428573 0.78571433 0.2857143 0.78571433 0.35714287 0.78571433 0.42857146 0.78571433
		 0.5 0.78571433 0.5714286 0.78571433 0.64285719 0.78571433 0.71428573 0.78571433 0.78571433
		 0.78571433 0.85714293 0.78571433 0.92857146 0.78571433 1 0.78571433 0 0.85714293
		 0.071428575 0.85714293 0.14285715 0.85714293 0.21428573 0.85714293 0.2857143 0.85714293
		 0.35714287 0.85714293 0.42857146 0.85714293 0.5 0.85714293 0.5714286 0.85714293 0.64285719
		 0.85714293 0.71428573 0.85714293 0.78571433 0.85714293 0.85714293 0.85714293 0.92857146
		 0.85714293 1 0.85714293 0 0.92857146 0.071428575 0.92857146 0.14285715 0.92857146
		 0.21428573 0.92857146 0.2857143 0.92857146 0.35714287 0.92857146 0.42857146 0.92857146
		 0.5 0.92857146 0.5714286 0.92857146 0.64285719 0.92857146 0.71428573 0.92857146 0.78571433
		 0.92857146 0.85714293 0.92857146 0.92857146 0.92857146 1 0.92857146 0 1 0.071428575
		 1 0.14285715 1 0.21428573 1 0.2857143 1 0.35714287 1 0.42857146 1 0.5 1 0.5714286
		 1 0.64285719 1 0.71428573 1 0.78571433 1 0.85714293 1 0.92857146 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 225 ".vt";
	setAttr ".vt[0:165]"  -10 12 10 -8.5714283 12 10 -7.14285755 12 10 -5.71428537 12 10
		 -4.28571415 12 10 -2.85714269 12 10 -1.42857075 12 10 0 12 10 1.42857194 12 10 2.85714388 12 10
		 4.28571463 12 10 5.7142868 12 10 7.14285851 12 10 8.57142925 12 10 10 12 10 -10 12 8.5714283
		 -8.5714283 12 8.5714283 -7.14285755 12 8.5714283 -5.71428537 12 8.5714283 -4.28571415 12 8.5714283
		 -2.85714269 12 8.5714283 -1.42857075 12 8.5714283 0 12 8.5714283 1.42857194 12 8.5714283
		 2.85714388 12 8.5714283 4.28571463 12 8.5714283 5.7142868 12 8.5714283 7.14285851 12 8.5714283
		 8.57142925 12 8.5714283 10 12 8.5714283 -10 12 7.14285755 -8.5714283 12 7.14285755
		 -7.14285755 12 7.14285755 -5.71428537 12 7.14285755 -4.28571415 12 7.14285755 -2.85714269 12 7.14285755
		 -1.42857075 12 7.14285755 0 12 7.14285755 1.42857194 12 7.14285755 2.85714388 12 7.14285755
		 4.28571463 12 7.14285755 5.7142868 12 7.14285755 7.14285851 12 7.14285755 8.57142925 12 7.14285755
		 10 12 7.14285755 -10 12 5.71428537 -8.5714283 12 5.71428537 -7.14285755 12 5.71428537
		 -5.71428537 12 5.71428537 -4.28571415 12 5.71428537 -2.85714269 12 5.71428537 -1.42857075 12 5.71428537
		 0 12 5.71428537 1.42857194 12 5.71428537 2.85714388 12 5.71428537 4.28571463 12 5.71428537
		 5.7142868 12 5.71428537 7.14285851 12 5.71428537 8.57142925 12 5.71428537 10 12 5.71428537
		 -10 12 4.28571415 -8.5714283 12 4.28571415 -7.14285755 12 4.28571415 -5.71428537 12 4.28571415
		 -4.28571415 12 4.28571415 -2.85714269 12 4.28571415 -1.42857075 12 4.28571415 0 12 4.28571415
		 1.42857194 12 4.28571415 2.85714388 12 4.28571415 4.28571463 12 4.28571415 5.7142868 12 4.28571415
		 7.14285851 12 4.28571415 8.57142925 12 4.28571415 10 12 4.28571415 -10 12 2.85714269
		 -8.5714283 12 2.85714269 -7.14285755 12 2.85714269 -5.71428537 12 2.85714269 -4.28571415 12 2.85714269
		 -2.85714269 12 2.85714269 -1.42857075 12 2.85714269 0 12 2.85714269 1.42857194 12 2.85714269
		 2.85714388 12 2.85714269 4.28571463 12 2.85714269 5.7142868 12 2.85714269 7.14285851 12 2.85714269
		 8.57142925 12 2.85714269 10 12 2.85714269 -10 12 1.42857075 -8.5714283 12 1.42857075
		 -7.14285755 12 1.42857075 -5.71428537 12 1.42857075 -4.28571415 12 1.42857075 -2.85714269 12 1.42857075
		 -1.42857075 12 1.42857075 0 12 1.42857075 1.42857194 12 1.42857075 2.85714388 12 1.42857075
		 4.28571463 12 1.42857075 5.7142868 12 1.42857075 7.14285851 12 1.42857075 8.57142925 12 1.42857075
		 10 12 1.42857075 -10 12 0 -8.5714283 12 0 -7.14285755 12 0 -5.71428537 12 0 -4.28571415 12 0
		 -2.85714269 12 0 -1.42857075 12 0 0 12 0 1.42857194 12 0 2.85714388 12 0 4.28571463 12 0
		 5.7142868 12 0 7.14285851 12 0 8.57142925 12 0 10 12 0 -10 12 -1.42857194 -8.5714283 12 -1.42857194
		 -7.14285755 12 -1.42857194 -5.71428537 12 -1.42857194 -4.28571415 12 -1.42857194
		 -2.85714269 12 -1.42857194 -1.42857075 12 -1.42857194 0 12 -1.42857194 1.42857194 12 -1.42857194
		 2.85714388 12 -1.42857194 4.28571463 12 -1.42857194 5.7142868 12 -1.42857194 7.14285851 12 -1.42857194
		 8.57142925 12 -1.42857194 10 12 -1.42857194 -10 12 -2.85714388 -8.5714283 12 -2.85714388
		 -7.14285755 12 -2.85714388 -5.71428537 12 -2.85714388 -4.28571415 12 -2.85714388
		 -2.85714269 12 -2.85714388 -1.42857075 12 -2.85714388 0 12 -2.85714388 1.42857194 12 -2.85714388
		 2.85714388 12 -2.85714388 4.28571463 12 -2.85714388 5.7142868 12 -2.85714388 7.14285851 12 -2.85714388
		 8.57142925 12 -2.85714388 10 12 -2.85714388 -10 12 -4.28571463 -8.5714283 12 -4.28571463
		 -7.14285755 12 -4.28571463 -5.71428537 12 -4.28571463 -4.28571415 12 -4.28571463
		 -2.85714269 12 -4.28571463 -1.42857075 12 -4.28571463 0 12 -4.28571463 1.42857194 12 -4.28571463
		 2.85714388 12 -4.28571463 4.28571463 12 -4.28571463 5.7142868 12 -4.28571463 7.14285851 12 -4.28571463
		 8.57142925 12 -4.28571463 10 12 -4.28571463 -10 12 -5.7142868;
	setAttr ".vt[166:224]" -8.5714283 12 -5.7142868 -7.14285755 12 -5.7142868 -5.71428537 12 -5.7142868
		 -4.28571415 12 -5.7142868 -2.85714269 12 -5.7142868 -1.42857075 12 -5.7142868 0 12 -5.7142868
		 1.42857194 12 -5.7142868 2.85714388 12 -5.7142868 4.28571463 12 -5.7142868 5.7142868 12 -5.7142868
		 7.14285851 12 -5.7142868 8.57142925 12 -5.7142868 10 12 -5.7142868 -10 12 -7.14285851
		 -8.5714283 12 -7.14285851 -7.14285755 12 -7.14285851 -5.71428537 12 -7.14285851 -4.28571415 12 -7.14285851
		 -2.85714269 12 -7.14285851 -1.42857075 12 -7.14285851 0 12 -7.14285851 1.42857194 12 -7.14285851
		 2.85714388 12 -7.14285851 4.28571463 12 -7.14285851 5.7142868 12 -7.14285851 7.14285851 12 -7.14285851
		 8.57142925 12 -7.14285851 10 12 -7.14285851 -10 12 -8.57142925 -8.5714283 12 -8.57142925
		 -7.14285755 12 -8.57142925 -5.71428537 12 -8.57142925 -4.28571415 12 -8.57142925
		 -2.85714269 12 -8.57142925 -1.42857075 12 -8.57142925 0 12 -8.57142925 1.42857194 12 -8.57142925
		 2.85714388 12 -8.57142925 4.28571463 12 -8.57142925 5.7142868 12 -8.57142925 7.14285851 12 -8.57142925
		 8.57142925 12 -8.57142925 10 12 -8.57142925 -10 12 -10 -8.5714283 12 -10 -7.14285755 12 -10
		 -5.71428537 12 -10 -4.28571415 12 -10 -2.85714269 12 -10 -1.42857075 12 -10 0 12 -10
		 1.42857194 12 -10 2.85714388 12 -10 4.28571463 12 -10 5.7142868 12 -10 7.14285851 12 -10
		 8.57142925 12 -10 10 12 -10;
	setAttr -s 420 ".ed";
	setAttr ".ed[0:165]"  0 1 0 0 15 0 1 2 0 1 16 1 2 3 0 2 17 1 3 4 0 3 18 1
		 4 5 0 4 19 1 5 6 0 5 20 1 6 7 0 6 21 1 7 8 0 7 22 1 8 9 0 8 23 1 9 10 0 9 24 1 10 11 0
		 10 25 1 11 12 0 11 26 1 12 13 0 12 27 1 13 14 0 13 28 1 14 29 0 15 16 1 15 30 0 16 17 1
		 16 31 1 17 18 1 17 32 1 18 19 1 18 33 1 19 20 1 19 34 1 20 21 1 20 35 1 21 22 1 21 36 1
		 22 23 1 22 37 1 23 24 1 23 38 1 24 25 1 24 39 1 25 26 1 25 40 1 26 27 1 26 41 1 27 28 1
		 27 42 1 28 29 1 28 43 1 29 44 0 30 31 1 30 45 0 31 32 1 31 46 1 32 33 1 32 47 1 33 34 1
		 33 48 1 34 35 1 34 49 1 35 36 1 35 50 1 36 37 1 36 51 1 37 38 1 37 52 1 38 39 1 38 53 1
		 39 40 1 39 54 1 40 41 1 40 55 1 41 42 1 41 56 1 42 43 1 42 57 1 43 44 1 43 58 1 44 59 0
		 45 46 1 45 60 0 46 47 1 46 61 1 47 48 1 47 62 1 48 49 1 48 63 1 49 50 1 49 64 1 50 51 1
		 50 65 1 51 52 1 51 66 1 52 53 1 52 67 1 53 54 1 53 68 1 54 55 1 54 69 1 55 56 1 55 70 1
		 56 57 1 56 71 1 57 58 1 57 72 1 58 59 1 58 73 1 59 74 0 60 61 1 60 75 0 61 62 1 61 76 1
		 62 63 1 62 77 1 63 64 1 63 78 1 64 65 1 64 79 1 65 66 1 65 80 1 66 67 1 66 81 1 67 68 1
		 67 82 1 68 69 1 68 83 1 69 70 1 69 84 1 70 71 1 70 85 1 71 72 1 71 86 1 72 73 1 72 87 1
		 73 74 1 73 88 1 74 89 0 75 76 1 75 90 0 76 77 1 76 91 1 77 78 1 77 92 1 78 79 1 78 93 1
		 79 80 1 79 94 1 80 81 1 80 95 1 81 82 1 81 96 1 82 83 1 82 97 1 83 84 1 83 98 1 84 85 1
		 84 99 1 85 86 1;
	setAttr ".ed[166:331]" 85 100 1 86 87 1 86 101 1 87 88 1 87 102 1 88 89 1 88 103 1
		 89 104 0 90 91 1 90 105 0 91 92 1 91 106 1 92 93 1 92 107 1 93 94 1 93 108 1 94 95 1
		 94 109 1 95 96 1 95 110 1 96 97 1 96 111 1 97 98 1 97 112 1 98 99 1 98 113 1 99 100 1
		 99 114 1 100 101 1 100 115 1 101 102 1 101 116 1 102 103 1 102 117 1 103 104 1 103 118 1
		 104 119 0 105 106 1 105 120 0 106 107 1 106 121 1 107 108 1 107 122 1 108 109 1 108 123 1
		 109 110 1 109 124 1 110 111 1 110 125 1 111 112 1 111 126 1 112 113 1 112 127 1 113 114 1
		 113 128 1 114 115 1 114 129 1 115 116 1 115 130 1 116 117 1 116 131 1 117 118 1 117 132 1
		 118 119 1 118 133 1 119 134 0 120 121 1 120 135 0 121 122 1 121 136 1 122 123 1 122 137 1
		 123 124 1 123 138 1 124 125 1 124 139 1 125 126 1 125 140 1 126 127 1 126 141 1 127 128 1
		 127 142 1 128 129 1 128 143 1 129 130 1 129 144 1 130 131 1 130 145 1 131 132 1 131 146 1
		 132 133 1 132 147 1 133 134 1 133 148 1 134 149 0 135 136 1 135 150 0 136 137 1 136 151 1
		 137 138 1 137 152 1 138 139 1 138 153 1 139 140 1 139 154 1 140 141 1 140 155 1 141 142 1
		 141 156 1 142 143 1 142 157 1 143 144 1 143 158 1 144 145 1 144 159 1 145 146 1 145 160 1
		 146 147 1 146 161 1 147 148 1 147 162 1 148 149 1 148 163 1 149 164 0 150 151 1 150 165 0
		 151 152 1 151 166 1 152 153 1 152 167 1 153 154 1 153 168 1 154 155 1 154 169 1 155 156 1
		 155 170 1 156 157 1 156 171 1 157 158 1 157 172 1 158 159 1 158 173 1 159 160 1 159 174 1
		 160 161 1 160 175 1 161 162 1 161 176 1 162 163 1 162 177 1 163 164 1 163 178 1 164 179 0
		 165 166 1 165 180 0 166 167 1 166 181 1 167 168 1 167 182 1 168 169 1 168 183 1 169 170 1
		 169 184 1 170 171 1 170 185 1 171 172 1;
	setAttr ".ed[332:419]" 171 186 1 172 173 1 172 187 1 173 174 1 173 188 1 174 175 1
		 174 189 1 175 176 1 175 190 1 176 177 1 176 191 1 177 178 1 177 192 1 178 179 1 178 193 1
		 179 194 0 180 181 1 180 195 0 181 182 1 181 196 1 182 183 1 182 197 1 183 184 1 183 198 1
		 184 185 1 184 199 1 185 186 1 185 200 1 186 187 1 186 201 1 187 188 1 187 202 1 188 189 1
		 188 203 1 189 190 1 189 204 1 190 191 1 190 205 1 191 192 1 191 206 1 192 193 1 192 207 1
		 193 194 1 193 208 1 194 209 0 195 196 1 195 210 0 196 197 1 196 211 1 197 198 1 197 212 1
		 198 199 1 198 213 1 199 200 1 199 214 1 200 201 1 200 215 1 201 202 1 201 216 1 202 203 1
		 202 217 1 203 204 1 203 218 1 204 205 1 204 219 1 205 206 1 205 220 1 206 207 1 206 221 1
		 207 208 1 207 222 1 208 209 1 208 223 1 209 224 0 210 211 0 211 212 0 212 213 0 213 214 0
		 214 215 0 215 216 0 216 217 0 217 218 0 218 219 0 219 220 0 220 221 0 221 222 0 222 223 0
		 223 224 0;
	setAttr -s 196 -ch 784 ".fc[0:195]" -type "polyFaces" 
		f 4 0 3 -30 -2
		mu 0 4 0 1 16 15
		f 4 2 5 -32 -4
		mu 0 4 1 2 17 16
		f 4 4 7 -34 -6
		mu 0 4 2 3 18 17
		f 4 6 9 -36 -8
		mu 0 4 3 4 19 18
		f 4 8 11 -38 -10
		mu 0 4 4 5 20 19
		f 4 10 13 -40 -12
		mu 0 4 5 6 21 20
		f 4 12 15 -42 -14
		mu 0 4 6 7 22 21
		f 4 14 17 -44 -16
		mu 0 4 7 8 23 22
		f 4 16 19 -46 -18
		mu 0 4 8 9 24 23
		f 4 18 21 -48 -20
		mu 0 4 9 10 25 24
		f 4 20 23 -50 -22
		mu 0 4 10 11 26 25
		f 4 22 25 -52 -24
		mu 0 4 11 12 27 26
		f 4 24 27 -54 -26
		mu 0 4 12 13 28 27
		f 4 26 28 -56 -28
		mu 0 4 13 14 29 28
		f 4 29 32 -59 -31
		mu 0 4 15 16 31 30
		f 4 31 34 -61 -33
		mu 0 4 16 17 32 31
		f 4 33 36 -63 -35
		mu 0 4 17 18 33 32
		f 4 35 38 -65 -37
		mu 0 4 18 19 34 33
		f 4 37 40 -67 -39
		mu 0 4 19 20 35 34
		f 4 39 42 -69 -41
		mu 0 4 20 21 36 35
		f 4 41 44 -71 -43
		mu 0 4 21 22 37 36
		f 4 43 46 -73 -45
		mu 0 4 22 23 38 37
		f 4 45 48 -75 -47
		mu 0 4 23 24 39 38
		f 4 47 50 -77 -49
		mu 0 4 24 25 40 39
		f 4 49 52 -79 -51
		mu 0 4 25 26 41 40
		f 4 51 54 -81 -53
		mu 0 4 26 27 42 41
		f 4 53 56 -83 -55
		mu 0 4 27 28 43 42
		f 4 55 57 -85 -57
		mu 0 4 28 29 44 43
		f 4 58 61 -88 -60
		mu 0 4 30 31 46 45
		f 4 60 63 -90 -62
		mu 0 4 31 32 47 46
		f 4 62 65 -92 -64
		mu 0 4 32 33 48 47
		f 4 64 67 -94 -66
		mu 0 4 33 34 49 48
		f 4 66 69 -96 -68
		mu 0 4 34 35 50 49
		f 4 68 71 -98 -70
		mu 0 4 35 36 51 50
		f 4 70 73 -100 -72
		mu 0 4 36 37 52 51
		f 4 72 75 -102 -74
		mu 0 4 37 38 53 52
		f 4 74 77 -104 -76
		mu 0 4 38 39 54 53
		f 4 76 79 -106 -78
		mu 0 4 39 40 55 54
		f 4 78 81 -108 -80
		mu 0 4 40 41 56 55
		f 4 80 83 -110 -82
		mu 0 4 41 42 57 56
		f 4 82 85 -112 -84
		mu 0 4 42 43 58 57
		f 4 84 86 -114 -86
		mu 0 4 43 44 59 58
		f 4 87 90 -117 -89
		mu 0 4 45 46 61 60
		f 4 89 92 -119 -91
		mu 0 4 46 47 62 61
		f 4 91 94 -121 -93
		mu 0 4 47 48 63 62
		f 4 93 96 -123 -95
		mu 0 4 48 49 64 63
		f 4 95 98 -125 -97
		mu 0 4 49 50 65 64
		f 4 97 100 -127 -99
		mu 0 4 50 51 66 65
		f 4 99 102 -129 -101
		mu 0 4 51 52 67 66
		f 4 101 104 -131 -103
		mu 0 4 52 53 68 67
		f 4 103 106 -133 -105
		mu 0 4 53 54 69 68
		f 4 105 108 -135 -107
		mu 0 4 54 55 70 69
		f 4 107 110 -137 -109
		mu 0 4 55 56 71 70
		f 4 109 112 -139 -111
		mu 0 4 56 57 72 71
		f 4 111 114 -141 -113
		mu 0 4 57 58 73 72
		f 4 113 115 -143 -115
		mu 0 4 58 59 74 73
		f 4 116 119 -146 -118
		mu 0 4 60 61 76 75
		f 4 118 121 -148 -120
		mu 0 4 61 62 77 76
		f 4 120 123 -150 -122
		mu 0 4 62 63 78 77
		f 4 122 125 -152 -124
		mu 0 4 63 64 79 78
		f 4 124 127 -154 -126
		mu 0 4 64 65 80 79
		f 4 126 129 -156 -128
		mu 0 4 65 66 81 80
		f 4 128 131 -158 -130
		mu 0 4 66 67 82 81
		f 4 130 133 -160 -132
		mu 0 4 67 68 83 82
		f 4 132 135 -162 -134
		mu 0 4 68 69 84 83
		f 4 134 137 -164 -136
		mu 0 4 69 70 85 84
		f 4 136 139 -166 -138
		mu 0 4 70 71 86 85
		f 4 138 141 -168 -140
		mu 0 4 71 72 87 86
		f 4 140 143 -170 -142
		mu 0 4 72 73 88 87
		f 4 142 144 -172 -144
		mu 0 4 73 74 89 88
		f 4 145 148 -175 -147
		mu 0 4 75 76 91 90
		f 4 147 150 -177 -149
		mu 0 4 76 77 92 91
		f 4 149 152 -179 -151
		mu 0 4 77 78 93 92
		f 4 151 154 -181 -153
		mu 0 4 78 79 94 93
		f 4 153 156 -183 -155
		mu 0 4 79 80 95 94
		f 4 155 158 -185 -157
		mu 0 4 80 81 96 95
		f 4 157 160 -187 -159
		mu 0 4 81 82 97 96
		f 4 159 162 -189 -161
		mu 0 4 82 83 98 97
		f 4 161 164 -191 -163
		mu 0 4 83 84 99 98
		f 4 163 166 -193 -165
		mu 0 4 84 85 100 99
		f 4 165 168 -195 -167
		mu 0 4 85 86 101 100
		f 4 167 170 -197 -169
		mu 0 4 86 87 102 101
		f 4 169 172 -199 -171
		mu 0 4 87 88 103 102
		f 4 171 173 -201 -173
		mu 0 4 88 89 104 103
		f 4 174 177 -204 -176
		mu 0 4 90 91 106 105
		f 4 176 179 -206 -178
		mu 0 4 91 92 107 106
		f 4 178 181 -208 -180
		mu 0 4 92 93 108 107
		f 4 180 183 -210 -182
		mu 0 4 93 94 109 108
		f 4 182 185 -212 -184
		mu 0 4 94 95 110 109
		f 4 184 187 -214 -186
		mu 0 4 95 96 111 110
		f 4 186 189 -216 -188
		mu 0 4 96 97 112 111
		f 4 188 191 -218 -190
		mu 0 4 97 98 113 112
		f 4 190 193 -220 -192
		mu 0 4 98 99 114 113
		f 4 192 195 -222 -194
		mu 0 4 99 100 115 114
		f 4 194 197 -224 -196
		mu 0 4 100 101 116 115
		f 4 196 199 -226 -198
		mu 0 4 101 102 117 116
		f 4 198 201 -228 -200
		mu 0 4 102 103 118 117
		f 4 200 202 -230 -202
		mu 0 4 103 104 119 118
		f 4 203 206 -233 -205
		mu 0 4 105 106 121 120
		f 4 205 208 -235 -207
		mu 0 4 106 107 122 121
		f 4 207 210 -237 -209
		mu 0 4 107 108 123 122
		f 4 209 212 -239 -211
		mu 0 4 108 109 124 123
		f 4 211 214 -241 -213
		mu 0 4 109 110 125 124
		f 4 213 216 -243 -215
		mu 0 4 110 111 126 125
		f 4 215 218 -245 -217
		mu 0 4 111 112 127 126
		f 4 217 220 -247 -219
		mu 0 4 112 113 128 127
		f 4 219 222 -249 -221
		mu 0 4 113 114 129 128
		f 4 221 224 -251 -223
		mu 0 4 114 115 130 129
		f 4 223 226 -253 -225
		mu 0 4 115 116 131 130
		f 4 225 228 -255 -227
		mu 0 4 116 117 132 131
		f 4 227 230 -257 -229
		mu 0 4 117 118 133 132
		f 4 229 231 -259 -231
		mu 0 4 118 119 134 133
		f 4 232 235 -262 -234
		mu 0 4 120 121 136 135
		f 4 234 237 -264 -236
		mu 0 4 121 122 137 136
		f 4 236 239 -266 -238
		mu 0 4 122 123 138 137
		f 4 238 241 -268 -240
		mu 0 4 123 124 139 138
		f 4 240 243 -270 -242
		mu 0 4 124 125 140 139
		f 4 242 245 -272 -244
		mu 0 4 125 126 141 140
		f 4 244 247 -274 -246
		mu 0 4 126 127 142 141
		f 4 246 249 -276 -248
		mu 0 4 127 128 143 142
		f 4 248 251 -278 -250
		mu 0 4 128 129 144 143
		f 4 250 253 -280 -252
		mu 0 4 129 130 145 144
		f 4 252 255 -282 -254
		mu 0 4 130 131 146 145
		f 4 254 257 -284 -256
		mu 0 4 131 132 147 146
		f 4 256 259 -286 -258
		mu 0 4 132 133 148 147
		f 4 258 260 -288 -260
		mu 0 4 133 134 149 148
		f 4 261 264 -291 -263
		mu 0 4 135 136 151 150
		f 4 263 266 -293 -265
		mu 0 4 136 137 152 151
		f 4 265 268 -295 -267
		mu 0 4 137 138 153 152
		f 4 267 270 -297 -269
		mu 0 4 138 139 154 153
		f 4 269 272 -299 -271
		mu 0 4 139 140 155 154
		f 4 271 274 -301 -273
		mu 0 4 140 141 156 155
		f 4 273 276 -303 -275
		mu 0 4 141 142 157 156
		f 4 275 278 -305 -277
		mu 0 4 142 143 158 157
		f 4 277 280 -307 -279
		mu 0 4 143 144 159 158
		f 4 279 282 -309 -281
		mu 0 4 144 145 160 159
		f 4 281 284 -311 -283
		mu 0 4 145 146 161 160
		f 4 283 286 -313 -285
		mu 0 4 146 147 162 161
		f 4 285 288 -315 -287
		mu 0 4 147 148 163 162
		f 4 287 289 -317 -289
		mu 0 4 148 149 164 163
		f 4 290 293 -320 -292
		mu 0 4 150 151 166 165
		f 4 292 295 -322 -294
		mu 0 4 151 152 167 166
		f 4 294 297 -324 -296
		mu 0 4 152 153 168 167
		f 4 296 299 -326 -298
		mu 0 4 153 154 169 168
		f 4 298 301 -328 -300
		mu 0 4 154 155 170 169
		f 4 300 303 -330 -302
		mu 0 4 155 156 171 170
		f 4 302 305 -332 -304
		mu 0 4 156 157 172 171
		f 4 304 307 -334 -306
		mu 0 4 157 158 173 172
		f 4 306 309 -336 -308
		mu 0 4 158 159 174 173
		f 4 308 311 -338 -310
		mu 0 4 159 160 175 174
		f 4 310 313 -340 -312
		mu 0 4 160 161 176 175
		f 4 312 315 -342 -314
		mu 0 4 161 162 177 176
		f 4 314 317 -344 -316
		mu 0 4 162 163 178 177
		f 4 316 318 -346 -318
		mu 0 4 163 164 179 178
		f 4 319 322 -349 -321
		mu 0 4 165 166 181 180
		f 4 321 324 -351 -323
		mu 0 4 166 167 182 181
		f 4 323 326 -353 -325
		mu 0 4 167 168 183 182
		f 4 325 328 -355 -327
		mu 0 4 168 169 184 183
		f 4 327 330 -357 -329
		mu 0 4 169 170 185 184
		f 4 329 332 -359 -331
		mu 0 4 170 171 186 185
		f 4 331 334 -361 -333
		mu 0 4 171 172 187 186
		f 4 333 336 -363 -335
		mu 0 4 172 173 188 187
		f 4 335 338 -365 -337
		mu 0 4 173 174 189 188
		f 4 337 340 -367 -339
		mu 0 4 174 175 190 189
		f 4 339 342 -369 -341
		mu 0 4 175 176 191 190
		f 4 341 344 -371 -343
		mu 0 4 176 177 192 191
		f 4 343 346 -373 -345
		mu 0 4 177 178 193 192
		f 4 345 347 -375 -347
		mu 0 4 178 179 194 193
		f 4 348 351 -378 -350
		mu 0 4 180 181 196 195
		f 4 350 353 -380 -352
		mu 0 4 181 182 197 196
		f 4 352 355 -382 -354
		mu 0 4 182 183 198 197
		f 4 354 357 -384 -356
		mu 0 4 183 184 199 198
		f 4 356 359 -386 -358
		mu 0 4 184 185 200 199
		f 4 358 361 -388 -360
		mu 0 4 185 186 201 200
		f 4 360 363 -390 -362
		mu 0 4 186 187 202 201
		f 4 362 365 -392 -364
		mu 0 4 187 188 203 202
		f 4 364 367 -394 -366
		mu 0 4 188 189 204 203
		f 4 366 369 -396 -368
		mu 0 4 189 190 205 204
		f 4 368 371 -398 -370
		mu 0 4 190 191 206 205
		f 4 370 373 -400 -372
		mu 0 4 191 192 207 206
		f 4 372 375 -402 -374
		mu 0 4 192 193 208 207
		f 4 374 376 -404 -376
		mu 0 4 193 194 209 208
		f 4 377 380 -407 -379
		mu 0 4 195 196 211 210
		f 4 379 382 -408 -381
		mu 0 4 196 197 212 211
		f 4 381 384 -409 -383
		mu 0 4 197 198 213 212
		f 4 383 386 -410 -385
		mu 0 4 198 199 214 213
		f 4 385 388 -411 -387
		mu 0 4 199 200 215 214
		f 4 387 390 -412 -389
		mu 0 4 200 201 216 215
		f 4 389 392 -413 -391
		mu 0 4 201 202 217 216
		f 4 391 394 -414 -393
		mu 0 4 202 203 218 217
		f 4 393 396 -415 -395
		mu 0 4 203 204 219 218
		f 4 395 398 -416 -397
		mu 0 4 204 205 220 219
		f 4 397 400 -417 -399
		mu 0 4 205 206 221 220
		f 4 399 402 -418 -401
		mu 0 4 206 207 222 221
		f 4 401 404 -419 -403
		mu 0 4 207 208 223 222
		f 4 403 405 -420 -405
		mu 0 4 208 209 224 223;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode mesh -n "outputCloth1" -p "pPlane1";
	rename -uid "F5BAF900-0000-E0F6-5A85-808500001DA3";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".qsp" 0;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "pPrism1";
	rename -uid "F5BAF900-0000-E0F6-5A85-800F00001D7B";
	setAttr ".rp" -type "double3" -1.2306710232191134 4.0000001759689683 -0.89857845512316548 ;
	setAttr ".sp" -type "double3" -1.2306710232191134 4.0000001759689683 -0.89857845512316548 ;
createNode mesh -n "pPrismShape1" -p "pPrism1";
	rename -uid "F5BAF900-0000-E0F6-5A85-800F00001D7A";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 1 1 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".qsp" 0;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode mesh -n "polySurfaceShape1" -p "pPrism1";
	rename -uid "F5BAF900-0000-E0F6-5A85-826300001E08";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.421875 0.020933509
		 0.33899885 0.29156646 0.65625 0.15625 0.0064586401 0.3125 0.16096774 0.3125 0.83903241
		 0.3125 0.99354136 0.3125 0.0064586401 0.68843985 0.16096774 0.68843985 0.83903241
		 0.68843985 0.99354136 0.68843985 0.33899885 0.70843351 0.421875 0.97906649 0.65625
		 0.84375;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 6 ".vt[0:5]"  -5.56079769 0 -5.89857864 -5.56079817 0 4.10142136
		 3.099455833 0 -0.89857799 -5.56079769 8 -5.89857864 -5.56079817 8 4.10142136 3.099455833 8 -0.89857799;
	setAttr -s 9 ".ed[0:8]"  0 1 0 1 2 0 2 0 0 3 4 0 4 5 0 5 3 0 0 3 0
		 1 4 0 2 5 0;
	setAttr -s 5 -ch 18 ".fc[0:4]" -type "polyFaces" 
		f 4 0 7 -4 -7
		mu 0 4 3 4 8 7
		f 4 1 8 -5 -8
		mu 0 4 4 5 9 8
		f 4 2 6 -6 -9
		mu 0 4 5 6 10 9
		f 3 -3 -2 -1
		mu 0 3 0 2 1
		f 3 3 4 5
		mu 0 3 12 11 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".qsp" 0;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode nucleus -n "nucleus1";
	rename -uid "F5BAF900-0000-E0F6-5A85-808500001D9C";
	setAttr ".nupl" yes;
createNode transform -n "nCloth1";
	rename -uid "F5BAF900-0000-E0F6-5A85-808500001DA0";
	setAttr -l on ".t";
	setAttr -l on ".r";
	setAttr -l on ".s";
createNode nCloth -n "nClothShape1" -p "nCloth1";
	rename -uid "F5BAF900-0000-E0F6-5A85-808500001D9F";
	addAttr -ci true -sn "lifespan" -ln "lifespan" -at "double";
	addAttr -s false -ci true -sn "lifespanPP" -ln "lifespanPP" -dt "doubleArray";
	addAttr -ci true -h true -sn "lifespanPP0" -ln "lifespanPP0" -dt "doubleArray";
	setAttr -k off ".v";
	setAttr ".gf" -type "Int32Array" 0 ;
	setAttr ".pos0" -type "vectorArray" 0 ;
	setAttr ".vel0" -type "vectorArray" 0 ;
	setAttr ".acc0" -type "vectorArray" 0 ;
	setAttr ".mas0" -type "doubleArray" 0 ;
	setAttr ".id0" -type "doubleArray" 0 ;
	setAttr ".nid" 225;
	setAttr ".bt0" -type "doubleArray" 0 ;
	setAttr ".ag0" -type "doubleArray" 0 ;
	setAttr -k off ".dve";
	setAttr -k off ".lfm";
	setAttr -k off ".lfr";
	setAttr -k off ".ead";
	setAttr ".irbx" -type "string" "";
	setAttr ".irax" -type "string" "";
	setAttr ".icx" -type "string" "";
	setAttr -k off ".dw";
	setAttr -k off ".fiw";
	setAttr -k off ".con";
	setAttr -k off ".eiw";
	setAttr -k off ".mxc";
	setAttr -k off ".lod";
	setAttr -k off ".inh";
	setAttr -k off ".stf";
	setAttr -k off ".igs";
	setAttr -k off ".ecfh";
	setAttr -k off ".tgs";
	setAttr -k off ".gsm";
	setAttr -k off ".chd";
	setAttr ".chw" 51;
	setAttr -k off ".trd";
	setAttr -k off ".prt";
	setAttr ".thss" 0.1414213627576828;
	setAttr ".scfl" 3;
	setAttr ".por" 0.5656854510307312;
	setAttr -s 2 ".fsc[0:1]"  0 1 1 1 0 1;
	setAttr -s 2 ".pfdo[0:1]"  0 1 1 1 0 1;
	setAttr ".lsou" yes;
	setAttr -k on ".lifespan" 1;
	setAttr ".lifespanPP0" -type "doubleArray" 0 ;
createNode transform -n "nRigid1";
	rename -uid "F5BAF900-0000-E0F6-5A85-808A00001DAF";
	setAttr -l on ".t";
	setAttr -l on ".r";
	setAttr -l on ".s";
createNode nRigid -n "nRigidShape1" -p "nRigid1";
	rename -uid "F5BAF900-0000-E0F6-5A85-808A00001DAE";
	addAttr -ci true -sn "lifespan" -ln "lifespan" -at "double";
	addAttr -s false -ci true -sn "lifespanPP" -ln "lifespanPP" -dt "doubleArray";
	addAttr -ci true -h true -sn "lifespanPP0" -ln "lifespanPP0" -dt "doubleArray";
	setAttr -k off ".v";
	setAttr ".gf" -type "Int32Array" 0 ;
	setAttr ".pos0" -type "vectorArray" 0 ;
	setAttr ".vel0" -type "vectorArray" 0 ;
	setAttr ".acc0" -type "vectorArray" 0 ;
	setAttr ".mas0" -type "doubleArray" 0 ;
	setAttr ".id0" -type "doubleArray" 0 ;
	setAttr ".nid" 6;
	setAttr ".bt0" -type "doubleArray" 0 ;
	setAttr ".ag0" -type "doubleArray" 0 ;
	setAttr -k off ".dve";
	setAttr -k off ".lfm";
	setAttr -k off ".lfr";
	setAttr -k off ".ead";
	setAttr ".irbx" -type "string" "";
	setAttr ".irax" -type "string" "";
	setAttr ".icx" -type "string" "";
	setAttr -k off ".dw";
	setAttr -k off ".fiw";
	setAttr -k off ".con";
	setAttr -k off ".eiw";
	setAttr -k off ".mxc";
	setAttr -k off ".lod";
	setAttr -k off ".inh";
	setAttr -k off ".stf";
	setAttr -k off ".igs";
	setAttr -k off ".ecfh";
	setAttr -k off ".tgs";
	setAttr -k off ".gsm";
	setAttr -k off ".chd";
	setAttr ".chw" 51;
	setAttr -k off ".trd";
	setAttr -k off ".prt";
	setAttr ".thss" 0.065160743892192841;
	setAttr ".actv" no;
	setAttr ".scld" no;
	setAttr ".por" 0.26064297556877136;
	setAttr ".tpc" yes;
	setAttr -s 2 ".fsc[0:1]"  0 1 1 1 0 1;
	setAttr -s 2 ".pfdo[0:1]"  0 1 1 1 0 1;
	setAttr -k on ".lifespan" 1;
	setAttr ".lifespanPP0" -type "doubleArray" 0 ;
createNode transform -n "pPlane2";
	rename -uid "F5BAF900-0000-E0F6-5A85-844E00001ECE";
	setAttr ".t" -type "double3" -6.337056364893157 0 1.1148387811513096 ;
	setAttr ".s" -type "double3" 90.650125777505664 44.78431617940808 56.717988937656926 ;
createNode mesh -n "pPlaneShape2" -p "pPlane2";
	rename -uid "F5BAF900-0000-E0F6-5A85-844E00001ECD";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "aiSkyDomeLight1";
	rename -uid "F5BAF900-0000-E0F6-5A85-85AD00001F39";
createNode aiSkyDomeLight -n "aiSkyDomeLightShape1" -p "aiSkyDomeLight1";
	rename -uid "F5BAF900-0000-E0F6-5A85-85AD00001F38";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr -k off ".v";
	setAttr ".csh" no;
	setAttr ".rcsh" no;
	setAttr ".ai_samples" 2;
	setAttr ".aal" -type "attributeAlias" {"exposure","aiExposure"} ;
createNode rmanGlobals -s -n "rmanGlobals";
	rename -uid "5B233C80-0000-2168-61E1-82C500000339";
	setAttr ".cch" no;
	setAttr ".fzn" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".hider_minSamples" 0;
	setAttr ".hider_maxSamples" 128;
	setAttr ".ri_pixelVariance" 0.014999999664723873;
	setAttr ".hider_incremental" yes;
	setAttr ".ipr_hider_maxSamples" 64;
	setAttr ".ipr_ri_pixelVariance" 0.05000000074505806;
	setAttr ".ipr_ri_decidither" 0;
	setAttr ".ri_maxSpecularDepth" 4;
	setAttr ".ri_maxDiffuseDepth" 1;
	setAttr ".ri_displayFilter" -type "string" "gaussian";
	setAttr ".ri_displayFilterSize" -type "float2" 2 2 ;
	setAttr ".pixelFilterMode" -type "string" "importance";
	setAttr ".renderVariant" -type "string" "ris";
	setAttr ".xpuMode" -type "long2" 1 1 ;
	setAttr ".motionBlur" 0;
	setAttr ".cameraBlur" no;
	setAttr ".shutterAngle" 180;
	setAttr ".shutterOpenEnd" 0;
	setAttr ".shutterCloseStart" 1;
	setAttr ".shutterTiming" 0;
	setAttr ".motionSamples" 2;
	setAttr ".ocioConfig" 0;
	setAttr ".ocioConfigPath" -type "string" "";
	setAttr ".ocioColorSpaceName" -type "string" "";
	setAttr ".enableStylizedLooks" no;
	setAttr ".displayFilters[0]" -type "string" "";
	setAttr ".sampleFilters[0]" -type "string" "";
	setAttr ".outputAllShaders" no;
	setAttr ".reentrantProcedurals" yes;
	setAttr ".outputShadowAOV" 0;
	setAttr ".enableImagePlaneFilter" yes;
	setAttr ".learnLightSelection" yes;
	setAttr ".shadowBumpTerminator" yes;
	setAttr ".blueNoise" yes;
	setAttr ".geomShadowTermBias" yes;
	setAttr ".roughnessMollification" 1;
	setAttr ".opt_bucket_order" -type "string" "circle";
	setAttr ".limits_bucketsize" -type "long2" 16 16 ;
	setAttr ".limits_othreshold" -type "float3" 0.99599999 0.99599999 0.99599999 ;
	setAttr ".rfm_referenceFrame" 0;
	setAttr ".adaptiveMetric" -type "string" "variance";
	setAttr ".hider_darkfalloff" 0.02500000037252903;
	setAttr ".hider_exposurebracket" -type "float2" -1 1 ;
	setAttr ".ri_hider_adaptAll" no;
	setAttr ".dice_micropolygonlength" 1;
	setAttr ".dice_watertight" no;
	setAttr ".dice_referenceCameraType" 0;
	setAttr ".dice_referenceCamera" -type "string" "";
	setAttr ".hair_minWidth" 0.5;
	setAttr ".trace_autobias" yes;
	setAttr ".trace_bias" 0.0010000000474974513;
	setAttr ".trace_worldorigin" -type "string" "camera";
	setAttr ".trace_worldoffset" -type "float3" 0 0 0 ;
	setAttr ".opt_oslmatchcpp" no;
	setAttr ".opt_oslSIMDEnable" yes;
	setAttr ".opt_oslVerbosity" 0;
	setAttr ".opt_oslStatistics" 0;
	setAttr ".deep_quality" 0.75;
	setAttr ".opt_cropWindowEnable" no;
	setAttr ".opt_cropWindowTopLeft" -type "float2" 0 0 ;
	setAttr ".opt_cropWindowBottomRight" -type "float2" 1 1 ;
	setAttr ".user_sceneUnits" 1;
	setAttr ".user_iesIgnoreWatts" yes;
	setAttr ".limits_texturememory" 4096;
	setAttr ".limits_geocachememory" 4096;
	setAttr ".limits_opacitycachememory" 2048;
	setAttr ".statistics_level" 1;
	setAttr ".statistics_xmlfilename" -type "string" "";
	setAttr ".lpe_reload_definitions" -type "string" "";
	setAttr ".lpe_diffuse2" -type "string" "Diffuse,HairDiffuse,diffuse,translucent,hair4,irradiance";
	setAttr ".lpe_diffuse3" -type "string" "Subsurface,subsurface";
	setAttr ".lpe_specular2" -type "string" "Specular,HairSpecularR,specular,hair1";
	setAttr ".lpe_specular3" -type "string" "RoughSpecular,HairSpecularTRT,hair3";
	setAttr ".lpe_specular4" -type "string" "Clearcoat";
	setAttr ".lpe_specular5" -type "string" "Iridescence";
	setAttr ".lpe_specular6" -type "string" "Fuzz,HairSpecularGLINTS";
	setAttr ".lpe_specular7" -type "string" "SingleScatter,HairSpecularTT,hair2";
	setAttr ".lpe_specular8" -type "string" "Glass,specular";
	setAttr ".lpe_user2" -type "string" "Albedo,DiffuseAlbedo,SubsurfaceAlbedo,HairAlbedo";
	setAttr ".lpe_user3" -type "string" "Position";
	setAttr ".lpe_user4" -type "string" "UserColor";
	setAttr ".lpe_user5" -type "string" "";
	setAttr ".lpe_user6" -type "string" "Normal,DiffuseNormal,HairTangent,SubsurfaceNormal,SpecularNormal,RoughSpecularNormal,SingleScatterNormal,FuzzNormal,IridescenceNormal,GlassNormal";
	setAttr ".lpe_user7" -type "string" "";
	setAttr ".lpe_user8" -type "string" "";
	setAttr ".lpe_user9" -type "string" "";
	setAttr ".lpe_user10" -type "string" "";
	setAttr ".lpe_user11" -type "string" "";
	setAttr ".lpe_user12" -type "string" "";
	setAttr ".imageFileFormat" -type "string" "<scene>_<layer>_<camera>_<aov>.<f4>.<ext>";
	setAttr ".ribFileFormat" -type "string" "<camera><layer>.<f4>.rib";
	setAttr ".version" 1;
	setAttr ".take" 1;
	setAttr ".imageOutputDir" -type "string" "<ws>/images/<scene>_v<version>_t<take>";
	setAttr ".ribOutputDir" -type "string" "<ws>/renderman/rib/<scene>/v<version>_t<take>";
	setAttr -s 10 ".UserTokens";
	setAttr ".UserTokens[0].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[0].userTokenValues" -type "string" "";
	setAttr ".UserTokens[1].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[1].userTokenValues" -type "string" "";
	setAttr ".UserTokens[2].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[2].userTokenValues" -type "string" "";
	setAttr ".UserTokens[3].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[3].userTokenValues" -type "string" "";
	setAttr ".UserTokens[4].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[4].userTokenValues" -type "string" "";
	setAttr ".UserTokens[5].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[5].userTokenValues" -type "string" "";
	setAttr ".UserTokens[6].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[6].userTokenValues" -type "string" "";
	setAttr ".UserTokens[7].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[7].userTokenValues" -type "string" "";
	setAttr ".UserTokens[8].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[8].userTokenValues" -type "string" "";
	setAttr ".UserTokens[9].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[9].userTokenValues" -type "string" "";
	setAttr ".rlfData" -type "string" "init";
	setAttr ".jobid" -type "string" "";
	setAttr ".txmanagerData" -type "string" "";
createNode PxrPathTracer -s -n "PxrPathTracer";
	rename -uid "5B233C80-0000-2168-61E1-82C50000033A";
	setAttr ".cch" no;
	setAttr ".fzn" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".maxIndirectBounces" 8;
	setAttr ".maxContinuationLength" -1;
	setAttr ".maxNonStochasticOpacityEvents" 0;
	setAttr ".sampleMode" -type "string" "bxdf";
	setAttr ".numLightSamples" 1;
	setAttr ".numBxdfSamples" 1;
	setAttr ".numIndirectSamples" 1;
	setAttr ".numDiffuseSamples" 1;
	setAttr ".numSpecularSamples" 1;
	setAttr ".numSubsurfaceSamples" 1;
	setAttr ".numRefractionSamples" 1;
	setAttr ".allowCaustics" no;
	setAttr ".accumOpacity" no;
	setAttr ".rouletteDepth" 4;
	setAttr ".rouletteThreshold" 0.20000000298023224;
	setAttr ".clampDepth" 2;
	setAttr ".clampLuminance" 10;
createNode rmanBakingGlobals -s -n "rmanBakingGlobals";
	rename -uid "5B233C80-0000-2168-61E1-82C50000033B";
	setAttr ".cch" no;
	setAttr ".fzn" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".bakeMode" 0;
	setAttr ".bakingImageFileFormat" -type "string" "<scene>_<user:bakingIdentifier>_<aov>.<ext>";
	setAttr ".resolution" 512;
	setAttr ".rman_diceDistanceLength" 0.05000000074505806;
	setAttr ".ri_maxSpecularDepth" 4;
	setAttr ".ri_maxDiffuseDepth" 1;
	setAttr ".init" 0;
createNode rmanDisplay -n "rmanDefaultBakeDisplay";
	rename -uid "033E1C80-0000-2627-61E6-821D0000028E";
	setAttr ".cch" no;
	setAttr ".fzn" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".enable" yes;
	setAttr ".denoise" no;
	setAttr ".frameMode" 0;
	setAttr ".remapBreakPoint" 0;
	setAttr ".remapMaxValue" 0;
	setAttr ".remapSmoothness" 0;
	setAttr -s 2 ".displayChannels";
	setAttr ".name" -type "string" "";
createNode rmanDisplayChannel -n "diffuse";
	rename -uid "033E1C80-0000-2627-61E6-821D0000028F";
	setAttr ".cch" no;
	setAttr ".fzn" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".enable" yes;
	setAttr ".channelType" -type "string" "color";
	setAttr ".channelSource" -type "string" "lpe:C(D[DS]*[LO])|[LO]";
	setAttr ".lpeLightGroup" -type "string" "";
	setAttr ".filter" -type "string" "inherit from display";
	setAttr ".filterwidth" -type "float2" -1 -1 ;
	setAttr ".statistics" -type "string" "";
	setAttr ".relativepixelvariance" -1;
	setAttr ".shadowthreshold" 0.0099999997764825821;
	setAttr ".remapBreakPoint" 0;
	setAttr ".remapMaxValue" 0;
	setAttr ".remapSmoothness" 0;
	setAttr ".name" -type "string" "diffuse";
createNode rmanDisplayChannel -n "a";
	rename -uid "033E1C80-0000-2627-61E6-821D00000290";
	setAttr ".cch" no;
	setAttr ".fzn" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".enable" yes;
	setAttr ".channelType" -type "string" "float";
	setAttr ".channelSource" -type "string" "a";
	setAttr ".lpeLightGroup" -type "string" "";
	setAttr ".filter" -type "string" "inherit from display";
	setAttr ".filterwidth" -type "float2" -1 -1 ;
	setAttr ".statistics" -type "string" "";
	setAttr ".relativepixelvariance" -1;
	setAttr ".shadowthreshold" 0.0099999997764825821;
	setAttr ".remapBreakPoint" 0;
	setAttr ".remapMaxValue" 0;
	setAttr ".remapSmoothness" 0;
	setAttr ".name" -type "string" "a";
createNode PxrPathTracer -s -n "bake_PxrPathTracer";
	rename -uid "5B233C80-0000-2168-61E1-82C50000033F";
	setAttr ".cch" no;
	setAttr ".fzn" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".maxIndirectBounces" 8;
	setAttr ".maxContinuationLength" -1;
	setAttr ".maxNonStochasticOpacityEvents" 0;
	setAttr ".sampleMode" -type "string" "bxdf";
	setAttr ".numLightSamples" 1;
	setAttr ".numBxdfSamples" 1;
	setAttr ".numIndirectSamples" 1;
	setAttr ".numDiffuseSamples" 1;
	setAttr ".numSpecularSamples" 1;
	setAttr ".numSubsurfaceSamples" 1;
	setAttr ".numRefractionSamples" 1;
	setAttr ".allowCaustics" no;
	setAttr ".accumOpacity" no;
	setAttr ".rouletteDepth" 4;
	setAttr ".rouletteThreshold" 0.20000000298023224;
	setAttr ".clampDepth" 2;
	setAttr ".clampLuminance" 10;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "3B4BCC80-0000-2A9C-61E6-D064000003CB";
	setAttr -s 5 ".lnk";
	setAttr -s 5 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "3B4BCC80-0000-2A9C-61E6-D064000003CC";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "3B4BCC80-0000-2A9C-61E6-D064000003CD";
createNode displayLayerManager -n "layerManager";
	rename -uid "3B4BCC80-0000-2A9C-61E6-D064000003CE";
createNode displayLayer -n "defaultLayer";
	rename -uid "F5BAF900-0000-E0F6-5A85-7F5700001D53";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "3B4BCC80-0000-2A9C-61E6-D064000003D0";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "F5BAF900-0000-E0F6-5A85-7F5700001D55";
	setAttr ".g" yes;
createNode partition -n "mtorPartition";
	rename -uid "F5BAF900-0000-E0F6-5A85-80D800001DBC";
	addAttr -s false -ci true -sn "rgcnx" -ln "rgcnx" -at "message";
	addAttr -ci true -sn "sd" -ln "slimData" -dt "string";
	addAttr -ci true -sn "sr" -ln "slimRIB" -dt "string";
	addAttr -ci true -sn "rd" -ln "rlfData" -dt "string";
	setAttr ".sr" -type "string" "";
createNode script -n "uiConfigurationScriptNode";
	rename -uid "F5BAF900-0000-E0F6-5A85-80D800001DBD";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n"
		+ "            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n"
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n"
		+ "            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 1\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n"
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 927\n            -height 674\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n"
		+ "            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n"
		+ "            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n"
		+ "            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n"
		+ "            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n"
		+ "                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n"
		+ "                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showPlayRangeShades \"on\" \n                -lockPlayRangeShades \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n"
		+ "                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -valueLinesToggle 0\n                -outliner \"graphEditor1OutlineEd\" \n                -highlightAffectedCurves 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n"
		+ "                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n"
		+ "                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n"
		+ "                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n"
		+ "            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n"
		+ "                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n"
		+ "                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n"
		+ "                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\n{ string $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n"
		+ "                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n"
		+ "                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n"
		+ "                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName; };\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n"
		+ "        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 927\\n    -height 674\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 1\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 927\\n    -height 674\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "F5BAF900-0000-E0F6-5A85-80D800001DBE";
	setAttr ".b" -type "string" "playbackOptions -min 0 -max 50 -ast 0 -aet 50 ";
	setAttr ".st" 6;
createNode aiStandard -n "aiStandard1";
	rename -uid "F5BAF900-0000-E0F6-5A85-821100001DF2";
createNode shadingEngine -n "aiStandard1SG";
	rename -uid "F5BAF900-0000-E0F6-5A85-821100001DF3";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo1";
	rename -uid "F5BAF900-0000-E0F6-5A85-821100001DF4";
createNode aiOptions -s -n "defaultArnoldRenderOptions";
	rename -uid "F5BAF900-0000-E0F6-5A85-821100001DF5";
	setAttr ".version" -type "string" "1.4.2.0";
createNode aiAOVFilter -s -n "defaultArnoldFilter";
	rename -uid "F5BAF900-0000-E0F6-5A85-821100001DF6";
	setAttr ".ai_translator" -type "string" "gaussian";
createNode aiAOVDriver -s -n "defaultArnoldDriver";
	rename -uid "F5BAF900-0000-E0F6-5A85-821100001DF7";
	setAttr ".ai_translator" -type "string" "tif";
createNode aiAOVDriver -s -n "defaultArnoldDisplayDriver";
	rename -uid "F5BAF900-0000-E0F6-5A85-821100001DF8";
	setAttr ".output_mode" 0;
	setAttr ".ai_translator" -type "string" "maya";
createNode file -n "file1";
	rename -uid "F5BAF900-0000-E0F6-5A85-821900001DF9";
	setAttr ".ftn" -type "string" "/home/cglynos/Desktop/MayaExamples/Arnold Project//sourceimages/cat.jpg";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "place2dTexture1";
	rename -uid "F5BAF900-0000-E0F6-5A85-821900001DFA";
createNode polyAutoProj -n "polyAutoProj1";
	rename -uid "F5BAF900-0000-E0F6-5A85-826300001E07";
	setAttr ".uopa" yes;
	setAttr ".ics" -type "componentList" 1 "f[0:4]";
	setAttr ".ix" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 0 0 0 1;
	setAttr ".s" -type "double3" 10 10 10 ;
	setAttr ".ps" 0.20000000298023224;
	setAttr ".dl" yes;
createNode polyTweakUV -n "polyTweakUV1";
	rename -uid "F5BAF900-0000-E0F6-5A85-828600001E2E";
	setAttr ".uopa" yes;
	setAttr -s 18 ".uvtk[0:17]" -type "float2" -0.0019920666 -0.45527625
		 0.99800801 -0.0018217874 0.63524443 0.99817818 -0.36475563 0.54472375 -0.27248791
		 0.69817817 -0.56519097 0.57145095 -0.17248787 0.24472371 -0.50530487 -0.2127223 -0.50530487
		 0.34073231 -0.79800802 0.11400501 -0.23640332 -0.85197067 0.76358283 -0.45926738
		 0.40081996 0.54073155 -0.59915823 0.14802837 0.99645591 -0.45926777 0.76972938 0.5407322
		 -0.23025998 0.17796786 -0.0035346027 -0.82203102;
createNode aiStandard -n "aiStandard2";
	rename -uid "F5BAF900-0000-E0F6-5A85-83A000001EAA";
createNode shadingEngine -n "aiStandard2SG";
	rename -uid "F5BAF900-0000-E0F6-5A85-83A000001EAB";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "F5BAF900-0000-E0F6-5A85-83A000001EAC";
createNode file -n "file2";
	rename -uid "F5BAF900-0000-E0F6-5A85-83A700001EAF";
	setAttr ".ftn" -type "string" "/home/cglynos/Desktop/MayaExamples/Arnold Project//sourceimages/guitar.jpg";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "place2dTexture2";
	rename -uid "F5BAF900-0000-E0F6-5A85-83A700001EB0";
createNode polyPlane -n "polyPlane1";
	rename -uid "F5BAF900-0000-E0F6-5A85-844E00001ECC";
	setAttr ".cuv" 2;
createNode blinn -n "blinn1";
	rename -uid "F5BAF900-0000-E0F6-5A85-848A00001EDD";
	setAttr ".dc" 0;
	setAttr ".c" -type "float3" 1 1 1 ;
	setAttr ".sc" -type "float3" 0.14935064 0.14935064 0.14935064 ;
	setAttr ".rfl" 20;
	setAttr ".rc" -type "float3" 0.058441557 0.058441557 0.058441557 ;
	setAttr ".ec" 0.20000000298023224;
	setAttr ".sro" 1;
createNode shadingEngine -n "blinn1SG";
	rename -uid "F5BAF900-0000-E0F6-5A85-848A00001EDE";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo3";
	rename -uid "F5BAF900-0000-E0F6-5A85-848A00001EDF";
createNode aiPhysicalSky -n "aiPhysicalSky1";
	rename -uid "F5BAF900-0000-E0F6-5A85-857D00001F13";
createNode rmanDisplay -n "rmanDefaultBakeDisplay1";
	rename -uid "5B233C80-0000-2168-61E1-82C50000033C";
	setAttr ".cch" no;
	setAttr ".fzn" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".enable" yes;
	setAttr ".denoise" no;
	setAttr ".frameMode" 0;
	setAttr ".remapBreakPoint" 0;
	setAttr ".remapMaxValue" 0;
	setAttr ".remapSmoothness" 0;
	setAttr ".name" -type "string" "";
createNode rmanDisplayChannel -n "diffuse1";
	rename -uid "5B233C80-0000-2168-61E1-82C50000033D";
	setAttr ".cch" no;
	setAttr ".fzn" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".enable" yes;
	setAttr ".channelType" -type "string" "color";
	setAttr ".channelSource" -type "string" "lpe:C(D[DS]*[LO])|[LO]";
	setAttr ".lpeLightGroup" -type "string" "";
	setAttr ".filter" -type "string" "inherit from display";
	setAttr ".filterwidth" -type "float2" -1 -1 ;
	setAttr ".statistics" -type "string" "";
	setAttr ".relativepixelvariance" -1;
	setAttr ".shadowthreshold" 0.0099999997764825821;
	setAttr ".remapBreakPoint" 0;
	setAttr ".remapMaxValue" 0;
	setAttr ".remapSmoothness" 0;
	setAttr ".name" -type "string" "diffuse";
createNode rmanDisplayChannel -n "a1";
	rename -uid "5B233C80-0000-2168-61E1-82C50000033E";
	setAttr ".cch" no;
	setAttr ".fzn" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".enable" yes;
	setAttr ".channelType" -type "string" "float";
	setAttr ".channelSource" -type "string" "a";
	setAttr ".lpeLightGroup" -type "string" "";
	setAttr ".filter" -type "string" "inherit from display";
	setAttr ".filterwidth" -type "float2" -1 -1 ;
	setAttr ".statistics" -type "string" "";
	setAttr ".relativepixelvariance" -1;
	setAttr ".shadowthreshold" 0.0099999997764825821;
	setAttr ".remapBreakPoint" 0;
	setAttr ".remapMaxValue" 0;
	setAttr ".remapSmoothness" 0;
	setAttr ".name" -type "string" "a";
createNode d_openexr -n "d_openexr";
	rename -uid "5B233C80-0000-2168-61E1-82C500000340";
	setAttr ".cch" no;
	setAttr ".fzn" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".asrgba" yes;
	setAttr ".autocrop" -type "string" "false";
	setAttr ".storage" -type "string" "scanline";
	setAttr ".exrpixeltype" -type "string" "half";
	setAttr ".compression" -type "string" "zips";
	setAttr ".compressionlevel" 45;
	setAttr ".forcepar" 0;
	setAttr ".metadatacount" 0;
createNode d_openexr -n "d_openexr1";
	rename -uid "033E1C80-0000-2627-61E6-821E000002CC";
	setAttr ".cch" no;
	setAttr ".fzn" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".asrgba" yes;
	setAttr ".autocrop" -type "string" "false";
	setAttr ".storage" -type "string" "scanline";
	setAttr ".exrpixeltype" -type "string" "half";
	setAttr ".compression" -type "string" "zips";
	setAttr ".compressionlevel" 45;
	setAttr ".forcepar" 0;
	setAttr ".metadatacount" 0;
createNode VRaySettingsNode -s -n "vraySettings";
	rename -uid "3B4BCC80-0000-2A9C-61E6-D064000003EF";
	setAttr ".gi" yes;
	setAttr ".rfc" yes;
	setAttr ".pe" 2;
	setAttr ".se" 3;
	setAttr ".cmph" 60;
	setAttr ".cfile" -type "string" "";
	setAttr ".cfile2" -type "string" "";
	setAttr ".casf" -type "string" "";
	setAttr ".casf2" -type "string" "";
	setAttr ".st" 3;
	setAttr ".msr" 6;
	setAttr ".aaft" 3;
	setAttr ".aafs" 2;
	setAttr ".dma" 24;
	setAttr ".dam" 1;
	setAttr ".pt" 0.0099999997764825821;
	setAttr ".pmt" 0;
	setAttr ".sd" 1000;
	setAttr ".ss" 0.01;
	setAttr ".pfts" 20;
	setAttr ".ufg" yes;
	setAttr ".fnm" -type "string" "";
	setAttr ".lcfnm" -type "string" "";
	setAttr ".asf" -type "string" "";
	setAttr ".lcasf" -type "string" "";
	setAttr ".urtrshd" yes;
	setAttr ".rtrshd" 2;
	setAttr ".lightCacheType" 1;
	setAttr ".ifile" -type "string" "";
	setAttr ".ifile2" -type "string" "";
	setAttr ".iasf" -type "string" "";
	setAttr ".iasf2" -type "string" "";
	setAttr ".pmfile" -type "string" "";
	setAttr ".pmfile2" -type "string" "";
	setAttr ".pmasf" -type "string" "";
	setAttr ".pmasf2" -type "string" "";
	setAttr ".dmcstd" yes;
	setAttr ".dmculs" no;
	setAttr ".dmcsat" 0.004999999888241291;
	setAttr ".cmtp" 6;
	setAttr ".cmao" 2;
	setAttr ".cg" 2.2000000476837158;
	setAttr ".mtah" yes;
	setAttr ".rgbcs" -1;
	setAttr ".suv" 0;
	setAttr ".srflc" 1;
	setAttr ".srdml" 0;
	setAttr ".seu" yes;
	setAttr ".gormio" yes;
	setAttr ".gocle" yes;
	setAttr ".gopl" 2;
	setAttr ".wi" 960;
	setAttr ".he" 540;
	setAttr ".aspr" 1.7777780294418335;
	setAttr ".productionGPUResizeTextures" 0;
	setAttr ".autolt" 0;
	setAttr ".jpegq" 100;
	setAttr ".animtp" 1;
	setAttr ".vfbOn" yes;
	setAttr ".vfbSA" -type "Int32Array" 847 124 20 0 0 0 0
		 0 0 0 0 -1073724351 0 0 0 0 0 0 0
		 0 0 0 -1074790400 0 -1074790400 0 -1074790400 0 -1074790400 1 0
		 0 0 3253 1 3241 0 1 3233 1700143739 1869181810 825893486 1632379436
		 1936876921 578501154 1936876886 577662825 573321530 1935764579 574235251 1953460082 1881287714 1701867378 1701409906 2067407475
		 1919252002 1852795251 741423650 1835101730 574235237 1696738338 1818386798 1949966949 744846706 1886938402 577007201 1818322490
		 573334899 1634760805 1650549870 975332716 1702195828 1931619453 1814913653 1919252833 1530536563 1818436219 577991521 1751327290
		 779317089 1886611812 1132028268 1701999215 1869182051 573317742 1886351984 1769239141 975336293 1702240891 1869181810 825893486
		 1634607660 975332717 1936278562 2036427888 1919894304 1952671090 577662825 1852121644 1701601889 1920219682 573334901 1634760805
		 975332462 1702195828 2019893804 1684955504 1701601889 1920219682 573334901 1718579824 577072233 573321530 1869641829 1701999987
		 774912546 1763847216 1717527395 577072233 740434490 1667459362 1852142175 1953392996 578055781 573321274 1886088290 1852793716
		 1715085942 1702063201 1668227628 1717530473 577072233 740434490 1768124194 1868783471 1936879468 1701011824 741358114 1768124194
		 1768185711 1634496627 1986356345 577069929 573321274 1869177711 1701410399 1634890871 1868985198 975334770 1864510512 1601136995
		 1702257011 1835626089 577070945 1818322490 746415475 1651864354 2036427821 577991269 578509626 1935764579 574235251 1868654691
		 1701981811 1869819494 1701016181 1684828006 740455013 1869770786 1953654128 577987945 1981971258 1769173605 975335023 1847733297
		 577072481 1867719226 1701016181 1196564538 573317698 1650552421 975332716 1702195828 2019893804 1684955504 1634089506 744846188
		 1886938402 1633971809 577072226 1818322490 573334899 1667330159 578385001 808333626 1818370604 1600417381 1701080941 741358114
		 1668444962 1887007839 809116261 1931619453 1814913653 1919252833 1530536563 1818436219 577991521 1751327290 779317089 778462578
		 1751607660 2020175220 1881287714 1701867378 1701409906 2067407475 1919252002 1852795251 741423650 1835101730 574235237 1751607628
		 2020167028 1696738338 1818386798 1715085925 1702063201 2019893804 1684955504 1634089506 744846188 1886938402 1633971809 577072226
		 1970435130 573341029 761427315 1702453612 975336306 746413403 1818436219 577991521 1751327290 779317089 778462578 1886220131
		 1953067887 573317733 1886351984 1769239141 975336293 1702240891 1869181810 825893486 1634607660 975332717 1836008226 1769172848
		 740451700 1634624802 577072226 1818322490 573334899 1634760805 975332462 1936482662 1696738405 1851879544 1818386788 1949966949
		 744846706 1634758434 2037672291 774978082 1646406704 1684956524 1685024095 809116261 1931619453 1814913653 1919252833 1530536563
		 2103278941 1663204140 1936941420 1663187490 1936679272 778399790 1869505892 1919251305 1881287714 1701867378 1701409906 2067407475
		 1919252002 1852795251 741423650 1835101730 574235237 1869505860 1919251305 1853169722 1767994977 1818386796 573317733 1650552421
		 975332716 1936482662 1696738405 1851879544 1715085924 1702063201 2019893804 1684955504 1701601889 1920219682 573334901 1667330159
		 578385001 808333626 1818370604 1600417381 1701080941 741358114 1952669986 577074793 1818322490 573334899 1936028272 975336549
		 1931619378 1852142196 577270887 808333626 1634869804 1937074532 808532514 573321262 1665234792 1701602659 1702125938 1920219682
		 573334901 1869505892 1919251305 1685024095 825893477 1931619453 1814913653 1919252833 1530536563 2066513245 1634493218 975336307
		 1634231074 1882092399 1701588581 2019980142 1881287714 1701867378 1701409906 2067407475 1919252002 1852795251 741423650 1835101730
		 574235237 1936614732 1717978400 1937007461 1696738338 1818386798 1949966949 744846706 1886938402 577007201 1818322490 573334899
		 1634760805 1650549870 975332716 1702195828 1886331436 1953063777 825893497 573321262 1852140642 1869438820 975332708 1730292786
		 1701994860 577662815 1818322490 573334899 1918987367 1769168741 975332730 808333363 1818698284 1600483937 1734960503 975336552
		 741355057 1869373986 2002742639 1751607653 809116276 808465454 808464432 909718832 1818698284 1600483937 1701996660 1819240563
		 825893476 573321262 1953261926 1918857829 1952543855 577662825 808333370 1634935340 1634891124 1852795252 774978082 1747070000
		 2003071585 1600483937 1701012321 1634887020 577004916 1970435130 1663183973 1600416879 1836212599 1634089506 744846188 1953392930
		 1667330661 1702259060 1920219682 573334901 1650552421 1650419052 1701077356 1949966963 744846706 1684632354 975336293 1646406710
		 1701077356 1869766515 1769234804 975335023 808334641 1953702444 1801545074 1970037343 809116274 808464942 808464432 943272496
		 1937056300 1919377253 1852404833 1715085927 1702063201 1919361580 1852404833 1701076839 1953067886 893002361 741355056 1634887458
		 1735289204 1852140639 577270887 774910266 1730292784 1769234802 2053072750 577597295 808334650 1919361580 1852404833 1819500391
		 577073263 808333370 1919361580 1852404833 1953718119 1735288178 975333492 741355057 1702065442 1667460959 1769174380 975335023
		 1936482662 1864510565 1970037603 1852795251 1836675935 1920230765 975332201 1702195828 1668227628 1937075299 1601073001 1668441456
		 578055781 774910522 1864510512 1970037603 1852795251 1953460831 1869182049 809116270 573321262 1818452847 1869181813 1918984046
		 825893475 808333360 1937056300 1668505445 1668571506 1715085928 1702063201 1668489772 2037604210 1952804205 576940402 1970435130
		 1931619429 1885303395 1702130785 975335026 1931619376 1834971747 1769237621 1918987367 1868783461 578055797 573321530 1601332083
		 1936614756 578385001 774911290 1931619376 1818194531 1952935525 893002344 741355056 1919120162 1869378399 1985963376 1634300513
		 577069934 808333370 1668489772 1769430898 1600681060 1769103734 1701015137 774912546 1931619376 1935635043 577004901 573321274
		 1601332083 1836019578 775043618 1931619376 1918857827 1952543855 577662825 808333370 1668489772 1953718130 1735288178 975333492
		 741355057 1702065442 1937073247 1715085940 1702063201 1969496620 1885303923 1702130785 975335026 1679961136 1601467253 1936614756
		 578385001 774911290 1679961136 1601467253 1768186226 1985966965 1634300513 577069934 808333370 1969496620 1784640627 1702130793
		 809116274 573321262 1953723748 1869576799 842670701 573321262 1953723748 1953460831 1869182049 809116270 573321262 1953723748
		 1920234335 1952935525 825893480 573321262 1918987367 1937071973 1651466085 1667331187 1767859564 1701273965 1634089506 744846188
		 1634494242 1868522866 1635021666 1600482403 1734438249 1634754405 975333492 573317666 1953718895 1634560351 2053072231 577597295
		 808333626 1651450412 1767863411 1701273965 1953460831 1869182049 809116270 573321262 1953718895 1634560351 1935631719 1852142196
		 577270887 808333626 1937056300 1768316773 1919251564 1634560351 975332711 1936482662 1730292837 1701994860 1634560351 1885300071
		 577270881 2099388986 1970479660 1634479458 1936876921 1566259746 1568497021 1377971325 1869178725 1852131182 578501154 1936876918
		 577662825 573321530 1937076077 1868980069 2003790956 1634624863 1684368482 1634089506 744846188 1970236706 1717527923 1869376623
		 1869635447 1601465961 1801678700 975332453 1936482662 1830956133 1702065519 1819240031 1601662828 1852403568 578314100 573321274
		 1937076077 1868980069 2003790956 1768910943 2036298862 2100312610 1699881516 1919247470 2003134806 578501154 1936876918 577662825
		 573321530 1650552421 1918854508 1701080677 1701994354 1852795239 1634089506 744846188 1852142114 1601332580 1768383858 2019520111
		 758784560 741355057 1852142114 1601332580 1768383858 2036297327 758784560 741355057 1852142114 1601332580 1768383858 2019520111
		 758784561 741355057 1852142114 1601332580 1768383858 2036297327 758784561 741355057 1701410338 1701994359 1949966948 744846706
		 1701410338 1919377271 577660261 1970435130 1981951077 1601660265 1702194274 1920219682 573334901 2003134838 1852796255 1715085935
		 1702063201 1868767788 1601335148 1835101283 1869438832 975332708 573323574 1869377379 1818451826 1601203553 975335023 1702195828
		 1768956460 1600939384 1868983913 1668246623 577004907 1818322490 573334899 1702390128 1852399468 1667198822 1701999215 1684370531
		 1819239263 577991279 1818322490 746415475 1952661794 1936617321 578501154 1936876918 577662825 573321530 1937072496 1380993381
		 1701339999 1684368227 1634089506 744846188 1702065442 1702390096 1886601580 1601463141 1667590243 577004907 1818322490 573334899
		 1953719668 1601398098 1768186226 893002351 1948396593 1383363429 1667199845 1801676136 975332453 1936482662 1679961189 1735746149
		 1684105299 1600613993 1768186226 893002351 1679961142 1735746149 1684105299 1600613993 1667590243 577004907 1818322490 573334899
		 1919251571 1867345765 1918854500 1869177953 943143458 1953702444 1868919397 1701080909 1701339999 1684368227 1634089506 2103800684
		 125 ;
	setAttr ".mSceneName" -type "string" "/home/cglynos/Desktop/MayaExamples/Arnold Project/scenes with spaces/cloth_sim_arnold.ma";
	setAttr ".rt_cpuRayBundleSize" 4;
	setAttr ".rt_gpuRayBundleSize" 128;
	setAttr ".rt_maxPaths" 10000;
	setAttr ".rt_engineType" 3;
	setAttr ".rt_gpuResizeTextures" 0;
select -ne :time1;
	setAttr ".o" 0;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".etmr" no;
	setAttr ".tmr" 4096;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 5 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 8 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 2 ".u";
select -ne :defaultRenderingList1;
	setAttr -s 7 ".r";
select -ne :lightList1;
select -ne :defaultTextureList1;
	setAttr -s 2 ".tx";
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr ".ren" -type "string" "arnold";
	setAttr ".outf" 51;
	setAttr ".imfkey" -type "string" "tif";
	setAttr ".an" yes;
	setAttr ".fs" 0;
	setAttr ".ef" 50;
	setAttr ".pff" yes;
	setAttr ".ifp" -type "string" "cloth_sim";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :defaultLightSet;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "nClothShape1.omsh" "outputCloth1.i";
connectAttr "polyTweakUV1.out" "pPrismShape1.i";
connectAttr "polyTweakUV1.uvtk[0]" "pPrismShape1.uvst[0].uvtw";
connectAttr ":time1.o" "nucleus1.cti";
connectAttr "nClothShape1.cust" "nucleus1.niao[0]";
connectAttr "nClothShape1.stst" "nucleus1.nias[0]";
connectAttr "nRigidShape1.cust" "nucleus1.nipo[0]";
connectAttr "nRigidShape1.stst" "nucleus1.nips[0]";
connectAttr "nucleus1.stf" "nClothShape1.stf";
connectAttr ":time1.o" "nClothShape1.cti";
connectAttr "pPlaneShape1.w" "nClothShape1.imsh";
connectAttr "nucleus1.noao[0]" "nClothShape1.nxst";
connectAttr "nucleus1.stf" "nRigidShape1.stf";
connectAttr ":time1.o" "nRigidShape1.cti";
connectAttr "pPrismShape1.w" "nRigidShape1.imsh";
connectAttr "polyPlane1.out" "pPlaneShape2.i";
connectAttr ":PxrPathTracer.msg" ":rmanGlobals.ri_integrator";
connectAttr "rmanDefaultBakeDisplay.msg" ":rmanBakingGlobals.displays[0]";
connectAttr ":bake_PxrPathTracer.msg" ":rmanBakingGlobals.ri_integrator";
connectAttr "diffuse.msg" "rmanDefaultBakeDisplay.displayChannels[0]";
connectAttr "a.msg" "rmanDefaultBakeDisplay.displayChannels[1]";
connectAttr "d_openexr.msg" "rmanDefaultBakeDisplay.displayType";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "aiStandard1SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "aiStandard2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn1SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "aiStandard1SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "aiStandard2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn1SG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr ":defaultRenderGlobals.msg" "mtorPartition.rgcnx";
connectAttr "file1.oc" "aiStandard1.Kd_color";
connectAttr "aiStandard1.out" "aiStandard1SG.ss";
connectAttr "pPrismShape1.iog" "aiStandard1SG.dsm" -na;
connectAttr "aiStandard1SG.msg" "materialInfo1.sg";
connectAttr "aiStandard1.msg" "materialInfo1.m";
connectAttr "file1.msg" "materialInfo1.t" -na;
connectAttr ":defaultArnoldDisplayDriver.msg" ":defaultArnoldRenderOptions.drivers"
		 -na;
connectAttr ":defaultArnoldFilter.msg" ":defaultArnoldRenderOptions.filt";
connectAttr ":defaultArnoldDriver.msg" ":defaultArnoldRenderOptions.drvr";
connectAttr ":defaultColorMgtGlobals.cme" "file1.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "file1.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "file1.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "file1.ws";
connectAttr "place2dTexture1.c" "file1.c";
connectAttr "place2dTexture1.tf" "file1.tf";
connectAttr "place2dTexture1.rf" "file1.rf";
connectAttr "place2dTexture1.mu" "file1.mu";
connectAttr "place2dTexture1.mv" "file1.mv";
connectAttr "place2dTexture1.s" "file1.s";
connectAttr "place2dTexture1.wu" "file1.wu";
connectAttr "place2dTexture1.wv" "file1.wv";
connectAttr "place2dTexture1.re" "file1.re";
connectAttr "place2dTexture1.of" "file1.of";
connectAttr "place2dTexture1.r" "file1.ro";
connectAttr "place2dTexture1.n" "file1.n";
connectAttr "place2dTexture1.vt1" "file1.vt1";
connectAttr "place2dTexture1.vt2" "file1.vt2";
connectAttr "place2dTexture1.vt3" "file1.vt3";
connectAttr "place2dTexture1.vc1" "file1.vc1";
connectAttr "place2dTexture1.o" "file1.uv";
connectAttr "place2dTexture1.ofs" "file1.fs";
connectAttr "polySurfaceShape1.o" "polyAutoProj1.ip";
connectAttr "pPrismShape1.wm" "polyAutoProj1.mp";
connectAttr "polyAutoProj1.out" "polyTweakUV1.ip";
connectAttr "file2.oc" "aiStandard2.Kd_color";
connectAttr "aiStandard2.out" "aiStandard2SG.ss";
connectAttr "outputCloth1.iog" "aiStandard2SG.dsm" -na;
connectAttr "aiStandard2SG.msg" "materialInfo2.sg";
connectAttr "aiStandard2.msg" "materialInfo2.m";
connectAttr "file2.msg" "materialInfo2.t" -na;
connectAttr ":defaultColorMgtGlobals.cme" "file2.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "file2.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "file2.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "file2.ws";
connectAttr "place2dTexture2.c" "file2.c";
connectAttr "place2dTexture2.tf" "file2.tf";
connectAttr "place2dTexture2.rf" "file2.rf";
connectAttr "place2dTexture2.mu" "file2.mu";
connectAttr "place2dTexture2.mv" "file2.mv";
connectAttr "place2dTexture2.s" "file2.s";
connectAttr "place2dTexture2.wu" "file2.wu";
connectAttr "place2dTexture2.wv" "file2.wv";
connectAttr "place2dTexture2.re" "file2.re";
connectAttr "place2dTexture2.of" "file2.of";
connectAttr "place2dTexture2.r" "file2.ro";
connectAttr "place2dTexture2.n" "file2.n";
connectAttr "place2dTexture2.vt1" "file2.vt1";
connectAttr "place2dTexture2.vt2" "file2.vt2";
connectAttr "place2dTexture2.vt3" "file2.vt3";
connectAttr "place2dTexture2.vc1" "file2.vc1";
connectAttr "place2dTexture2.o" "file2.uv";
connectAttr "place2dTexture2.ofs" "file2.fs";
connectAttr "blinn1.oc" "blinn1SG.ss";
connectAttr "pPlaneShape2.iog" "blinn1SG.dsm" -na;
connectAttr "blinn1SG.msg" "materialInfo3.sg";
connectAttr "blinn1.msg" "materialInfo3.m";
connectAttr "d_openexr1.msg" "rmanDefaultBakeDisplay1.displayType";
connectAttr "aiStandard1SG.pa" ":renderPartition.st" -na;
connectAttr "aiStandard2SG.pa" ":renderPartition.st" -na;
connectAttr "blinn1SG.pa" ":renderPartition.st" -na;
connectAttr "aiStandard1.msg" ":defaultShaderList1.s" -na;
connectAttr "aiStandard2.msg" ":defaultShaderList1.s" -na;
connectAttr "blinn1.msg" ":defaultShaderList1.s" -na;
connectAttr "place2dTexture1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "place2dTexture2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr ":rmanGlobals.msg" ":defaultRenderingList1.r" -na;
connectAttr ":PxrPathTracer.msg" ":defaultRenderingList1.r" -na;
connectAttr ":rmanBakingGlobals.msg" ":defaultRenderingList1.r" -na;
connectAttr ":bake_PxrPathTracer.msg" ":defaultRenderingList1.r" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "d_openexr.msg" ":defaultRenderingList1.r" -na;
connectAttr "d_openexr1.msg" ":defaultRenderingList1.r" -na;
connectAttr "aiSkyDomeLightShape1.ltd" ":lightList1.l" -na;
connectAttr "file1.msg" ":defaultTextureList1.tx" -na;
connectAttr "file2.msg" ":defaultTextureList1.tx" -na;
connectAttr "pPlaneShape1.iog" ":initialShadingGroup.dsm" -na;
connectAttr "aiSkyDomeLight1.iog" ":defaultLightSet.dsm" -na;
// End of cloth_sim_arnold.ma
