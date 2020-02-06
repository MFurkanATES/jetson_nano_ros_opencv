# jetson_nano_ros_opencv

Jetson nano icin csi kamera portuna takili kameradan , gstreamer kullanarak ROS icerisine opencv-cv_bridge uzerinden video yayini yapmakta kullandigim opencv_mst dosyasidir.Bu dosya calistirilmadan once ros calistirilmis olmalidir,opencv_mst paketleri yayinlanmaya basladiginde sub_opencv dosyasini calistirarak goruntu yayinini kontrol edebilirsiniz
opencv_mst dosyasinin icerisinde gstreamer stringini degistirerek goruntu parametreleri degistirebilirsiniz.


Calistirmak icin ayri ayri terminalleri acin

1.terminalde ROS u baslatin

roscore

2.terminalde opencv_mst dosyasini bulundugu klasorde gidip calistirin

python opencv_mst.py

3.terminalde sub_opencv_mst dosyasinin bulunduğu klasore gidip dosyayi calistirin,bu sayede ros icerisine yapilan yayini görebileceksiniz

python sub_opencv_mst.py


sonrasinda kendi kodunuzda sub_opencv_mst de ki gibi görüntü alabilirsiniz,Burda ki olusturulmus pipeline ROS icerisine yayin yaptigi icin,ros icerisinde yazmis oldugunuz farkli programladan bu yayina ulasabilirsiniz,herhangi bir rtsp server baglantisina vs. gerek kalmaz.

Mekatronik sistem tasarimi dersi 2019-Konya
