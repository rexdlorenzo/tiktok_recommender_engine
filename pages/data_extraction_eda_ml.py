from st_pages import add_indentation
import streamlit as st

add_indentation()

def data_extraction():
    
    # Write the title
    st.header("Data Extraction")
    st.image("images/data_extraction.png")

    st.markdown(
        """
        For our data extraction process, we used the Spotipy module for Python to access the Spotify Web API. We extracted the top 5 most popular TikTok playlists, each with over 430,000 likes. After combining these playlists, we removed any duplicate tracks.

        Next, we extracted the top 5 most popular playlists for each of our chosen genres, all with at least 100,000 likes. We also combined these playlists and removed any duplicates.

        Finally, we removed any tracks from the genre playlists that were also found in the TikTok playlists and stored them in 2 separate CSV files.
        """
    )

def eda():
    st.header("Exploratory Data Analysis (EDA)")
    st.image("images/eda1.png")
    st.image("images/eda2.png")
    st.markdown(
        """
        Our Exploratory Data Analysis of popular tracks on TikTok found results that may align with common beliefs about what makes them successful on the app.

        First, most of the popular tiktok tracks are also popular on Spotify. 

        Next, these tracks also tend to be more danceable than not. 

        Additionally, popular tracks on TikTok usually have higher energy scores. Energy is a measure of intensity and activity. Energetic songs typically feel fast-paced, loud, and full of noise.
        """
    )
    st.markdown(
        """
        Our EDA also shows that majority of the popular tiktok tracks are not acoustic, which makes sense considering which genres are common among these tracks, like EDM, hip-hop, pop, and r&b.  The exception to this trend is the Indie genre, since Indie music is most likely to have acoustic elements.

        Finally, our analysis showed that most popular TikTok tracks contain vocal content as indicated by their very low instrumentalness scores. Only a few tracks have high instrumentalness, suggesting that they are likely to be instrumental.
        """
    )

def ml():
    st.header("Machine Learning")
    st.image("images/ml.png")
    st.markdown(
    """
    Now for our machine learning modeling:

    We selected 9 audio features, including danceability, energy, acousticness, and instrumentalness. All of them are numerical. We tried adding other features like the key, mode, and time signature but they did not improve the performance. Removing any of the 9 features also reduced the performance of the model so we kept these 9 as our features.

    Our target variable  is the genre, encoded as numbers from 0 to 4.   Our model is used to predict the genre of tiktok tracks, where tracks with the highest percentage confidence for each class are used as the seed tracks for recommending which songs in an artist's album have the potential of becoming popular on Tiktok PH.

    We scaled the features using MinMaxScaler then run the data through tree-like classifiers such a random forest  and xgboost. We chose these type of classifiers for their strong ability to provide explainable results.
    """
    )

data_extraction()
eda()
ml()
