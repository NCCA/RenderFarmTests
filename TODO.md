# TODO

This is a non exhaustive list of things to do and think about. Will most likely not make sense to anyone but Jon :-)

## NEXT!

Can render vray from script, the scene needs to be careful with paths so the next job is to figure out how to strip all of these in the submission


./vray_batch.py -s 1 -e 1 -sc /render/jmacey/FarmTest/scenes/VR2.vrscene --project_root=/home/jmacey/RenderFarmTests/MayaProjects/FarmTest/ --env "VRAY_ASSETS_PATH" "/render/jmacey/FarmTest/shaders:../" -i ../test_images/VR2.exr 


## Tests 

1. Renderman
2. Houdini (Mantra / Solaris)
3. Arnold

- Time / test per file submission (i.e. one file per frame) vs bulk / in file multi frame to figure best practice

- Test folder locations / maya scene setup

- Pre post submission scripts

- Hserver tests and shutdown.
