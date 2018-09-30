import os
import re
import shutil

def mask_email(inputdir,inputfile):
    if inputdir == "\.":
        fqpath = os.path.join(os.getcwd() , inputfile)  
    else:
        fqpath=os.getcwd()+os.path.join(inputdir, inputfile)  
    print(fqpath)
    fqpathnew = fqpath+"."+"txt"
    print(fqpathnew)
    readfile = open(fqpath, mode='r')
    writfile = open(fqpathnew, mode='w')
    for line in readfile:
        print(line)
        maskline = re.sub('(.*)@','MASKED@',line)
        writfile.write(maskline)
    writfile.close()
    readfile.close()
    shutil.move(fqpathnew,fqpath)


for dirpath, dirs, files in os.walk("."):
    for file in files:
        thisfile = re.match( r'(.*)\.(html)', file, re.M|re.I)
        if thisfile:
            mask_email(dirpath,thisfile.group(0))



