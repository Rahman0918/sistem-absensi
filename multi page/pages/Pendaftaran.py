import streamlit as st
import cv2
from datetime import datetime
import pandas as pd  
import csv
import os
import numpy as np
from PIL import Image

camera = 0
video = cv2.VideoCapture(camera, cv2.CAP_DSHOW)
faceDeteksi = cv2.CascadeClassifier('D:/PENYIMPANAN UTAMA/PROGRAM CODING/STREAMLIT/multi page/pages/haarcascade_frontalface_default.xml')

st.title("PENDAFTARAN")
st.subheader("SILAHKAN MENDAFTAR")
run = st.checkbox("Run camera") #checkbox
id_input = st.text_input('Masukkan ID:')
name_input = st.text_input('Masukkan Nama:')  # Tambahkan ini
if run and id_input and name_input:  # Pastikan checkbox dicentang dan ID dan Nama dimasukkan
    id = id_input  # mengambil id
    name = name_input  # mengambil nama
    a = 0
    photo_paths = []  # Untuk menyimpan path foto yang berhasil diambil
    while True: 
        a = a + 1
        check, frame = video.read() 
        # membuat mode pengambilan gambar pada scan menjadi Gray (abu-abu)
        abu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Mendeteksi wajah
        wajah = faceDeteksi.detectMultiScale(abu,1.3,5)
        print(wajah)
        for(x,y,w,h) in wajah:
            # Membuat file foto ke folder Dataset/ dengan identifikasi Id dan perulangan a
            cv2.imwrite('Dataset/User.'+str(id)+'.'+str(a)+'.jpg', abu[y:y+h,x:x+w])
            # Mengenali bentuk wajah (kotak warna hijau di wajah)
            cv2.rectangle(frame, (x,y),(x+w,y+h), (0,255,0),2)
        # Nama Window 
        cv2.imshow("Face Recognation Window", frame)
        # Perulangan dilakukan hingga 30 pengambilan foto
        if (a > 29):
            break

    # Cam berhenti
    video.release()
    cv2.destroyAllWindows()
             
st.title("Sedang di proses")
 # Fungsi untuk melatih foto dan menyimpan hasil training
def train_faces():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    def getImagesWithLabels(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        Ids = []
        for imagePath in imagePaths:
            try:
                pilImage = Image.open(imagePath).convert('L')
                imageNp = np.array(pilImage, 'uint8')
                Id = int(os.path.split(imagePath)[-1].split(".")[1])
                faces = detector.detectMultiScale(imageNp)
                for (x, y, w, h) in faces:
                    faceSamples.append(imageNp[y:y + h, x:x + w])
                    Ids.append(Id)
            except Exception as e:
                st.write(f"berhasil terdaftar: {imagePath} - {e}")
        return faceSamples, Ids
    faces, Ids = getImagesWithLabels('D:/PENYIMPANAN UTAMA/PROGRAM CODING/STREAMLIT/multi page/Dataset')
    recognizer.train(faces, np.array(Ids))
    # Simpan hasil training
    recognizer.save('D:/PENYIMPANAN UTAMA/PROGRAM CODING/STREAMLIT/multi page/Dataset/training.xml')
    st.success("Training selesai!")

# Membuat tombol untuk melatih foto
if st.button("kLIK UNTUK MEMPROSES"):
    train_faces()
