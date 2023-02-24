#!/usr/bin/bash

export VRAY_AUTH_CLIENT_FILE_PATH=/opt


Render -s 1 -e 120 -b 10 -rd /render/jmacey/output -im VRBatch.exr -r vray -proj /render/jmacey/FarmTest -cam persp /render/jmacey/FarmTest/scenes/VRayTestUsingRender.ma 