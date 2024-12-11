import streamlit as st
import pickle
def predict():
    Usage=st.text_input("**Usage_kWh**","")
    LAGCRPK= st.text_input("**Lagging_Current_Reactive.Power_kVarh**","")
    LEACRPK=st.text_input("**Leading_Current_Reactive_Power_kVarh**","")
    CO2=st.text_input("CO2(**tCO2**)","")
    LAGCPF=st.text_input("**Lagging_Current_Power_Factor**","")
    LEACPF=st.text_input("**Leading_Current_Power_Factor**","")
    NSM=st.text_input("**NSM**","")
    WeekStatus=st.selectbox("**WeekStatus**",("Weekday","Weekend"))
    if WeekStatus == "Weekday":
        ws=0
    else:
        ws=1

    DOW=st.selectbox("Day of week",("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"))
    if DOW=='Monday':
        d=1
    elif DOW=='Tuesday':
        d=5
    elif DOW=='Wednesday':
        d=6
    elif DOW=='Thursday':
        d=4
    elif DOW=='Friday':
        d=0
    elif DOW=='Saturday':
        d=2
    else:
        d=3
    features=[Usage,LAGCRPK,LEACRPK,CO2,LAGCPF,LEACPF,NSM,ws,d]
    scaler=pickle.load(open('scaler.sav','rb'))
    model=pickle.load(open('model.sav','rb'))
    pred=st.button("PREDICT")

    if pred:
        result=model.predict(scaler.transform([features]))
        if result==0:
            st.write("**LIGHT LOAD**")
        elif result ==1:
            st.write("**MEDIUM LOAD**")
        else:
            st.write("**HIGH LOAD**")