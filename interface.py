import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd

# Set page title and favicon
st.set_page_config(page_title="Disease Prediction System", page_icon=":hospital:")



#loading the models

#diab_model = pickle.load(open("C:/Users/Divyansh/Desktop/multiple_disease/saved_models/Diabetes_svm.pkl","rb"));
heart_model = pickle.load(open("C:/Users/Divyansh/Desktop/multiple_disease/saved_models/naive_heart.pkl","rb"));
park_model = pickle.load(open("C:/Users/Divyansh/Desktop/multiple_disease/saved_models/svm_parks.pkl","rb"));
stroke_model = pickle.load(open("C:/Users/Divyansh/Desktop/multiple_disease/saved_models/Brain_Stroke.pkl","rb"))
stroke_model2 = pickle.load(open("C:/Users/Divyansh/Desktop/multiple_disease/saved_models/Brain_Stroke_NB.pkl","rb"))
diab_model2 = pickle.load(open("C:/Users/Divyansh/Desktop/multiple_disease/saved_models/diabetes_svm2.pkl","rb"));

#diab_model = pickle.load(open("D:\Mini_PROJECT/saved_models/Diabetes_svm.pkl","rb"));
#heart_model = pickle.load(open("D:\Mini_PROJECT/saved_models/naive_heart.pkl","rb"));
#park_model = pickle.load(open("D:\Mini_PROJECT/saved_models/svm_parks.pkl","rb"));
#stroke_model = pickle.load(open("D:\Mini_PROJECT/saved_models/Brain_Strokes.pkl","rb"))
#stroke_model2 = pickle.load(open("D:\Mini_PROJECT/saved_models/Brain_Stroke_NB.pkl","rb"))
#diab_model2 = pickle.load(open("D:\Mini_PROJECT/saved_models/diabetes_svm2.pkl","rb"));


#Creating the sidebar of our web application

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Brain Stroke Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital',
                           icons=['activity', 'file-earmark-medical', 'heart-pulse', 'person'],
                           default_index=0)
    
if selected=='Diabetes Prediction':
    #decorate the page
    st.title("Diabetes Prediction")
    #Take input from user
    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        glucose = st.text_input("Glucose Level")
    with col3:
        blood_pressure = st.text_input("Blood Pressure Level")
    with col1:
        skin_thickness = st.text_input("Skin Thickness Value")
    with col2:
        insulin = st.text_input("Insulin Level")
    with col3:
        bmi = st.text_input("BMI value")
    # with col1:
        # diabetes_pedigree = st.text_input("Diabetes Pedigree function value")
    with col1:
        age = st.text_input("Age")

    user_input=[pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,age]

    # user_input = [int(x) for x in user_input]
    
    diab_diagnosis=''
    
    if st.button("Diabetes Test Result"):
        predn = diab_model2.predict([user_input])
        if predn[0]==0:
            diab_diagnosis="Person is not diabetic"
        else:
            diab_diagnosis="Person is diabetic"
    
        st.success(diab_diagnosis)


# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    #giving page title
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        val = st.selectbox('Sex',['','Male','Female'])
        sex=0
        if val=='Male':
            sex=1
        else:
            sex=0

    with col3:
        cp = st.slider('Chest Pain level',0,3)

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs=0
        value = st.selectbox('Fasting Blood Sugar',['','greater than 120mg/dl','less than 120mg/dl'])
        if value == 'greater than 120mg/dl':
            fbs=1
        else:
            fbs=0

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        value2 = st.selectbox('Exercise Induced Angina',['','Yes','No'])
        if value2=='Yes':
            exang=1
        else:
            exang=0

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('Thal(Duration of exercise test in minutes)')

    #Code for Prediction
    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

        st.success(heart_diagnosis)

#Parkinsons Prediction
if selected == "Parkinsons Prediction":

    #title of our page
    st.title("Parkinson's Disease Prediction")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        fo = st.text_input('MDVP::Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP::Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP::Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP::Jitter(%)')

    with col1:
        Jitter_Abs = st.text_input('MDVP::Jitter(Abs)')

    with col2:
        RAP = st.text_input('MDVP::RAP')

    with col3:
        PPQ = st.text_input('MDVP::PPQ')

    with col4:
        DDP = st.text_input('Jitter::DDP')

    with col1:
        Shimmer = st.text_input('MDVP::Shimmer')

    with col2:
        Shimmer_dB = st.text_input('MDVP::Shimmer(dB)')

    with col3:
        APQ3 = st.text_input('Shimmer::APQ3')

    with col4:
        APQ5 = st.text_input('Shimmer::APQ5')

    with col1:
        APQ = st.text_input('MDVP::APQ')

    with col2:
        DDA = st.text_input('Shimmer::DDA')

    with col3:
        NHR = st.text_input('NHR')

    with col4:
        HNR = st.text_input('HNR')

    with col1:
        RPDE = st.text_input('RPDE')

    with col2:
        DFA = st.text_input('DFA')

    with col3:
        spread1 = st.text_input('Spread1')

    with col4:
        spread2 = st.text_input('Spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    #Prediction using our trained model
    parkinsons_diagnosis = ''
   
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = park_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

        st.success(parkinsons_diagnosis)

#Brain Stroke Prediction

if selected == "Brain Stroke Prediction":

    #title of our page
    st.title("Brain Stroke Prediction")
  
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        key = st.selectbox("Gender",["","Male","Female"])
        # print(key)
        gender=0
        if key == "Male":
            gender=1
        else:
            gender=0

    with col2:
        age = st.text_input("Age")

    with col3:
        hypertension=0
        key2 = st.selectbox("Hypertension",["","Yes","No"])
        # print(key2)
        if key2=="Yes":
            hypertension=1
        else:
            hypertension=0

    with col4:
        heart_disease=0
        key3=st.selectbox("Any Heart Disease",["","Yes","No"]) 
        if key3== "yes":
            heart_disease=1
        else:
            heart_disease=0

    with col1:
        ever_married=0
        key4=st.selectbox("Ever Married",["","Yes","No"])
        if key4=="Yes":
            ever_married=1
        else:
            ever_married=0

    with col2:
        work_type=0
        val =st.selectbox("Work Type",["","Private","Self-employed","Govt_job","Student"])
        # print(val)
        if val=="Private" :
            work_type=1
        elif val=="Self-employed" :
            work_type=2
        elif val=="Govt_job":
            work_type=0
        else:
            work_type=3

    with col3:
        Residence_type=0
        key6=st.selectbox("Residence_Type",["","City/Urban","Rural"]) 
        # print(key6)
        if key6=="Rural":
            Residence_type=0
        else:
            Residence_type=1

    with col4:
        glucose_level = st.text_input("Glucose Level")

    with col1:
        bmi = st.text_input('BMI value')

    with col2:
        smoking = st.selectbox("Smoking Status",["","Formerly smoked","Never smoked","Smokes","Not known"])
        smoking_status=0
        if smoking=="Formerly smoked":
            smoking_status=1
        elif smoking=="Never smoked":
            smoking_status=2
        elif smoking=="Smokes":
            smoking_status=3
        else:
            smoking_status=0
    

    statement=''
    if st.button("Brain Stroke Prediction Result"):
        
        input_val = [gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,glucose_level,bmi,smoking_status]

        user_input = [float(x) for x in input_val]

        # print(user_input)

        prediction = stroke_model2.predict([user_input])
       
        if prediction[0]==0:
            statement="You are healthy and out of danger of stroke"
        else:
            statement="You have high chances of stroke"
        
        st.success(statement)

