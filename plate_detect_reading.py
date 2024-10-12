# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 04:34:56 2024

@author: aytur
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
import cv2
from ultralytics import YOLO
import pytesseract  # OCR için gerekli kütüphane

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1450, 800)
        Form.setMaximumSize(QtCore.QSize(1920, 1080))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("QWidget {\n"
"    background: qradialgradient(\n"
"        cx: 0.5, cy: 0.5, radius: 1,\n"
"        fx: 0.5, fy: 0.5,\n"
"        stop: 0 #4682B4, /* Ortada koyu mavi (SteelBlue) */\n"
"        stop: 0.3 #4169E1, /* Daha koyu mavi (Royal Blue) */\n"
"        stop: 0.6 #6A0DAD, /* Koyu mor */\n"
"        stop: 1 #4B0082 /* Dış kenarlarda çok koyu mor (İndigo) */\n"
"    );\n"
"}\n"
"")

        # Sol Taraftaki Görüntü Label'i
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 100, 611, 631))
        self.label.setStyleSheet("QLabel {\n"
"    background-color: #f0f0f0; /* Arka plan rengi */\n"
"    border: 2px solid #555;    /* Kenarlık kalınlığı ve rengi */\n"
"    color: #333;               /* Metin rengi */\n"
"    font-size: 16px;           /* Metin boyutu */\n"
"    padding: 10px;             /* İç boşluk */\n"
"}\n"
"")
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")

        # Tablo Widget'i
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(1270, 100, 161, 521))
        self.tableWidget.setMaximumSize(QtCore.QSize(161, 16777215))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    background-color: #ffffff; /* Beyaz arka plan */\n"
