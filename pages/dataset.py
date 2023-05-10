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

def future():
    
    # Write the title
    st.title(
        "Majority of Filipinos have not saved for Old Age"
    )
    st.markdown(
        "**58.4%** of Filipinos have not set aside money for Old Age in the past year."
    )

    ##################################################

    st.markdown(
        """
        While this figure may seem discouraging, it is worth noting that a significant portion of the population was able to save for old age, \
        especially when compared to several other countries in the East Asia & Pacific (excluding high income) region, such as Cambodia, Mongolia, Lao PDR, Indonesia \
        and Myanmar, where less than a third of the population saved for old age, the percentage of savers in the Philippines (41.6%) is relatively high. \
        In terms of those who saved in the past year, **the Philippines still ranked third in the region**, behind Malaysia (54.8%) and Thailand (55.6%), which had higher percentages.
        """
    )

future()
