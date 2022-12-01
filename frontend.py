import streamlit as st
import requests

# Give the Name of the Application
st.title('Fire Alarm')

# Create Submit Form
with st.form(key='form_parameters'):
    T = st.number_input('Temperature (C)', min_value=0.0, step=0.1)
    H = st.number_input('Humidity (%)', min_value=0.0, step=0.1)
    tvoc = st.number_input('TVOC (ppb)', min_value=0.0, step=0.1)
    co2 = st.number_input('eCO2 (ppm)', min_value=0.0, step=0.1)
    h2 = st.number_input('Raw H2', min_value=0.0, step=0.1)
    enol = st.number_input('Ethanol', min_value=0.0, step=0.1)
    P = st.number_input('Pressure (hPa)', min_value=0.0, step=0.1)
    pm1 = st.number_input('PM 1.0', min_value=0.0, step=0.1)
    pm2_5 = st.number_input('PM 2.5', min_value=0.0, step=0.1)
    pm0_5 = st.number_input('PM 0.5', min_value=0.0, step=0.1)
    nc0_5 = st.number_input('NC 0.5', min_value=0.0, step=0.1)
    nc1 = st.number_input('NC 1.0', min_value=0.0, step=0.1)
    nc2_5 = st.number_input('NC 2.5', min_value=0.0, step=0.1)
    cnt = st.number_input('CNT', min_value=0.0, step=0.1)


    submitted = st.form_submit_button('Predict')

# inference
if submitted:
    URL = 'http://127.0.0.1:5000/predict'
    param = {'Temperature[C]': T,
      'Humidity[%]': H, 
      'TVOC[ppb]': tvoc, 
      'eCO2[ppm]': co2,
      'Raw H2' : h2,
      'Ethanol' : enol,
      'Pressure[hPa]' : P,
      'PM1.0' : pm1,
      'PM2.5' : pm2_5,
      'NC0.5' : nc0_5,
      'NC1.0' : nc1,
      'NC2.5' : nc2_5,
      'CNT' : cnt}

    r = requests.post(URL, json=param)
    if r.status_code == 200:
        res = r.json()
        st.title('Fire Alarm is {}'.format(res['label_names']))
    else:
        st.title("Unexpected Error")
        st.write(r.status_code)