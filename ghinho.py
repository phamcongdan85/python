1. 
Để cài các gói cần thiết trong thư mục đã tải về: 
pip install -r requirements.txt --no-index --find-links download


Dong bo cac goi cai dat giua cac may tinh
pip freeze > requirements.txt
pip install --download=/path/to/packages/downloaded -r requirements.txt

tao wheel file
pip wheel pyspark-2.4.6.tar.gz --wheel-dir download


# Tai file wheel ve may

pip wheel -r requirements.txt -w .\outputdir

# Tao khong duoc file wheel thi can tai python-dev
sudo apt-get install python3.x-dev

# tai mot thu vien pip ve

 pip download -d ./out1 pyOpenSSL




## Cai java

link https://stackjava.com/install/cai-dat-java-jdk-tren-ubuntu-linux-bang-file-tar-gz.html


Home » Install » Cài đặt Java, JDK trên Ubuntu (Linux) bằng file tar.gz

Cài đặt Java, JDK trên Ubuntu (Linux) bằng file tar.gz
Posted on Tháng Năm 20, 2018
Cài đặt Java, JDK trên Ubuntu (Linux) bằng file tar.gz

(Xem thêm: Cài đặt Java trên Ubuntu/Linux từ Repository)

Download và cài đặt JDK từ Oracle
Trong bài này mình sẽ thực hiện cài đặt Java 8 (đây là bản ổn định nhất tại thời điểm hiện tại). Java 9 thì không thay đổi nhiều còn Java 10 thì bắt đầu tính phí.

Truy cập https://www.oracle.com/technetwork/java/javaee/downloads/jdk8-downloads-2133151.html để tải bản JDK tương ứng với máy của mình.

Chọn Accept License Agreement và chọn bản JDK.

Máy mình 64 bit nên mình sẽ chọn Linux x64 và đuôi mở rộng là tar.gz

Cài đặt Java, JDK trên Ubuntu (Linux) bằng file tar.gz

Tạo folder /opt/java

sudo mkdir /opt/java
Giải nén file .tar.gz vừa tải về vào folder /opt/java

sudo tar xvzf jdk-8u211-linux-x64.tar.gz -C /opt/java
Cài đặt Java, JDK trên Ubuntu (Linux) bằng file tar.gz

Kết quả sau khi giải nén:

Cài đặt Java, JDK trên Ubuntu (Linux) bằng file tar.gz

Thiết lập biến môi trường JAVA_HOME
Chạy lệnh sau để mở file chứa biến môi trường:

sudo gedit /etc/environment
(Nếu bạn chỉ sử dụng dòng lệnh thì có thể thay lệnh gedit bằng vi hoặc nano)

Thêm dòng JAVA_HOME=your_java_path, với your_java_path chính là folder bạn vừa giải nén java.

Ví dụ:JAVA_HOME=/opt/java/jdk1.8.0_221

Thêm biến JAVA_HOME vào PATH

Cài đặt Java, JDK trên Ubuntu (Linux) bằng file tar.gz

Khởi động lại máy để hệ thống cập nhật biến môi trường.

Chạy lệnh java -version để kiểm tra version java vừa cài:

Chạy lệnh javac -version kiểm tra version javac

Chạy lệnh echo $JAVA_HOME để kiểm tra biến môi trường java

Cài đặt Java, JDK trên Ubuntu (Linux) bằng file tar.gz

 

Okay, Done!




####################################################################
caif cuda


#!/bin/bash

### steps ####
# verify the system has a cuda-capable gpu
# download and install the nvidia cuda toolkit and cudnn
# setup environmental variables
# verify the installation
###

### to verify your gpu is cuda enable check
lspci | grep -i nvidia

### If you have previous installation remove it first. 
sudo apt purge nvidia* -y
sudo apt remove nvidia-* -y
sudo rm /etc/apt/sources.list.d/cuda*
sudo apt autoremove -y && sudo apt autoclean -y
sudo rm -rf /usr/local/cuda*

# system update
sudo apt update && sudo apt upgrade -y

# install other import packages
sudo apt install g++ freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev

# first get the PPA repository driver
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update

# find recommended driver versions for you
ubuntu-drivers devices

# install nvidia driver with dependencies
sudo apt install libnvidia-common-515 libnvidia-gl-515 nvidia-driver-515 -y

# reboot
sudo reboot now

# verify that the following command works
nvidia-smi

sudo wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/3bf863cc.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /"

# Update and upgrade
sudo apt update && sudo apt upgrade -y

 # installing CUDA-11.8
sudo apt install cuda-11-8 -y

# setup your paths
echo 'export PATH=/usr/local/cuda-11.8/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
sudo ldconfig

# install cuDNN v11.8
# First register here: https://developer.nvidia.com/developer-program/signup

CUDNN_TAR_FILE="cudnn-linux-x86_64-8.7.0.84_cuda11-archive.tar.xz"
sudo wget https://developer.download.nvidia.com/compute/redist/cudnn/v8.7.0/local_installers/11.8/cudnn-linux-x86_64-8.7.0.84_cuda11-archive.tar.xz
sudo tar -xvf ${CUDNN_TAR_FILE}
sudo mv cudnn-linux-x86_64-8.7.0.84_cuda11-archive cuda

# copy the following files into the cuda toolkit directory.
sudo cp -P cuda/include/cudnn.h /usr/local/cuda-11.8/include
sudo cp -P cuda/lib/libcudnn* /usr/local/cuda-11.8/lib64/
sudo chmod a+r /usr/local/cuda-11.8/lib64/libcudnn*

# Finally, to verify the installation, check
nvidia-smi
nvcc -V

# install Pytorch (an open source machine learning framework)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