"    gridline-color: #dcdcdc; /* Izgara çizgileri */\n"
"    border: 1px solid #dcdcdc;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f0f0f0; /* Başlık arka planı */\n"
"    padding: 4px;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    color: #333;\n"
"}\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 247, 28))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(159)

        # Orta Görüntü Label'i
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(640, 100, 611, 631))
        self.label_2.setStyleSheet("QLabel {\n"
"    background-color: #f0f0f0; /* Arka plan rengi */\n"
"    border: 2px solid #555;    /* Kenarlık kalınlığı ve rengi */\n"
"    color: #333;               /* Metin rengi */\n"
"    font-size: 16px;           /* Metin boyutu */\n"
"    padding: 10px;             /* İç boşluk */\n"
"}\n"
"")
        self.label_2.setText("")
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")

        # Butonlar
        # BAŞLAT Butonu
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(1280, 630, 141, 41))  # BAŞLAT butonunu y=630 olarak ayarladık
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(-1)
        font.setItalic(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50; /* Yeşil renk */\n"
"    color: white;\n"
"    border: 1px solid #4CAF50;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* Hover rengi */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #388E3C; /* Basılı rengi */\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")

        # DURDUR Butonu
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(1280, 680, 141, 41))  # DURDUR butonunu y=680 olarak ayarladık
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #F44336; /* Kırmızı renk */\n"
"    color: white;\n"
"    border: 1px solid #4CAF50;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E53935; /* Hover rengi */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D32F2F; /* Basılı rengi */\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")

        # PLAKA TESPİTİ Butonu
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(1280, 730, 141, 41))  # PLAKA TESPİTİ butonunu y=730 olarak ayarladık
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: #FF9800; /* Turuncu renk */\n"
"    color: white;\n"
"    border: 1px solid #FF9800;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FB8C00; /* Hover rengi */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F57C00; /* Basılı rengi */\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")

        # Başlık Label'i
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(530, 20, 361, 61))
        self.label_3.setStyleSheet("QLabel {\n"
"    font: bold 28px Arial; /* Kalın ve büyük yazı tipi */\n"
"    color: rgba(255, 255, 255, 0.8); /* Hafif şeffaf beyaz metin */\n"
"    text-align: center; /* Metin ortalama */\n"
"    border: 1px solid #ffffff; /* Beyaz kenarlık */\n"
"    border-radius: 0px; /* Köşe yuvarlaklığı */\n"
"    padding: 10px; /* İç kenar boşluğu */\n"
"    background-color: rgba(0, 0, 0, 0.2); /* Hafif şeffaf arka plan */\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Butonlar ile fonksiyonları bağlama
        self.pushButton_3.clicked.connect(self.start_video)
        self.pushButton_2.clicked.connect(self.stop_video)
        self.pushButton_4.clicked.connect(self.detect_plate_from_center_label)  # Plaka tespiti butonuna fonksiyon bağlandı

        # Başlangıçta video akışı durdurulmuş olmalı
        self.is_running = False
        # Araç tespiti için yolov8n modeli
        self.car_model = YOLO('yolov8n.pt')  # Araç tespiti için model
        # Plaka tespiti için model
        self.plate_model = YOLO('last.pt')  # Plaka tespiti için model
        self.is_showing_vehicle = False
        self.current_vehicle_image = None  # Gösterilecek araç resmi
        self.vehicle_timer = QtCore.QTimer()  # Araç resmi gösterme zamanlayıcı
        self.vehicle_timer.timeout.connect(self.hide_vehicle_image)  # 6 saniye sonra resmi gizleme

        # Tesseract yolunu belirtin
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\aytur\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'  # Windows için

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Plaka Tanıma Sistemi"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "PLAKA"))
        self.pushButton_2.setText(_translate("Form", "DURDUR"))
        self.pushButton_3.setText(_translate("Form", "BAŞLAT"))
        self.pushButton_4.setText(_translate("Form", "PLAKA TESPİTİ"))
        self.label_3.setText(_translate("Form", "PLAKA TANIMA SİSTEMİ"))

    def start_video(self):
        # Video akışını başlat
        if not self.is_running:
            self.is_running = True
            self.cap = cv2.VideoCapture('Plaka Video.mp4')  # Videonun yolu güncellendi
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(30)  # 30 ms aralıklarla güncelle

    def update_frame(self):
        # Frame güncelleme ve model tespiti
        ret, frame = self.cap.read()
        if ret:
            frame_height, frame_width, _ = frame.shape

            # ROI (Region of Interest) belirleme - Görüntünün sadece ön kısmını kullanıyoruz
            roi_y_start = int(frame_height * 0.5)  # Görüntünün alt 50%'sinden başla
            roi = frame[roi_y_start:, :]  # Sadece ön kısım

            # Araç tespiti sadece bu alan üzerinde yapılır
            car_results = self.car_model(roi, conf=0.9)  # Araç tespiti için %90 güven
            if len(car_results[0].boxes) > 0:
                # İlk tespit edilen aracın kutusunu al
                box = car_results[0].boxes[0]
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                # Global koordinatlara çevir
                y1 += roi_y_start
                y2 += roi_y_start

                # Aracın resmini kırp ve ortada göster
                car_image = frame[y1:y2, x1:x2].copy()
                self.current_vehicle_image = car_image  # Şu an gösterilen araç resmi

                if not self.is_showing_vehicle:
                    # Tespit edilen aracın çözünürlüğünü koruyarak göster
                    self.display_full_resolution_image(self.current_vehicle_image, self.label_2)
                    self.is_showing_vehicle = True
                    self.vehicle_timer.start(6000)  # 6 saniye boyunca araç resmini göster

                # Tespit edilen kutuyu ana görüntüde göster
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Tespit edilen kareyi sol tarafa göster
            self.display_image(frame, self.label)
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Video bittiğinde yeniden başlat

    def detect_plate_from_center_label(self):
        # Orta label'da gösterilen araç resminde plaka tespiti yap
        if self.current_vehicle_image is not None:
            self.detect_and_read_plate(self.current_vehicle_image)

    def detect_and_read_plate(self, car_image):
        try:
            # Plaka tespiti yap ve OCR işlemi
            plate_results = self.plate_model(car_image, conf=0.5)  # Plaka tespiti için %50 güven
            if len(plate_results[0].boxes) > 0:
                # İlk tespit edilen plakanın kutusunu al
                plate_box = plate_results[0].boxes[0]
                x1, y1, x2, y2 = map(int, plate_box.xyxy[0])
                plate_image = car_image[y1:y2, x1:x2]

                # Plaka kutusunu araç resminde göster (Yeşil dikdörtgen)
                cv2.rectangle(car_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # Güncellenmiş araç resmini tekrar label_2'de göster (araç resmi kesilmeden)
                self.display_full_resolution_image(car_image, self.label_2)

                # OCR işlemi ile plakayı oku
                plate_text = self.read_plate_with_tesseract(plate_image)
                if plate_text:
                    print(f"Tespit Edilen Plaka: {plate_text}")  # Terminale yazdırma
                    self.add_plate_to_table(plate_text)  # Plakayı tabloya ekleme
                else:
                    print("Plaka okunamadı.")
            else:
                print("Plaka tespit edilemedi.")
        except Exception as e:
            print(f"Plaka tespit ve okuma hatası: {e}")

    def read_plate_with_tesseract(self, plate_image):
        try:
            # Görüntüyü gri tonlamaya çevir
            gray = cv2.cvtColor(plate_image, cv2.COLOR_BGR2GRAY)
            
            # Görüntüyü iyileştirmek için histogram eşitleme uygulayın
            gray = cv2.equalizeHist(gray)

            # Gürültüyü azaltmak için bilateral filter uygulayın
            gray = cv2.bilateralFilter(gray, 11, 17, 17)
            
            # Eşikleme işlemi - adaptif eşikleme
            thresh = cv2.adaptiveThreshold(
                gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
            )

            # Eşiklenmiş görüntüyü biraz büyütme veya küçültme
            resized = cv2.resize(thresh, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

            # OCR işlemi ile metni al
            custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            plate_text = pytesseract.image_to_string(resized, config=custom_config)
            print(f"OCR ile okunan metin: {plate_text}")  # Terminale yazdırma
            return plate_text.strip()
        except Exception as e:
            print(f"OCR hatası: {e}")
            return ""

    def add_plate_to_table(self, plate_text):
        # Tabloya yeni bir satır ekleme
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        item = QtWidgets.QTableWidgetItem(plate_text)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(row_position, 0, item)

    def hide_vehicle_image(self):
        # Araç resmini gizleme ve flag sıfırlama
        self.label_2.clear()  # Orta labeli temizle
        self.is_showing_vehicle = False
        self.vehicle_timer.stop()  # Zamanlayıcıyı durdur

    def stop_video(self):
        # Video akışını durdur
        if self.is_running:
            self.is_running = False
            self.cap.release()
            self.timer.stop()
            self.vehicle_timer.stop()
            self.current_vehicle_image = None
            self.label_2.clear()  # Orta labeli temizle

    def display_image(self, img, label):
        # OpenCV görüntüsünü PyQt label'a aktar ve orantılı boyutlandır
        height, width, channel = img.shape
        label_width = label.width()
        label_height = label.height()

        # Orantılı boyutlandırma hesapla
        scale_width = label_width / width
        scale_height = label_height / height
        scale = min(scale_width, scale_height)

        new_width = int(width * scale)
        new_height = int(height * scale)

        resized_img = cv2.resize(img, (new_width, new_height))

        # Resized image to QImage
        qformat = QImage.Format_RGB888
        img_rgb = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
        out_image = QImage(img_rgb.data, new_width, new_height, 3 * new_width, qformat)

        label.setPixmap(QPixmap.fromImage(out_image))
        label.setAlignment(QtCore.Qt.AlignCenter)

    def display_full_resolution_image(self, img, label):
        # OpenCV görüntüsünü PyQt label'a aktar ve tam çözünürlükte göster
        height, width, channel = img.shape
        bytes_per_line = 3 * width
        qformat = QImage.Format_RGB888
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        out_image = QImage(img_rgb.data, width, height, bytes_per_line, qformat)

        label.setPixmap(QPixmap.fromImage(out_image))
        label.setAlignment(QtCore.Qt.AlignCenter)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
