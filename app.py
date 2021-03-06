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

with row1_2:
    st.write(
    """
    ##
    Interactive visualisation of Irish Charity data. 
    Aiming to encourage data-driven charitable contributions and increase awareness of lesser known charities with similar objectives.
    """)

# LOADING THE CLEANED DATASETS
@st.cache(persist=True)
def load_data():
    path = './Data/CleanCSV/big_dataset.csv'
    df = pd.read_csv(path).dropna()
    return df

data = load_data()
print(data.columns)

purposes = list(data.Purpose.str.split(' ', expand=True).stack().unique())
for word in list(purposes):  # iterating on a copy since removing will mess things up
    if word in ['/', '', ' ']:
        purposes.remove(word)

# ADD PURPOSE FILTER TO THE SIDEBAR
purpose_filter = st.sidebar.multiselect(
    "Filter by Charitable Purpose",
    purposes
)

# FILTERING DATA BY A CERTAIN PURPOSE
for i in purpose_filter:
    data = data[data.Purpose.str.contains(i)]


# LAYING OUT THE MIDDLE SECTION OF THE APP 