import streamlit as st 
import pandas as pd 

st.write("""
    # Program Prediksi Peluang Penerimaan Program S2
""")

st.write( """
    ## Keterangan Data Yang Digunakan
    1. GRE Score: Merupakan Score Test Untuk Masuk Program S2 (0 - 340) Bersifat Continous
    2. TOEFL Score: Score Kemampuan TOEFL (0 - 120) Bersifat Continous
    3. University Rating: Rating Universitas (0 - 5) Bersifat Ordinal
    4. Kekuatan Surat Rekomendasi (0 - 5) Bersifat Ordinal
    5. GPA Sewaktu Undergraduate (0 - 10) Bersifat Continous
    6. Pengalaman Riset (0 : tidak ada, 1 : ada) Bersifat Nominal
    
    7. Peluang Diterima (0 - 1) Merupakan Dependent Variable

""")

st.write("""
    ## Overview Data
""")

myData = pd.read_csv('data.csv')
st.dataframe(myData)

st.write("""
    ## Deskripsi Data
""")

st.dataframe(myData.describe())

# Preproccessing Data
# Memisahkan Label Dan Fitur 

