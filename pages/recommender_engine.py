from st_pages import add_indentation
import streamlit as st
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import joblib
from sklearn.metrics.pairwise import euclidean_distances, manhattan_distances, cosine_similarity

st.set_page_config(layout="wide")
add_indentation()

def recommender_engine():
    
    st.header("TIKTOK Recommender engine")

    st.image("images/recommender_engine1.png")
    st.image("images/recommender_engine2.png")
    
    st.markdown(
        """
        We developed a recommender engine tool that underground and rising Philippine artists can use for their music. 

        With the top 5 tiktok playlists we have extracted from before, we will be feeding that to the Machine Model we have created. 

        Once fed, we will be able to generate seed tracks per genre, which is what our recommender engine will use to detect which of the artist's songs are the best to promote on tiktok. 
        """
    )
#####################################################
    client_id = st.secrets.cred.client_id
    client_secret = st.secrets.cred.client_secret
    redirect_uri = st.secrets.cred.redirect_uri
    username = st.secrets.cred.username
    
    scope_playlist = 'playlist-modify-public'
    scope_user = 'user-library-modify'

    def create_spotify():
        auth_manager = SpotifyOAuth(
            scope=[scope_user, scope_playlist],
            username=username,
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret= client_secret)

        sp = spotipy.Spotify(auth_manager = auth_manager)
    
        return auth_manager, sp
    
    def refresh_spotify(auth_manager, spotify):
        token_info = auth_manager.cache_handler.get_cached_token()
        if auth_manager.is_token_expired(token_info):
            auth_manager, spotify = create_spotify()
        return auth_manager, spotify

        
    inp, res = st.columns(2)

    auth_manager, sp = create_spotify()

    with inp.form(key='my_form', clear_on_submit=True):
        album_input = st.text_input(label='Enter Album')
        artist_input = st.text_input(label='Enter Artist/Band')
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.write(f'You entered: {album_input} and {artist_input}')
            auth_manager, sp = refresh_spotify(auth_manager, sp)
            results = sp.search(q='album:{} artist:{}'.format(album_input, artist_input), type='album')
            items = results["albums"]["items"]
            
            #if album is not found
            if len(items) == 0:
                st.subheader("Artist and/or album was not found!")
            else:
                album = items[0]
                album_id = album["id"]
                album_data = sp.album_tracks(album_id)
                album_tracks = album_data["items"]
                audio_features_dict = {}
                track_list_df = pd.DataFrame([{'track_id': track['id'], 'track_name': track['name']} for track in album_tracks])
                for track in album_tracks:
                    try:
                        # Get track ID
                        track_id = track['id']
                       
                        # Get track audio features
                        audio_features = sp.audio_features(track_id)[0]

                        # Add track audio features to dictionary
                        audio_features_dict[track['name']] = {
                            'danceability': audio_features['danceability'],
                            'energy': audio_features['energy'],
                            'key': audio_features['key'],
                            'loudness': audio_features['loudness'],
                            'mode': audio_features['mode'],
                            'speechiness': audio_features['speechiness'],
                            'acousticness': audio_features['acousticness'],
                            'instrumentalness': audio_features['instrumentalness'],
                            'liveness': audio_features['liveness'],
                            'valence': audio_features['valence'],
                            'tempo': audio_features['tempo']
                        }
                    except:
                        st.subheader(f"No audio features found for track '{track['name']}'")
                the_df = pd.DataFrame(audio_features_dict)
                the_df = the_df.T
                st.subheader("Here are the tracks in the album:")
                for i in the_df.index:
                    st.write(i)

                res.info("Here are the recommended songs to use in TikTok per genre:")
                seed_track_data = pd.read_csv('seed_tracks_list.csv')

                genre_lookup = {0: 'EDM', 1: 'hip-hop', 2: 'indie', 3: 'pop', 4: 'r&b'}
                pipeline = joblib.load('RF_V1_genre_classifier.pkl')
                feature_cols = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', \
                                'liveness', 'valence', 'tempo']
                the_df['predicted_genre_id'] = pipeline.predict(the_df[feature_cols])
                the_df['predicted_genre'] = the_df['predicted_genre_id'].map(genre_lookup)
                the_df['genre_probabilities'] = pipeline.predict_proba(the_df[feature_cols]).tolist()
                the_df['predicted_genre_proba'] = the_df['genre_probabilities'].apply(lambda x: max(x))
                genre_cols = [f'genre_{genre}_proba' for genre in genre_lookup.values()]
                the_df[genre_cols] = the_df['genre_probabilities'].apply(pd.Series)
                the_df = the_df.drop(columns=['genre_probabilities'])  # drop column with probability list

                hiphop_seed_track_data = seed_track_data[seed_track_data['predicted_genre'] == "hip-hop"].iloc[0]
                EDM_seed_track_data = seed_track_data[seed_track_data['predicted_genre'] == "EDM"].iloc[0]
                indie_seed_track_data = seed_track_data[seed_track_data['predicted_genre'] == "indie"].iloc[0]
                pop_seed_track_data = seed_track_data[seed_track_data['predicted_genre'] == "pop"].iloc[0]
                rnb_seed_track_data = seed_track_data[seed_track_data['predicted_genre'] == "r&b"].iloc[0]

                genre_proba_cols = [col for col in the_df.columns if col.startswith('genre_')]

                def get_distances(x, y):
                    euclidean_dist = euclidean_distances(x.values.reshape(1, -1), y.values.reshape(1, -1)).flatten()[0]
                    manhattan_dist = manhattan_distances(x.values.reshape(1, -1), y.values.reshape(1, -1)).flatten()[0]
                    cosine_dist = 1 - cosine_similarity(x.values.reshape(1, -1), y.values.reshape(1, -1)).flatten()[0]
                    return [euclidean_dist, manhattan_dist, cosine_dist]

                #HIPHOP
                the_df['all_distances_features'] = the_df.apply(lambda x: get_distances(x[feature_cols], \
                                                                                        hiphop_seed_track_data[feature_cols]),
                                                                axis=1)
                dist_feature_cols = ['euclidean_dist_features', 'manhattan_dist_features', 'cosine_dist_features']
                the_df[dist_feature_cols] = the_df['all_distances_features'].apply(pd.Series)
                hiphop_recommendation_df = the_df['euclidean_dist_features'].sort_values(ascending=True)
                res.write(f"Recommended Track for Hip-Hop: {hiphop_recommendation_df.index[0]}")

                #EDM
                the_df['all_distances_features'] = the_df.apply(lambda x: get_distances(x[feature_cols], \
                                                                                        EDM_seed_track_data[feature_cols]), axis=1)
                dist_feature_cols = ['euclidean_dist_features', 'manhattan_dist_features', 'cosine_dist_features']
                the_df[dist_feature_cols] = the_df['all_distances_features'].apply(pd.Series)
                EDM_recommendation_df = the_df['euclidean_dist_features'].sort_values(ascending=True)
                res.write(f"Recommended Track for EDM: {EDM_recommendation_df.index[0]}")

                #INDIE
                the_df['all_distances_features'] = the_df.apply(lambda x: get_distances(x[feature_cols], \
                                                                                        indie_seed_track_data[feature_cols]),
                                                                axis=1)
                dist_feature_cols = ['euclidean_dist_features', 'manhattan_dist_features', 'cosine_dist_features']
                the_df[dist_feature_cols] = the_df['all_distances_features'].apply(pd.Series)
                indie_recommendation_df = the_df['euclidean_dist_features'].sort_values(ascending=True)
                res.write(f"Recommended Track for Indie: {indie_recommendation_df.index[0]}")

                #POP
                the_df['all_distances_features'] = the_df.apply(lambda x: get_distances(x[feature_cols], \
                                                                                        pop_seed_track_data[feature_cols]), axis=1)
                dist_feature_cols = ['euclidean_dist_features', 'manhattan_dist_features', 'cosine_dist_features']
                the_df[dist_feature_cols] = the_df['all_distances_features'].apply(pd.Series)
                pop_recommendation_df = the_df['euclidean_dist_features'].sort_values(ascending=True)
                res.write(f"Recommended Track for Pop: {pop_recommendation_df.index[0]}")

                #R&B
                the_df['all_distances_features'] = the_df.apply(lambda x: get_distances(x[feature_cols], \
                                                                                        rnb_seed_track_data[feature_cols]), axis=1)
                dist_feature_cols = ['euclidean_dist_features', 'manhattan_dist_features', 'cosine_dist_features']
                the_df[dist_feature_cols] = the_df['all_distances_features'].apply(pd.Series)
                rnb_recommendation_df = the_df['euclidean_dist_features'].sort_values(ascending=True)
                res.write(f"Recommended Track for R&B: {rnb_recommendation_df.index[0]}")
                recommended_list = list(set([hiphop_recommendation_df.index[0], EDM_recommendation_df.index[0], indie_recommendation_df.index[0], pop_recommendation_df.index[0], rnb_recommendation_df.index[0]]))
                filtered_track_list_df = track_list_df[track_list_df['track_name'].isin(recommended_list)]
                track_ids_list = list(filtered_track_list_df.sort_values(by='track_name', key=lambda x: x.map({v: i for i, v in enumerate(recommended_list)}))['track_id'])
                new_playlist_name = f"Top tiktokable tracks from the album {album_input} by {artist_input}"
                new_playlist = sp.user_playlist_create(username, name = new_playlist_name)
                playlist_id = new_playlist['id']
                sp.user_playlist_add_tracks(username, playlist_id, track_ids_list)
                href = f"https://open.spotify.com/playlist/{playlist_id}"
                res.write(f"Spotify playlist: [{new_playlist_name}](%s)" % href)
