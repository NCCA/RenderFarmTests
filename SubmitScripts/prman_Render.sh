#!/usr/bin/bash
export MAYA_RENDER_DESC_PATH=$MAYA_RENDER_DESC_PATH:/opt/pixar/RenderManForMaya-24.4/etc/
export  PIXAR_LICENSE_FILE=9010@talavera.bournemouth.ac.uk

Render -s 1 -e 120 -b 10 -rd /render/jmacey/output -r renderman -proj /render/jmacey/FarmTest -cam persp /render/jmacey/FarmTest/scenes/RenderManTest.ma 