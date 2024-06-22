import streamlit as st
import requests

# Streamlit app title
st.title('Formant Prediction Application')

# Streamlit components to input formants
formant1 = st.slider('Formant 1', min_value=0, max_value=2000, value=400)
formant2 = st.slider('Formant 2', min_value=0, max_value=2000, value=555)
formant3 = st.slider('Formant 3', min_value=0, max_value=2000, value=899)

# Button to trigger prediction
if st.button('Predict'):
    # Prepare data to send to Flask API
    formants = [formant1, formant2, formant3]
    payload = {'features': formants}

    try:
        # Make POST request to Flask API
        response = requests.post('http://127.0.0.1:5000/predict', json=payload)

        # Check if request was successful
        if response.status_code == 200:
            prediction = response.json()['prediction']
            
            # Map predictions to vowels
            vowels = ['A', 'E', 'I', 'O', 'U']
            if prediction in range(len(vowels)):
                st.success(f'This is vowel \'{vowels[prediction]}\'')
                
                # Display button with predicted vowel text
                st.button(f'Predicted Vowel: {vowels[prediction]}')

        else:
            st.error(f'Error: {response.text}')

    except requests.exceptions.RequestException as e:
        st.error(f'Request failed: {e}')