from copyreg import pickle
import streamlit as st
import base64
from PIL import Image
import pickle
import time

st.header('Diabetes Predictor')

tab1, tab2 ,tab3 = st.tabs(["Instructions & informations", "prediction","About"])
with tab1:
    st.subheader("What is Diabetes?")
    st.write("- Diabetes is a lifelong condition that causes a person's blood sugar level to become too high.")
    st.subheader("What information is needed to make a prediction?")
    st.write("1- Pregnancies : we are talking about the month of pregnancy. If it is in the first month, for example, we write 1 , and if there is no pregnancy, we write 0 and so on ... ")
    st.write("2- Glucose : we mean the level of sugar in the blood, and this is when we measure random glucose, we are not talking here about a cumulative measure or a fasting measure. ")
    st.write("3- Insulin : we mean the level of insulin secretion in the body.")
    st.write("4- Age : your old in years not months or days or else ..")
    st.write("5- BMI : is a person's weight in kilograms (or pounds) divided by the square of height in meters (or feet).")
    st.latex(" USC Units:BMI = 703 × mass (lbs) / height^2 (in)")
    st.latex(" SI, Metric Units:BMI = mass (kg) / height^2 (m)")
    st.subheader("About Model")
    st.write("- we used Random Forest Algorithm")
    st.write('- Model Accuracy : 91%')
# ----------------------------------------------------------------------------

with tab2:
    st.header("Prediction")
    st.text('1- Make sure that the entries are written correctly')
    st.text('2- Press Predict')
    st.write("-----------------------------------------")
    try:
        Age=st.slider('Age', 1, 100)
        Pregnancies=st.selectbox('Pregnancies',[0,1,2,3,4,5,6,7,8,9,10,11,12])
        Glucose=st.text_input('Glucose')
        Insulin=st.text_input('Insulin')
        bmi=st.text_input('BMI')
        with open('diabetes.pkl', 'rb') as f:
            model_RF = pickle.load(f)

    

        time.sleep(1.1)
        results=model_RF.predict([[Pregnancies, Glucose, Insulin, bmi, Age]])
    except :
        st.write('Check From Your Inputs')
 
    if st.button("Predict"):
        if results[0] == 0 :
            st.success("You are Healthy")
        else:
            st.error('You have diabetes, you should see a doctor.')
# ----------------------------------------------------------------------------
with tab3:
    st.header("How I Am ?")
    st.text('My Name is Abdelhamid Adel, Data scientist')
    st.text('I am From Cairo, Egypt')
    if st.button(" MY GitHub"):
        import webbrowser
        webbrowser.open('https://github.com/AbdelhamidADel', new=2)
