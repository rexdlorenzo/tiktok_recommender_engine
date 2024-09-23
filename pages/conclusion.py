from st_pages import add_indentation
import streamlit as st

add_indentation()

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
        To improve the popularity of rising Philippine artists, we have developed a data-driven approach using a machine learning model. Our recommender engine analyzes an artist’s album listed on Spotify and suggests tracks with the potential to become popular on TikTok. The engine takes into account 5 different genres commonly found among popular TikTok tracks. By leveraging the suggestions provided by our recommender engine and combining them with the artist’s and their team’s expertise, they can strategically promote specific tracks to increase their popularity on TikTok.  
        """
    )

conclusion1()
conclusion2()
conclusion3()