# Renderfarm Update

This document contains the basic workplan and estimated time span for the renderfarm upgrade project. 


## Outline 

A present the current farm doesn't work due to upgrades with different DCC tools and the change of python versions from 2.7 to 3.9 in the DCC tools. 

As Qube is primarily written in Python this is a problem as our current tools and systems are incompatible with each other, there are also problems with the current install which crashes the Qube GUI when running (there is a job logged with pfx who are investigating the crash).

Across our courses we use Maya and Houdini as the core DCC tools, Houdini mainly used by the MADE students and Maya with the other courses. 

These tools use renderers with Houdini mainly using Mantra and moving to Solaris / Karma.

Maya uses V-Ray, Arnold and Renderman in that order. This means we need to support 2 tools and 5 core renderers each of which use different file formats and pipelines to generate the scenes. 

Whilst is is possible to automate some of these processes in Maya at present this is not working as the versions of Maya in the lab and farm are out of synch, and the pipeline for this process will need to be developed and tested.

Ideally we would like a one button solution to allow the export of the scenes for render to the farm, submission of jobs for render and reporting of jobs completed. This is a complex process requiring the integration of many tools and parts. The old system semi-automated this process. This is further  complicated by the fact that this is relatively simple under Linux as we have control over the build and infrastructure but massively complex under windows due to the nature of the windows install (Apps Anywhere / Security)



- SWOT
- Issues with Qube on present system
- Need scene files (passing and failing)
- develop tools 
  - command line (simple)
  - GUI harder 
  - Integrated (best)
- Tests need to be written for code
- Documentation
- Videos 


## Plan and Timeline

1. Initial problem analysis and design (Including proof of concept for cmd line tools) 40hrs
2. Development of Test scenes for V-Ray (most popular tool) 10hrs
3. Design, Development and Testsing of V-Ray command line python tool 40 hrs