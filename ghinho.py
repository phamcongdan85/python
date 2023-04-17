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
