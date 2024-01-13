import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="ABSENSI MAHASISWA",
    page_icon=Image.open('absensi.png'),
)

st.title("Home")
st.sidebar.success("Pilih Halaman Di Atas")
st.subheader("Selamat datang di halaman absen mahasiswa")
st.write("web ini di buat dengan tujuan untuk absensi mahasiswa menggunakan face recognition")
Image.open('absen.jpg')
st.image("absen.jpg")
st.write("untuk memenuhi tugas projek computer vision")
