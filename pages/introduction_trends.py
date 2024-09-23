from st_pages import add_indentation
import streamlit as st

add_indentation()

def introduction():
    
    st.header("INTRODUCTION")
    st.image("images/introduction.png")

    st.markdown(
        """
        The project aims to promote rising Philippine artists using TikTok's music discovery and promotion platform.

         By identifying suitable music genres we can increase their visibility and exposure to  the right audiences, leading to more streams and sales on other platforms.
    """
    )
    
def trends():
    st.header("TRENDS")
    st.image("images/trends.png")
    
    st.markdown(
        """
        As you can see on the image above, when a song becomes popular on TikTok through related hashtag, it increases the number of streams on other music services like Spotify.

        Some of the examples are #blindinglightschallenge and #paubayachallenge which gained popularity in 2020 and 2021 respectively.

        """
    )
introduction()
trends()