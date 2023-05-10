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
    st.title("GOING VIRAL: USING DATA SCIENCE TO PROMOTE FILIPINO MUSIC ON TIKTOK"
    )
    st.subheader(
        """
        A Data Driven Approach
        """
    )
    st.subheader(
        """
        COHORT 11 SPRINT 3 GROUP BRMZ-RADIO
        """
    )

    st.subheader(
        """
        Prepared by:
        Ben Estera,
        Martel Espiritu,
        Zee Halagao,
        Rex Lorenzo
        """
    )

title()