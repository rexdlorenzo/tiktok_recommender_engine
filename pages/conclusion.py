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

def conclusion1():
    st.header("Conclusion 1")
    st.image("images/conclusion1.png")
    st.markdown(
        """
        Now moving forward to objective #1: the most prominent features that contribute to suitability on tiktok. 

        So for our 5 genres, pop, hiphop, EDM, r&b , and indie:

        Indie has high instrumentalness, which makes sense since these types of music tend to have acoustic guitar beats.

        For pop music: it has balance to every feature: danceable rhythm, and a positive or uplifting message. 

        For Hip-hop: It's highest is speechiness, which makes sense because hiphop tends to have rap lyrics.

        For electronic dance music or EDM:  it has high-energy beats, because it has drops and a focus on creating a party or club atmosphere.

        For R&B: it typically has energetic tracks which feel fast, loud, and noisy.
        """
    )
def conclusion2():
    st.header("Conclusion 2")
    st.image("images/conclusion2.png")
    st.markdown(
        """
        The ML model we chose is Random Forest. 

        Although XG boost scored higher in precision, recall, and F1, we still decided to choose random forest since it has the highest test score and accuracy. 

        We deemed accuracy is the most important metric because we aim to create a recommender engine and we want to maximize the accuracy of our tool. 
        """
    )
def conclusion3():
    st.header("Conclusion 3")
    st.image("images/conclusion3.png")
    st.markdown(
        """
        For Objective #3: How are we  going to improve the popularity of rising Philippine artists given the data and ML model that we have created?

        So, onto the next slide.
        """
    )

conclusion1()
conclusion2()
conclusion3()