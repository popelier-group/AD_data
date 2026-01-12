import os
import shutil


XYZ = "alanine-langevin-displaced-0.25.xyz"
with open(XYZ,"r") as f:
    content = f.readlines()

items = list()
orig_folder = "orig"
for item in os.listdir(orig_folder):
    items.append(os.path.join(orig_folder,item))

ngeoms = int(len(content)/24)
for i in range(ngeoms):
    idx = i+1
    geom = content[i*24:(i+1)*24]
    newdir = "RUN"+str(idx)
    if not os.path.isdir(newdir):
        os.mkdir(newdir)
    newfilename = os.path.join(newdir,"ALANINE.xyz")
    with open(newfilename,"w") as f:
        for line in geom:
            f.write(line)

    for item in items:
        if os.path.isfile(item):
            shutil.copy2(item,newdir)
        else:
            shutil.copytree(item,os.path.join(newdir,os.path.split(item)[1]),dirs_exist_ok=True)

