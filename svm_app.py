import streamlit as st
import pickle
#loading the saved model
st.title('Loan prediction using svm classifier')
model=pickle.load(open("/Users/bansalshrivastava/Desktop/loan_prediction/loan_prediction_model.sav","rb"))

def loan_prediction(input_data):

  input_data_as_np_array = np.asarray(input_data)
  input_data_reshaped = input_data_as_np_array.reshape(1,-1)
  prediction = model.predict(input_data_reshaped)
  print(prediction)

  if (prediction[0] == 0):
    return 'The loan is not approved'
  else:
    return 'The loan is approved'

def main():
    #getting input from user
    gender= st.text_input("male or female")
    married= st.text_input("yes or no")
    Dependents= st.text_input("0 or 1")
    Education= st.text_input("Graduate or not graduate")
    Self_Employed= st.text_input("yes or no")
    ApplicantIncome= st.text_input("Income of applicant")
    CoapplicantIncome= st.text_input("Income of Coapplicant")
    LoanAmount= st.text_input("enter loan amount")
    Loan_Amount_Term= st.text_input("enter loan amount term")
    Credit_History= st.text_input("0 or 1")
    Property_Area= st.text_input("rural or urban")
    #code for prediction
    Loan_Status=''
    #creating a button for prediction
    if st.button("Loan Status result"):
        Loan_Status=loan_prediction(["gender","married","Dependents","Education","Self_Employed","ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Credit_History","Property_Area"])
    st.success(Loan_Status)
if __name__ == '_main_':
    main()