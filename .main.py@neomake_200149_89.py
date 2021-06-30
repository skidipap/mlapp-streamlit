import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split 

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
X = myData.iloc[:, :-1].values
y = myData.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=69)

# Melakukan Scaling 
X_train_ss_scaled = X_train
X_test_ss_scaled = X_test
X_train_mms_scaled = X_train
X_test_mms_scaled = X_test

y_train_ss_scaled = y_train
y_test_ss_scaled = y_test
y_train_mms_scaled = y_train
y_test_mms_scaled = y_test


from sklearn.preprocessing import StandardScaler 

ss_train_test = StandardScaler()
X_train_ss_scaled[:, :-1] = ss_train_test.fit_transform(X_train[:, :-1])
X_test_ss_scaled[:, :-1] = ss_train_test.transform(X_test[:, :-1])

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

l_regressor_ss = LinearRegression()
l_regressor_ss.fit(X_train_ss_scaled, y_train)
y_pred_l_reg_ss = l_regressor_ss.predict(X_test_ss_scaled)

st.write("Dengan Menggunakan Multiple Linear Regression Diperoleh Skor Untuk Data Test")
st.write(r2_score(y_test, y_pred_l_reg_ss))


st.write("# Sekarang Silahkan Masukan Skor Test Kamu Untuk Mengetahui Prediksi Peluang Kelulusan S2 Kamu")


form = st.form(key='my-form')
inputGRE = form.text_input("Masukan GRE Score: ")
inputTOEFL = form.text_input("Masukan TOEFL Score: ")
inputUnivRating = form.text_input("Masukan Rating Univ: ")
inputSOP = form.text_input("Masukan Kekuatan SOP: ")
inputLOR = form.text_input("Masukan Kekuatan LOR: ")
inputCGPA = form.text_input("Masukan CGPA: ")
inputResearch = form.text_input("Pengalaman Researc, 1 Jika Pernah Riset, 0 Jika Tidak")
submit = form.form_submit_button('Submit')

completeData = [[inputGRE, inputTOEFL, inputUnivRating, inputSOP, inputLOR, inputCGPA, inputResearch]]
st.write('Tekan Submit Untuk Melihat Prediksi Peluang S2 Anda')

if submit:
    st.write(f'hello {name}')


#scaledData = ss_train_test.fit_transform(completeData)
#st.write(scaledData)
#submit = st.form_submit_button()
#if submit:
#    prediction = l_regressor_ss.predict(completeData)
#    st.write(prediction)
 



