import pandas as pd
import pickle
import streamlit as st
import requests
import random


df = pd.DataFrame(pickle.load(open("movie_dict.pkl", "rb")))
similarity = pickle.load(open("similarity.pkl", "rb"))


API_KEY = "ca8ed1de0cdd3e9c4f5c844902ce6a10"


def fetch_poster(movie_title):
    base_url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": API_KEY, "query": movie_title}
    response = requests.get(base_url, params=params).json()

    if response.get("results"):
        poster_path = response["results"][0].get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return "https://via.placeholder.com/500x750?text=No+Image" 

def recommend(movie=None, selected_genre="All"):
    recommended_movies = []
    recommended_posters = []

    if movie:  
        movie_index = df[df["title"] == movie].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:20]

        for i in movie_list:
            title = df.iloc[i[0]].title
            genres = df.iloc[i[0]].genres  

            if selected_genre == "All" or selected_genre in genres:
                poster_url = fetch_poster(title)
                recommended_movies.append(title)
                recommended_posters.append(poster_url)

            if len(recommended_movies) == 5:
                break
    else:  
        filtered_df = df if selected_genre == "All" else df[df["genres"].apply(lambda x: selected_genre in x)]
        sampled_movies = filtered_df.sample(n=min(5, len(filtered_df)), random_state=random.randint(1, 100))  

        for _, row in sampled_movies.iterrows():
            recommended_movies.append(row["title"])
            recommended_posters.append(fetch_poster(row["title"]))

    return recommended_movies, recommended_posters


st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #141e30, #243b55);
        color: white;
    }
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #ff6600;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #dddddd;
    }
    .movie-container {
        text-align: center;
        padding: 10px;
    }
    .movie-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 15px;
        transition: transform 0.2s ease-in-out;
    }
    .movie-box:hover {
        transform: scale(1.05);
        background-color: rgba(255, 255, 255, 0.2);
    }
    .movie-poster {
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown('<h1 class="title">🍿Movie Recommendation System </h1>', unsafe_allow_html=True)
st.markdown('<h6 class="subtitle">Find the best movies based on your choice!</h4>', unsafe_allow_html=True)


all_genres = ["All"] + sorted(set([genre for sublist in df["genres"] for genre in sublist]))
selected_genre = st.sidebar.selectbox("🎭 Filter by Genre", all_genres)


if "last_genre" not in st.session_state or st.session_state.last_genre != selected_genre:
    st.session_state.selected_movie = ""  
    st.session_state.last_genre = selected_genre  


selected_movie = st.selectbox("🎥 Choose a movie (or leave empty for genre-based recommendations):", 
                              [""] + list(df["title"].values), index=0, key="selected_movie")


if st.button("🎯 Recommend"):
    movies_list, posters_list = recommend(selected_movie if selected_movie else None, selected_genre)

    if not movies_list:
        st.warning(f"No recommendations found in the {selected_genre} genre.")
    else:
        st.subheader("🔍 Recommended Movies:")
        cols = st.columns(5)

        for idx, (movie, poster) in enumerate(zip(movies_list, posters_list)):
            with cols[idx]:  
                st.markdown(
                    f"""
                    <div class="movie-container">
                        <div class="movie-box">
                            <img class="movie-poster" src="{poster}" width="100%">
                            <p><b>{movie}</b></p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
