#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 11:43:18 2018

@author: abhay
"""

import argparse
import sys
import os
import shutil

def check_arg(args=None):
    homedir = os.environ['HOME']
    parser = argparse.ArgumentParser(description='Input Parameters to be passed')
    parser.add_argument('-i', '--input',
                        help='Test Input Directory',
                        required='True',
                        default=os.getcwd())
    parser.add_argument('-o', '--out',
                        help='Rejected images/files',
                        default=homedir+"/Documents/RejectedImages")

    results = parser.parse_args(args)
    return (results.input,results.out)

if __name__ == '__main__':
    arr=[]    
    i=0
    inputDir,outputDir= check_arg(sys.argv[1:])
    print("Input Directory : ",inputDir)
    print("Output Directory: ",outputDir)    
    if not os.path.exists(outputDir):
            os.mkdir(outputDir,0755)        
    for file in os.listdir(inputDir):
        arr.append(file)
        if(file.lower().endswith(('.png', '.jpg', '.jpeg')))==False:
            shutil.move(inputDir+"/"+file,outputDir)
            
            
        
        
        
        
        
        
        
        
        
        
        