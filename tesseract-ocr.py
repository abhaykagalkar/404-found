#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 11:43:18 2018

@author: abhay
"""

import argparse
import sys
import os
import cv2
import shutil
def tesseractRun(infile, outfile):
        
     if infile != False:
        try :
           #print(infile)
           os.system("tesseract "+infile+" "+outfile)
           ocr_out=outfile+".txt"
           
           if(os.stat(ocr_out).st_size <35):
               os.remove(ocr_out)
           else:
               print(os.stat(ocr_out).st_size)
               shutil.move(infile,outfile)
        except IOError:
            print "Cannot find text for : ", infile


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
    arr=[]    
    i=0
    inputDir,outputDir= check_arg(sys.argv[1:])
    #inputDir="/home/abhay/Documents/OCR/testdata/"
  #  outputDir="/home/abhay/Documents/Rejectedimages"
    print("Input Directory : ",inputDir)
    print("Output Directory: ",outputDir)    
    if not os.path.exists(outputDir):
            os.mkdir(outputDir,0755)        
    for file in os.listdir(inputDir):
        arr.append(file)
        i+=1
        outfile=outputDir+"/"+str(i)
        file= inputDir+"/"+file
        print(str(i)+":"+file)
        tesseractRun(file,outfile)
