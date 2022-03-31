# model deployment using all in one method

import streamlit as st
import pickle
import pandas as pd

with open("pipe.pkl", "rb") as model_file:
    model = pickle.load(model_file)

columns=['Species', 'Length1', 'Length2', 'Length3','Height','Width']


st.title("Aplikasi Prediksi Berat ikan dalam gram")
Length1 = st.number_input("Panjang vertikal dalam cm")
Length2 = st.number_input("Panjang diagonal dalam cm")
Length3 = st.number_input("Panjang silang dalam cm")
Height = st.number_input("Tinggi dalam cm")
Width = st.number_input("Lebar silang dalam cm")
Species = st.selectbox("Species", ['Smelt', 'Parkki','Roach','Bream','Perch','Pike','Whitefish'])

# inference
new_data = [Species, Length1, Length2, Length3, Height, Width]
new_data = pd.DataFrame([new_data], columns=columns)
res = model.predict(new_data)
st.title([res[0]])