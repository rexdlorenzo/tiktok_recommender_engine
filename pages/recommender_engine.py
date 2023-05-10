import streamlit as st
import pandas as pd
#from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
#import keyring
import time
import joblib
from sklearn.metrics.pairwise import euclidean_distances, manhattan_distances, cosine_similarity

my_client_id = st.secrets.cred.client_id
my_client_secret = st.secrets.cred.client_secret

client_credentials_manager = SpotifyClientCredentials(client_id=my_client_id,
                                                      client_secret=my_client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

st.set_page_config(layout="wide")
st.title("TIKTOK Recommender engine")

inp, res = st.columns(2)

with inp.form(key='my_form'):
    album_input = st.text_input(label='Enter Album')
    artist_input = st.text_input(label='Enter Artist/Band')
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.write(f'You entered: {album_input} and {artist_input}')
        results = sp.search(q='album:{} artist:{}'.format(album_input, artist_input), type='album')
        items = results["albums"]["items"]

        album = items[0]
        album_id = album["id"]
        album_data = sp.album_tracks(album_id)
        album_tracks = album_data["items"]
        audio_features_dict = {}
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
                print(f"No audio features found for track '{track['name']}'")
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

