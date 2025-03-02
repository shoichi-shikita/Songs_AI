import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

mock_tracks = pd.DataFrame([
    {"title": "Song 1", "danceability": 0.8, "energy": 0.7, "valence": 0.6},
    {"title": "Song 2", "danceability": 0.6, "energy": 0.9, "valence": 0.7},
    {"title": "Song 3", "danceability": 0.9, "energy": 0.8, "valence": 0.5},
])

st.title("🎵 Spotify Music Analysis")

st.write("🎭 **楽曲のノリやすさ・エネルギー感・感情的特徴**")
fig, ax = plt.subplots()
mock_tracks.set_index("title").plot(kind="bar", ax=ax)
st.pyplot(fig)