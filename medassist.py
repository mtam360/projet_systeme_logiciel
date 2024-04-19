import streamlit as st
import joblib
import numpy as np

# Charger le modèle
grid_result = joblib.load("saved_models/model_01.pkl")

# Fonction de prédiction
def predict_diabetes(pregnancies, glucose, blood_pressure, bmi, age):
    prediction = grid_result.predict([[pregnancies, glucose, blood_pressure, bmi, age]])
    return prediction[0]

# Informations d'identification pré-enregistrées
USERNAME = 'adeja'
PASSWORD = 'adeja'

# Titre de l'application
st.title('Prédiction de diabète')

# Vérifier l'état de connexion
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Interface de connexion
def login():
    # Champ de saisie pour le nom d'utilisateur
    username_input = st.text_input('Nom d\'utilisateur')

    # Champ de saisie pour le mot de passe
    password_input = st.text_input('Mot de passe', type='password')

    # Vérification des informations d'identification
    if st.button('Se connecter'):
        if username_input == USERNAME and password_input == PASSWORD:
            st.session_state.logged_in = True
            st.success('Connexion réussie!')
            st.experimental_rerun()  # Rediriger vers la page principale
        else:
            st.error('Nom d\'utilisateur ou mot de passe incorrect.')

# Fonction pour afficher l'interface graphique principale
def show_main_interface():
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
            st.write('Le patient est diabétique.')
        else:
            st.write('Le patient n/est diabétique.')

# Appel de la fonction de connexion si non connecté
if not st.session_state.logged_in:
    login()
else:
    show_main_interface()
