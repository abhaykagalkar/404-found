# Author : IPCVG TEAM - ABHAY ABHIJEET SUJAY VAISHNAVI
# Script follows here:

PROJ_NAME:"CROWDSOUCRING"
sudo apt update &&
sudo apt upgrade &&
echo "Do you want to install PyTorch - TorchVision [Y/N]"
read choice
if choice==Y || choice==y 
conda install pytorch-cpu torchvision -c pytorch &&
conda install -c conda-forge opencv &&
#conda install -c anaconda pillow &&
#conda install -c anaconda pil &&
#sudo apt install tesseract-ocr &&
#sudo apt install libtesseract-dev &&
echo "IPCVG TINDI"
echo "------------------------------------------------------------------------------------------
     +                  
            IPCVG - $PROJ_NAME                  +
     ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo *****CLONING DARKNET***
git clone https://github.com/abhaykagalkar/darknet-modified.git &&
cd darknet-modified &&
wget https://pjreddie.com/media/files/yolov3.weights &&
make &&
cd .. 
