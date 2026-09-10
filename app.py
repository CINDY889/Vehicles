
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header("Análisis de anuncios de vehículos")
st.write( "Creación de un histograma para el conjunto de datos de anuncios de ventas de vehículos")

# Botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Distribución del kilometraje de los vehículos')
    fig = px.histogram(car_data, x='odometer', title='Distribución del kilometraje')
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Relación entre el kilometraje y el precio')
    st.plotly_chart(
        px.scatter(car_data, x='odometer', y='price', title='Precio vs. kilometraje'),
        use_container_width=True) 


build_histogram = st.checkbox(
    'Mostrar histograma'
)

if build_histogram:

    fig = px.histogram(
        car_data,
        x='odometer',
        title='Distribución del kilometraje'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


build_scatter = st.checkbox(
    'Mostrar gráfico de dispersión'
)

if build_scatter:

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Precio vs. kilometraje'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

