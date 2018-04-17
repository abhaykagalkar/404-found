sudo apt update &&
sudo apt upgrade &&
conda install pytorch-cpu torchvision -c pytorch &&
conda install -c conda-forge opencv &&
conda install -c anaconda pillow &&
conda install -c anaconda pil &&
sudo apt install tesseract-ocr &&
sudo apt install libtesseract-dev &&
sudo git clone https://github.com/pjreddie/darknet &&
cd darknet &&
make &&
wget https://pjreddie.com/media/files/yolov3.weights
cd .. &&

