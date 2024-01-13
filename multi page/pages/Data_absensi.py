import pandas as pd  
import streamlit as st

df = pd.read_csv('D:/PENYIMPANAN UTAMA/PROGRAM CODING/STREAMLIT/multi page/absensi.csv')
print(df.head())  
df = pd.read_csv('D:/PENYIMPANAN UTAMA/PROGRAM CODING/STREAMLIT/multi page/absensi.csv')
st.subheader("MAHASISWA YANG TERDAFTAR")
st.write("DAFTAR HADIR MAHASISWA")
df = pd.read_csv('D:/PENYIMPANAN UTAMA/PROGRAM CODING/STREAMLIT/multi page/absensi.csv')
st.write(df)

