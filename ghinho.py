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
