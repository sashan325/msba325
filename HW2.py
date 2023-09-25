import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px

st.title ('MSBA 325 Assignment 2')

st.subheader('Passport Power 🌎')

st.write('The following table represents the passport power of all the countries in the world in 2023 in addition to their coordinates:')
passport_power = pd.read_csv('https://raw.githubusercontent.com/sashan325/msba325/main/passport_power.csv', encoding='latin1')
passport_power
st.write('The following map represents the countries by their respective passport power rank globally. As the 2023 Rank slider is moved, the countries with the respective ranking will be shown on the map:')


Rank = st.slider('Select 2023 Rank', min_value=1, max_value=110, value=1)

# Filter data based on the selected rank
filtered_data = passport_power[passport_power['2023 Rank'] == Rank]

# Display the filtered data
st.write(f'Data for selected rank ({Rank}):')
st.map(filtered_data)

st.subheader('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
st.subheader('Countries Life Expectancy 🌐')

countries = pd.read_csv('https://raw.githubusercontent.com/sashan325/msba325/main/countries.csv', encoding='latin1')
chart_data=pd.DataFrame(countries)
st.write('The following table represents different indicators for certain countries in the world:')
chart_data

st.write('The following Box Plot Chart shows the Life Expectancy per Continent:')
   
# Assuming you've already loaded your countries dataframe

# Get unique continents for the dropdown
continents = ['All'] + list(countries['Continent'].unique())

# Create a dropdown in Streamlit and store the selected value in the variable 'selected_continent'
selected_continent = st.selectbox('Select a continent:', options=continents)

# Check the selected value. If it's "All", don't filter. Otherwise, filter the dataframe.
if selected_continent == 'All':
    data_to_plot = countries
else:
    data_to_plot = countries[countries['Continent'] == selected_continent]

# Draw boxplot for the relevant data
if selected_continent == 'All':
    fig = px.box(data_to_plot, x='Continent', y='Life Expectancy', title=f'Life Expectancy per Continent')
else:
    fig = px.box(data_to_plot, x='Continent', y='Life Expectancy', title=f'Life Expectancy in {selected_continent}')

st.plotly_chart(fig)
