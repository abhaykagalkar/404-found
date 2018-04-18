#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 11:43:18 2018

@author: abhay
"""
import dbConnect
import argparse
import sys
import os
import cv2
import shutil


def check_arg(args=None):
    homedir = os.environ['HOME']
    parser = argparse.ArgumentParser(description='Input Parameters to be passed')
    parser.add_argument('-i', '--input',
                        help='Test Input Directory',
                        required='True',
                        default=os.getcwd())
    parser.add_argument('-o', '--out',
                        help='Output of Our Algorithm',
                        default=homedir+"/Documents/RejectedImages")

    results = parser.parse_args(args)
    return (results.input,results.out)

if __name__ == '__main__':
    connection=dbConnect.Connect()
    if(connection):
	print ("Database Connection successful!!")
    else:   
    	sys.exit("ERROR IN CONNECTION")
    arr=[]    
    i=0
    inputDir,outputDir= check_arg(sys.argv[1:])
    print("Input Directory : ",inputDir)
    print("Output Directory: ",outputDir)    
    if not os.path.exists(outputDir):
            os.mkdir(outputDir,0755)        
    #os.system("bash "+os.getcwd()+"/preRun.sh")
    #os.system("python "+os.getcwd()+"/initial.py -i "+inputDir+" -o "+outputDir)
    #os.system("python "+os.getcwd()+"/tesseract-ocr.py -i "+inputDir+" -o "+outputDir)
    #os.system("python "+os.getcwd()+"/label_image.py -i "+inputDir+" -o "+outputDir)
