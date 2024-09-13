import streamlit as st
import pickle
import numpy as np
#loading the saved model
st.title('Loan prediction using svm classifier')
model=pickle.load(open("/Users/bansalshrivastava/Desktop/loan_prediction/loan_prediction_model.sav","rb"))

def loan_prediction(input_data):

  input_data_as_np_array = np.asarray(input_data)
  input_data_reshaped = input_data_as_np_array.reshape(1,-1)
  prediction = model.predict(input_data_reshaped)
  print(prediction)

  if (prediction[0] == 0):
    return 'The loan will not be approved'
  else:
    return 'The loan will be approved'

def main():
    #getting input from user
    gender= st.text_input("if male enter 1 and if female enter 0")
    married= st.text_input("if married enter 1 and if not enter 0")
    Dependents= st.text_input("dependency level (0 to 4)")
    Education= st.text_input("if Graduate enter 1 if not enter 0")
    Self_Employed= st.text_input("if self employed enter 1 if not enter 0")
    ApplicantIncome= st.text_input("Income of applicant")
    CoapplicantIncome= st.text_input("Income of Coapplicant")
    LoanAmount= st.text_input("enter loan amount")
    Loan_Amount_Term= st.text_input("enter loan amount term")
    Credit_History= st.text_input("credit history 0 or 1")
    Property_Area= st.text_input("if rural enter 0 if Semiurban enter 1 if urban enter 2")
    #code for prediction
    Loan_Status=''
    #creating a button for prediction
    if st.button("Loan Status result"):
        Loan_Status=loan_prediction([gender, married ,Dependents ,Education ,Self_Employed ,ApplicantIncome ,CoapplicantIncome ,LoanAmount ,Loan_Amount_Term ,Credit_History ,Property_Area])
    st.success(Loan_Status)
if __name__ == '__main__':
    main()