import streamlit as st
import numpy as np

st.title('BMI計算ツール')

height = st.number_input('身長(cm)', value=160)
weight = st.number_input('体重(kg)', value=50)

bmi = np.round(weight / height / height * 10000, 1)

if st.button('BMIを計算'):
    st.write(f'あなたのBMIは{bmi}です')
    if bmi < 18.5:
        st.write('あなたはBMIが標準より低い、「やせ」の状態です')
    elif bmi >= 25:
        st.write('あなたはBMIが標準より高い、「肥満」の状態です')
    else:
        st.write('あなたのBMIは標準です')
