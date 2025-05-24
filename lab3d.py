#!/usr/bin/env python3

#Purpose of the script is to create a Python function that can return
#the free disk space on a Linux system's root directory
# Author ID: 160682231

#using OS:
#import os

#def free_space():
#    os.system("df -h | grep '/$' | awk '{print $4}'")

#Using SUBPROCESS
import subprocess

def free_space():
    p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], 
                     stdout=subprocess.PIPE, stdin=subprocess.PIPE, 
                     stderr=subprocess.PIPE, shell=True)
    output = p.communicate()
    return(output[0].decode('utf-8').strip())




if __name__ == '__main__':
    print(free_space())



