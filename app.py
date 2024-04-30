import pickle
import os
import webbrowser
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Parkinsons",
                   layout="wide",
                   page_icon="🧑‍⚕️")

redirect_url = 'http://127.0.0.1:3000/index1.html'

# Saving model to disk

# Open the Pickle File 
model=pickle.load(open('C:/Users/vaishnavi shervegar/Downloads/parkinson disease/deploy_DT.pkl','rb'))
#sidebar for navigate


    # page title
st.title("Parkinson's Disease Prediction ")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
        fo = st.text_input('MDVP_Fo(Hz)')

with col2:
        fhi = st.text_input('MDVP_Fhi(Hz)')

with col3:
        flo = st.text_input('MDVP_Flo(Hz)')

with col4:
        Jitter_percent = st.text_input('MDVP_Jitter(%)')

with col5:
        Jitter_Abs = st.text_input('MDVP_Jitter(Abs)')

with col1:
        RAP = st.text_input('MDVP_RAP')

with col2:
        PPQ = st.text_input('MDVP_PPQ')

with col3:
        DDP = st.text_input('Jitter_DDP')

with col4:
        Shimmer = st.text_input('MDVP_Shimmer')

with col5:
        Shimmer_dB = st.text_input('MDVP_Shimmer(dB)')

with col1:
        APQ3 = st.text_input('Shimmer_APQ3')

with col2:
        APQ5 = st.text_input('Shimmer_APQ5')

with col3:
        APQ = st.text_input('MDVP_APQ')

with col4:
        DDA = st.text_input('Shimmer_DDA')

with col5:
        NHR = st.text_input('NHR')

with col1:
        HNR = st.text_input('HNR')

with col2:
        RPDE = st.text_input('RPDE')

with col3:
        DFA = st.text_input('DFA')

with col4:
        spread1 = st.text_input('spread1')

with col5:
        spread2 = st.text_input('spread2')

with col1:
        D2 = st.text_input('D2')

with col2:
        PPE = st.text_input('PPE')

# code for Prediction
parkinsons_diagnosis = ''

    # creating a button for Prediction    
if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

        st.success(parkinsons_diagnosis)



# Define the URL you want to redirect to
redirect_url = "http://127.0.0.1:3000/index1.html"

# Display the button using Markdown

if st.button("Go back"):
    # When the button is clicked, open the URL in the default web browser
          webbrowser.open_new_tab(redirect_url)