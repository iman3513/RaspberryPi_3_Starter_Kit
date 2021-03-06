# [ENGLISH] Project 8: Image Processing
Commonly found microcontrollers can't handle any application that involves image processing as one of its features. That's because the available resources simply aren't enough. Usually, the last resort is to utilize a computer/laptop for that matter.

<img src="/images/roboLaptop.jpg" height="300">

As you can see, the appearance of the robot above is somewhat terrible and expensive at the same time. Now we can actually replace the laptop with Raspberry Pi 3, therefore the price for building one would be far cheaper and not to mention that the look would be somewhat better. In this project we will try to do some image processing stuffs on Raspberry Pi 3 with Python 3 and [OpenCV](https://opencv.org/).

## OpenCV Installation
Before we get started, we need to install OpenCV on our Raspberry Pi 3. The installation can be done by following the steps below:
* Type and run the commands below on your terminal:
```
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk2.0-dev libgtk-3-dev
sudo apt-get install libcanberra-gtk*
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python2.7-dev python3-dev
cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
unzip opencv_contrib.zip
cd ~/opencv-3.3.0/
mkdir build
cd build
```
* Type and run the command below on your terminal:
```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_INSTALL_PREFIX=/usr/local \
  -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules \
  -D ENABLE_NEON=ON \
  -D ENABLE_VFPV3=ON \
  -D BUILD_TESTS=OFF \
  -D INSTALL_PYTHON_EXAMPLES=OFF \
  -D BUILD_EXAMPLES=OFF ..
```
* Open ```/etc/dphys-swapfile``` then edit ```CONF_SWAPSIZE=100``` to ```CONF_SWAPSIZE=1024```.
* Type and run the commands below on your terminal:
```
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
make -j4
sudo make install
sudo ldconfig
```
* Open ```/etc/dphys-swapfile``` then edit ```CONF_SWAPSIZE=1024``` to ```CONF_SWAPSIZE=100```.
* Type and run the commands below on your terminal:
```
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
```
* Check OpenCV installation by typing commands below on Python 3:
```
import cv2
print(cv2.__version__)
```
If there are no errors prompted, that means we've been successfully installed OpenCV on our Raspberry Pi 3. The steps mentioned above is a slightly modified version [this](https://www.pyimagesearch.com/2017/10/09/optimizing-opencv-on-the-raspberry-pi/).

## Matplotlib Installation
In this project we will use the well known Matplotlib to display our image. We can install Matplotlib by typing and running ```sudo apt-get install python3-matplotlib``` command on terminal.

## SciPy Installation
Another package that will be used is SciPy. We can install SciPy by typing and running ```sudo apt-get install python3-scipy``` command on terminal.

## The topics which will be included in this project are:
* [Color Spaces](/08_Image_Processing/Color_Spaces).
* [Histogram](/08_Image_Processing/Histogram).
* [Smoothing Filter](/08_Image_Processing/Smoothing_Filter).
* [Thresholding](/08_Image_Processing/Thresholding).
* [Morphology](/08_Image_Processing/Morphology).
* [Labelling](/08_Image_Processing/Labelling).
* [Accessing Camera](/08_Image_Processing/Accessing_Camera).