def artist1():
    st.header("TIKTOK Recommender engine: Sample Output 1 - Upbeat Album")
    st.image("images/bgyo.png")
    st.markdown(
        """
        Okay, so this is how our streamlit recommender engine looks like.  So basically it has two parts.

        Looking at your left side, we ask users to input their album and artist name.
        
        Then on the lower right side, 5 songs will be recommended along with their recommended genre once you hit submit.

        For our presentation, we decided with 2 artist, for the first it would BGYO and their album Be Us to represent upbeat music. For the next one it would be clara benin, and indie, acoustic singer to represent slow songs.

        The reason why we chose these artist is because we understand that music can quite varied, however upon our experience, upbeat and slow songs are usually the type of music we hear on tiktok. 

        Looking at the results of BGYO, the songs recommended seem quite accurate with their music.

        For EDM, PNGNP was recommended. It is fitting because in their album it is the song that has the most electronic beats.

        And for the track extraordinary, it was resulted for both indie and pop. First, it is pop because it is very upbeat. And, It is also Indie because, some of the lines of this song is sung like an indie song. 

        And the fact that extra-ordinary appeared twice despite that there are other songs, means our algorithm is really vying for this song.
        """
    )

def artist2():
    st.header("TIKTOK Recommender engine: Sample Output 2 - Slow Album")
    st.image("images/clara_benin.png")
    st.markdown(
        """
        Similarly, we decided to test our engine with a slow, album like clara benin's, human eyes.

        As we look to the lower right side we can see the results.

        We can see that kingdom come is generated for indie, as it has the a very indie, guiatary, and pop feel.

        Then for EDM, although clara benin is generally an indie artist, blameless is one of the tracks in her album that uses percussion, which is why it is suggested for EDM.

        """
    )

recommender_engine()
artist1()
artist2()
