import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title('Gupo 2: Trabajo final')

file_path = '/mnt/data/2a Dataset Disposicion final de RRSS_V2.0 edit.csv'
data = pd.read_csv(file_path)

print(data.head())
plt.figure(figsize=(10, 6))
plt.bar(data['departamenos'], data['DISPOSICION_FINAL_ADECUADA'], color='blue')
plt.xlabel('Departamentos')
plt.ylabel('Disposición Final Adecuada')
plt.title('Disposición Final Adecuada por Departamento')
plt.xticks(rotation=90) 
plt.tight_layout()  
plt.show()

data = pd.read_csv(file_path, encoding='latin1')
print(data.head())

