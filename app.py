# Visualising Irish Charity data using Streamlit 

import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import pydeck as pdk 

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

# LAYOUT OF THE TOP SECTION OF THE APP
row1_1, row1_2 = st.beta_columns((2,3))

with row1_1:
    st.title("Charity Visualizer")
    #hour_selected = st.slider("Select hour of pickup", 0, 23)

with row1_2:
    st.write(
    """
    ##
    Interactive visualisation of Irish Charity data. 
    Aiming to encourage data-driven charitable contributions and increase awareness of lesser known charities with similar objectives.
    """)

# LOADING THE CLEANED DATASETS
@st.cache(persist=True)
def load_datasets():
    path = './Data/CleanCSV/'

    df = pd.read_csv(path+'general_data.csv').dropna(subset=['lat', 'lng'])[['lat', 'lng']]
    df2 = pd.read_csv(path+'fin_data.csv')
    df3 = pd.read_csv(path+'general_data.csv').dropna(subset=['lat', 'lng'])
    return df, df2, df3

data, fin_data, gen_data = load_datasets()

# FILTERING DATA BY A CERTAIN PROPERTY
#data = data[data[DATE_TIME].dt.hour == hour_selected]

# LAYING OUT THE MIDDLE SECTION OF THE APP WITH THE MAPS
row2_1, row2_2, row2_3, row2_4 = st.beta_columns((2,1,1,1))

# WRITING THESE LOCATIONS ONTO PAGE 
with row2_1:
    st.write("**Ireland _insert filters**")

with row2_2:
    st.write("**Dublin _insert filters**")

with row2_3:
    st.write("**Cork _insert filters**")

with row2_4:
    st.write("**Galway _insert filters**")