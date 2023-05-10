from st_pages import add_indentation
add_indentation()

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st
#add in libraries
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

sns.set()

def emergencies():
    # Write the title
    st.title(
        "Filipinos find it difficult to prepare for emergencies"
    )
    
    #add col for revised emergency funds source

    
    # Partition the page into 2
    col1, col2 = st.columns(2)


    # Display metric in column 1
    col1.metric(
        label='% with difficulty in getting emergency funds within 30 days',
        value=str('80.2%')
    )

    # Display metric in column 1
    col2.metric(
        label='% with difficulty in getting emergency funds within 7 days',
        value=str('85.5%')
    )

    st.markdown(
        "Filipinos that find it **very difficult** to get emergency funds increase by **13.8%** as the timeline is shortened from 30 to 7 days."
       
    )

emergencies()

