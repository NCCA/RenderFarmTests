#!/usr/bin/env python

import subprocess
import tempfile
import os
pn="Project Name"
od="/rop/mantra1"
fl="/render/jmacey/test.hip"
u="jmacey"

start_frame=1
end_frame=5
by_frame=2
range=f"{start_frame}-{end_frame}x{by_frame}"
payload=f"""
import os
import sys
sys.path.insert(0,"/public/devel/2022/pfx/qube/api/python/")

import qb
if os.environ.get("QB_SUPERVISOR") is None :
    os.environ["QB_SUPERVISOR"]="tete.bournemouth.ac.uk"
    os.environ["QB_DOMAIN"]="ncca"

project_name_text='{pn}'
output_drive_text='{od}'
farm_location_text='{fl}'
user='{u}'


job = {{}}
job['name'] = f"{{project_name_text}}"
job['prototype'] = 'cmdrange'
package = {{}}
package['shell']="/bin/bash"
pre_render="cd /opt/software/hfs19.5.303/; source houdini_setup_bash; "
render_command=f"hython $HB/hrender.py -e -F QB_FRAME_NUMBER -R -d {{output_drive_text}} {{farm_location_text}}"
package['cmdline']=f"{{pre_render}} {{render_command}}"
        
job['package'] = package
        
env={{"HOME" :f"/render/{{user}}",  
            "SESI_LMHOST" : "hamworthy.bournemouth.ac.uk",
            "PIXAR_LICENSE_FILE" : "9010@talavera.bournemouth.ac.uk",            
            }}
job['env']=env

agendaRange = f'{range}'  
agenda = qb.genframes(agendaRange)

job['agenda'] = agenda
        
listOfJobsToSubmit = []
listOfJobsToSubmit.append(job)
listOfSubmittedJobs = qb.submit(listOfJobsToSubmit)
id_list=[]
for job in listOfSubmittedJobs:
    print(job['id'])
    id_list.append(job['id'])

print(id_list)
"""

print(payload)


with tempfile.TemporaryDirectory() as tmpdirname:
    print(tmpdirname)
    with open(tmpdirname+"/payload.py","w") as fp :
        fp.write(payload)
    output=subprocess.run(["/usr/bin/python3",f"{tmpdirname}/payload.py"],capture_output=True)
    #os.system(f"ls {tmpdirname}")
    #os.system(f"/usr/bin/python3 {tmpdirname}/payload.py")
    print(output.stdout)
    


#with tempfile.TemporaryFile(mode="w+" ,encoding='utf-8') as fp:
#    fp.writelines(payload)
#    print(fp.name)
