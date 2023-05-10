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

def introduction():
    
    st.markdown(
        "According to the study, about 64.5% of Filipinos have saved or set aside money in the past year, whether using an account at a financial institution, mobile money account, savings club for any reason. In East Asia and Pacific region, Philippines ranked 4th for the highest % of people with savings and ranked 1st in the lower-middle income group in the region.")
    # Partition the page into 2
    col1, col2 = st.columns(2)


    # Display metric in column 1
    col1.metric(
        label='Filipinos with savings',
        value=str('64.50%')
    )

    # Display metric in column 1
    col2.metric(
        value=str('Rank 1'), label='versus neighboring countries in the Low Middle income group of East Asia & Pacific Region'
        )


    st.subheader(
        """.....but are we really doing great?"""
        )

    st.markdown(
        """According to the study, specifically in the low-income group, majority of the population have no savings hence the negative variance. In the graph, there is a trend that highlights that as one moves up the economic ladder, the gap between with and without savings increases. This shows that an increase in gap signifies that there are more Filipinos with savings versus without. 
        """
        )

    
    st.subheader("""Are savings only for the rich?""")

    st.markdown(
        """More than half of low-income Filipinos and almost half of the middle class have no savings. 
    """
    )

    st.markdown(
        """More than half of low-income Filipinos and almost half of the middle class have no savings. 
    """
    )
    

    st.subheader("""Why are Filipinos not saving enough?""")
    st.markdown(
        """Filipinos cannot save mainly due to lack of money and expensive fees of maintaining a savings account. 
    """
    )

       #INSERT GRAPH
    
    st.subheader("""
    INSERT GRAPH HERE
    """)


    st.markdown(
        """The inability of Filipinos to maintain a savings account can be attributed to various factors, with the most common ones being insufficient funds and high account maintenance fees. 
            Many Filipinos, specifically for the low-income group, struggle to make ends meet, and as a result, they may find it challenging to set aside money for savings.
            Moreover, some banks may require a minimum deposit amount to open and maintain a savings account, which can be a considerable challenge for many Filipinos. As a result, many Filipinos may opt not to open or maintain a savings account, leaving them without a reliable means of saving money. Overall, a combination of financial constraints, high fees, and low financial literacy may contribute to the insufficient savings of many Filipinos.
        """
    )

 
introduction()