import streamlit as st
import joblib
import numpy as np

# Charger le modèle
grid_result = joblib.load("saved_models/model_01.pkl")

# Fonction de prédiction
def predict_diabetes(pregnancies, glucose, blood_pressure, bmi, age):
    prediction = grid_result.predict([[pregnancies, glucose, blood_pressure, bmi, age]])
    return prediction[0]

# Titre de l'application
st.title('Prédiction de diabète')

# Section pour saisir les informations du patient
st.sidebar.header('Informations sur le patient')
pregnancies = st.sidebar.slider('Grossesses', 0, 20, 1)
glucose = st.sidebar.slider('Glucose', 0, 200, 100)
blood_pressure = st.sidebar.slider('Pression artérielle', 0, 150, 70)
bmi = st.sidebar.slider('Indice de masse corporelle (BMI)', 0.0, 70.0, 25.0)
age = st.sidebar.slider('Âge', 20, 90, 30)

# Bouton pour faire la prédiction
if st.sidebar.button('Prédire'):
    result = predict_diabetes(pregnancies, glucose, blood_pressure, bmi, age)
    if result == 0:
        st.write('Le patient n\'est pas diabétique.')
    else:
        st.write('Le patient est diabétique.')