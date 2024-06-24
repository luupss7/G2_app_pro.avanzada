import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
airbnb_data = pd.read_csv("2a_Dataset_Disposicion_final_de_RRSS_V2.0.csv",sep=';' , encoding='latin-1')

st.title('Disposicion de residuos solidos')

# Diccionario con la información de los archivos
archivos_excel = {
    "Encuesta 1": {"file": "2a_Dataset_Disposicion_final_de_RRSS_V2.0.", "count_column": 'P506', "df_column_name": 'DEPARTAMENTO'},
    "Encuesta 2": {"file": "2a_Dataset_Disposicion_final_de_RRSS_V2.0.", "count_column": 'P506', "df_column_name": 'PROVINCIA'},
    "Encuesta 3": {"file": "2a_Dataset_Disposicion_final_de_RRSS_V2.0.", "count_column": 'P506', "df_column_name": 'DISPOSICION'},
}    

print(airbnb_data)