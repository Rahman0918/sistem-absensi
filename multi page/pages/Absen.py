import streamlit as st
import cv2
from datetime import datetime
import pandas as pd  
import csv
import os
import numpy as np
from PIL import Image
        
FRAME_WINDOW = st.image([]) #frame window
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('D:/PENYIMPANAN UTAMA/PROGRAM CODING/STREAMLIT/multi page/Dataset/training.xml')
camera = 0
video = cv2.VideoCapture(camera, cv2.CAP_DSHOW)

st.title("Absensi")
st.subheader("SILAHKAN ABSEN")
run = st.checkbox("Run camera") #checkbox
a = 0
while True:
    if run:
        def faceList(name):
             now = datetime.now()
             dtString = now.strftime('%H:%M:%S')
             with open('D:/PENYIMPANAN UTAMA/PROGRAM CODING/STREAMLIT/multi page/absensi.csv', 'r+') as f:
                    myDataList = f.readlines()
                    nameList = []
                    timeList = []
                    for line in myDataList:
                        entry = line.split(',')
                        nameList.append(entry[0])
                        if len(entry) > 1:
                            timeList.append(entry[1].rstrip())
                    if name not in nameList or (name in nameList and nameList.index(name) < len(timeList) and dtString not in timeList[nameList.index(name)]):
                        f.writelines(f'\n{name},{dtString}')
        a = a + 1
        check, frame = video.read()
        if check:
            abu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            wajah = face_cascade.detectMultiScale(abu, 1.3, 5)
            for(x, y, w, h) in wajah:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Membuat kotak hijau di wajah
                id, conf = recognizer.predict(abu[y:y+h, x:x+w])# Seleksi Id
                 # Seleksi Id
                if (id == 1):
                    id = 'rahman abdullah'
                elif (id == 2):
                    id = 'firmansyah pipii'
                elif (id == 3):
                    id = 'sriyolfina'
                else:
                    id = 'Unknown'
                if id:
                    name = id
                    cv2.putText(frame, name, (x+40, y-10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0))
                    faceList(name)# Panggil fungsi faceList untuk menyimpan data absensi
                    cv2.imshow("Face Recognition", frame)
                    FRAME_WINDOW.image(frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit loop ketika tombol 'q' ditekan
                        break
                else:
                    break
        else:
            print("Gagal menangkap frame dari kamera")
            break
    else:
        break
video.release()# Pastikan kamera ditutup setelah pengguna selesai
cv2.destroyAllWindows()
