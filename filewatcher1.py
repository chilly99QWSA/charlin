import os
import shutil
import time
while(True):
    key="v2eTechnologies"
    a="xyz"
    path_key=a+"/"
    if a=="xyz":
        move_location="./abc"
    else:
        move_location="null"
    b=os.path.abspath(a)
    for path,dirt,files in os.walk(b):
        continue
    for i in files:
        c=open(path_key+i)
        d=c.read()
        c.close()
        if move_location=="null":
            print("file can not be move")
            break
        elif key in d:
            shutil.move(path_key+i,move_location)
            print("files moved to:",move_location)
    time.sleep(10)