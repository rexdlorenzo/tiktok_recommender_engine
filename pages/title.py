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

def title():
    # Write the title and the subheader
    st.title("Going Viral: Using Data Science to Promote Filipino Music on TikTok"
    )
    st.subheader(
        """
        A data Driven Approach
        """
    )
    st.subheader(
        """
        A project by Martel, Ben, Zee, and Rex of DSF11 Eskwelabs
        """
    )

    # Load photo
    st.image("streamlit-photo-1.jpeg")


    # Display data
    st.markdown("**The Data**")
    st.markdown("Source: Global Findex 2021 from World Bank.")

title()