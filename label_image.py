from PIL import Image
import torch
import torchvision.transforms as transforms
from torch.autograd import Variable
import numpy as np
import shutil
import os,sys
import argparse

transform = transforms.Compose([transforms.RandomCrop([128,128]),transforms.ToTensor()])

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

def load_image(fileName):
	img = Image.open(fileName)
	img = transform(img)
	img = Variable(img.view(-1,3*128*128)).double()
	return img

f = open('labels.txt','r')
labels=f.read()
labels=labels.strip().split(' ')
net = torch.load('model.pb')
inputDir,outputDir= check_arg(sys.argv[1:])
images = os.listdir(inputDir)
for img in images:
	image = load_image(os.path.join(inputDir,img))
	output = net(image)
	predictions=output.max(1)
	print img,' predicted label:',labels[int(predictions[0])]
	if labels[int(predictions[0])]=='1':
		print 'Discarded'
		shutil.move(os.path.join(inputDir,img),outputDir)
