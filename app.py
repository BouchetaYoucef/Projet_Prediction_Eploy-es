import streamlit as st
import pandas as pd
from PIL import Image
import pickle

## Variables d'environnement (secrets sur streamlit cloud) ##
valid_login = st.secrets["VALID_LOGIN"]
valid_password = st.secrets["VALID_PASSWORD"]

## Functions
def load_model():
    with open('model_pkl2.pickle', 'rb') as f:
        model = pickle.load(f)
    return model

def return_prediction(data):
    prediction = model.predict(data)
    if prediction == 0:
        return("This employee will probably LEAVE your company")
    else:  
        return("This employee will probably STAY in your company")    

## Import Model
model = load_model()

## Title
st.title("Employee leaving or not ?")
st.text("Check if an employee will leave the company or not.")

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == valid_password and st.session_state["login"] == valid_login:
            st.session_state["password_correct"] = True 
            del st.session_state["password"]  # don't store password
            del st.session_state["login"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Login", on_change=password_entered, key="login"
        )
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Login", on_change=password_entered, key="login"
        )
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Identifiants incorrects, veuillez réessayer")
        return False
    else:
        # Password correct.
        return True
    
## Login ##
if check_password():

    # Application ##
    img1 = Image.open('attrition.jpg')
    img1 = img1.resize((200, 200))
    st.image(img1, use_column_width=False)

## INPUTS ##
## For Education
Education = st.selectbox('Education',
                         (0, 1, 2))

## For Joining
JoiningYear = st.selectbox('JoiningYear',
                           (2012, 2013, 2014, 2015, 2016, 2017, 2018))

## For City
City_display = ('Bangalore','Pune','New Delhi')
City_options = list(range(len(City_display)))
City = st.selectbox("City",City_options, format_func=lambda x: City_display[x])

## For Payement
PaymentTier = st.selectbox('PaymentTier',
                           (1,2,3))

## For Age
Age = st.selectbox("Age",
                  (22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41))

## For Gender
Gender = st.selectbox('Gender',
                      (0, 1))

## For Bench
EverBenched = st.selectbox('EverBenched', 
                           (0, 1))

## For Experience
ExperienceInCurrentDomain = st.selectbox('ExperienceInCurrentDomain',
                                         (0, 1, 2, 3, 4, 5, 6, 7))

## For Prediction
if st.button(label="Prediction"):
    data = pd.DataFrame([[Education, JoiningYear, City, PaymentTier, Age, 
                          Gender, EverBenched, ExperienceInCurrentDomain]], 
                          columns=['Education', 'JoiningYear', 'City',
                                   'PaymentTier', 'Age', 'Gender',
                                   'EverBenched', 'ExperienceInCurrentDomain'])
    result = return_prediction(data)
    st.write(result)

## New Functionnality Added
    # Download prediction
    st.download_button("Download data",
                       data.to_csv(index=False).encode('utf-8'),
                       "Prediction.csv",
                       "text/csv")