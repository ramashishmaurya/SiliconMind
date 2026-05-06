import streamlit as st 
import requests 


st.title('calling the api')

name = st.text_input('Enter the name')
age = st.text_input('Enter the values age')

if st.button('click'):
    url = 'http://127.0.0.1:8000/api' # this  is api that we made 

    data = {
        "name":name , 
        "age":age
    }
    try:
        responses = requests.post(url=url , json=data)
        if responses.status_code ==200:
            st.success('connected to api')
            st.json(responses.json())
        else:
            st.error({
                "error is ":responses.status_code
            })
    except Exception as e:
        st.error(f'this is can be erro {e}')

