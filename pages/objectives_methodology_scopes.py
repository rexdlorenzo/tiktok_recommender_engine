from st_pages import add_indentation
import streamlit as st

add_indentation()

def objectives():
    # Write the title
    st.header("Objectives")
    st.image("images/objectives.png")

    st.write("The project has 3 objectives:")
    st.markdown("- Define features or traits of musical compositions that contribute  suitability in Tiktok")
    st.markdown("- Create machine learning model capable of accurately classifying the genre of a song and predicting its success on TikTok based on its musical features")
    st.markdown("- Recommendations for improving the popularity of rising Philippine artists")

    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        list-style-position: inside;
    }
    </style>
    ''', unsafe_allow_html=True)

def methodology():
    st.header("Methodology")
    st.image("images/methodology.png")

    st.markdown(
        """
        We start the project's pipeline by extracting data from Spotify using their Web API. 

        Next, is we conduct exploratory data analysis to gain insights and identify patterns in the data. 

        Then, we build a model to predict the genre of tracks and create seed tracks that match the predicted genre.

        Using this information, we develop a song recommender system that analyzes  user's music preferences and behavior. 

        Finally, we deploy the final product using Streamlit.
        """
    )

def scope_and_limitations():
    st.header("Scopes and Limitations")
    st.image("images/scopes_and_limitations.png")
    st.markdown(
        """
        For the scopes and limitations of our study: 

        We focused on five music genres - Pop, EDM, Hip-Hop, R&B, and Indie - as our general observations showed that these were the most common genres among tracks popular on TikTok in the Philippines.

        We used the top 5 Spotify playlists for each genre, with the number of likes as a basis for how well the tracks represent the genre. 

        For determining which tracks are popular on TikTok, we utilized the top 5 Spotify playlists with names containing the keyword “tiktok”. However, due to rapidly changing trends, our model may need to be updated to reflect future trends.

        Additionally, our recommender engine predicts a single genre for each track. Accurately assigning genres can be challenging as some tracks may incorporate elements from multiple genres. As such, these types of tracks, as well as tracks outside of the 5 genres, may not have accurate results.
        """
    )
objectives()
methodology()
scope_and_limitations()

