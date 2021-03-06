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
    df['Financial: Gross Income'] = np.ceil(df['Financial: Gross Income'])

    return df

data = load_data()

# Create Financial HeatMap dataset
fin_heat = data[['lng', 'lat', 'Financial: Gross Income']].groupby(['lng']).mean().reset_index()
fin_heat['Financial: Gross Income'] = np.ceil(fin_heat['Financial: Gross Income']/10000)
fin_heat = fin_heat.loc[fin_heat.index.repeat(fin_heat['Financial: Gross Income'])]

purposes = sorted(list(data.Purpose.str.split(' ', expand=True).stack().unique()))
for word in list(purposes):  # iterating on a copy since removing will mess things up
    if word in ['/', '', ' ']:
        purposes.remove(word)

# ADD FILTERS TO THE SIDEBAR
purpose_filter = st.sidebar.multiselect(
    "Filter by Charitable Purpose",
    purposes
)

counties = sorted(data['Benefact_county'].unique())
county_filter = st.sidebar.multiselect(
    "Filter by Irish County",
    counties
)

size_filter = st.sidebar.multiselect(
    "Filter by Charity Size",
    data['Report Size'].unique()
)

num_vols = ['None', '1-9', '10-19', '20-49', '50-249', '250-499', '500-999', '1000-4999', '5000+']
volunteers_filter = st.sidebar.multiselect(
    "Filter by Number of Volunteers",
    num_vols
)

# FILTERING DATA BY SIDEBAR CHOICES
for i in purpose_filter:
    data = data[data.Purpose.str.contains(i)]

for i in county_filter:
    data = data[data.Benefact_county.str.contains(i)]

for i in size_filter:
    data = data[data['Report Size'].str.contains(i)]

for i in volunteers_filter:
    if(i == '1-9'):
        i = '01-Sep'
    elif(i == '10-19'):
        i = 'Oct-19'
    data = data[data['Number of Volunteers'].str.contains(i)]


# CHART LAYOUT
row2_1, row2_2 = st.beta_columns((2,2))

# Define a layer to display on a map
layer = pdk.Layer(
    "HexagonLayer",
    data[['lng', 'lat']],
    get_position=["lng", "lat"],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[100, 3000],
    extruded=True,
    coverage=1,
)

view_state = pdk.ViewState(longitude=-6.6564, latitude=53.6055, zoom=6, min_zoom=5, max_zoom=15, pitch=40.5, bearing=-27.36)

def map(data):
    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={"latitude": 53.6055, "longitude": -6.6564, "zoom": 6, "pitch": 50,},
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data,
                get_position=["lng", "lat"],
                auto_highlight=True,
                elevation_scale=50,
                pickable=True,
                elevation_range=[0, 3000],
                extruded=True,
                coverage=1,
            ),
        ]
    ))

with row2_1:
    st.write("**Number of Charities**")
    map(data[['lng', 'lat']])

with row2_2:
    st.write("**Financial Income**")
    map(fin_heat[["lng", "lat"]])

# FILTERED TABLE LAYOUT
st.write("**Filtered Table of Charities**")
st.table(data[['Registered Charity Name', 'Period Start Date', 'Period End Date', 'Financial: Gross Income', 'Financial: Gross Expenditure']])