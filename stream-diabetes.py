import pickle
import streamlit as st

# Membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul web
st.title('Prediksi Data Mining Diabetes')

#membagi kolom
col1,col2=st.columns(2)

with col1:
    Pregnancies = st.text_input('Masukkan nilai Pregnancies')
with col2:
    Glucose = st.text_input('Masukkan nilai Glucose')
with col1:
    BloodPressure = st.text_input('Masukkan nilai BloodPressure')
with col2:
    SkinThickness = st.text_input('Masukkan nilai SkinThickness')
with col1:
    Insulin = st.text_input('Masukkan nilai Insulin')
with col2:
    BMI = st.text_input('Masukkan nilai BMI')
with col1:
    DiabetesPedigreeFunction = st.text_input('Masukkan nilai DiabetesPedigreeFunction')
with col2:
    Age = st.text_input('Masukkan nilai Age')

# Kode untuk prediksi
diab_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI,
                                               DiabetesPedigreeFunction, Age]])

    if diab_prediction[0] == 1:
        diab_diagnosis = 'Pasien terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien tidak terkena Diabetes'

# Memastikan st.success(diab_diagnosis) berada di luar blok if
st.success(diab_diagnosis)
