import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
        
st.header('Análisis de Vehículos US') # encabezado de la app

# CÓDIGO NUEVO (con checkbox)
build_histogram = st.checkbox('Construir un histograma') # crear una casilla de verificación

if build_histogram: # si la casilla está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# CÓDIGO NUEVO (Casilla)
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter: # si la casilla está seleccionada
    st.write('Construir un gráfico de dispersión para las columnas odómetro y precio')
    
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)