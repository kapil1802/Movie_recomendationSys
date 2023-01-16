import streamlit as st
import pickle
import pandas as pd
import requests


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies 


similarity = pickle.load(open('similarity.pkl','rb'))
movies = pickle.load(open('movies.pkl','rb'))
movies_title = movies['title'] 


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which Movie would you like to see?',
    movies_title)



if st.button('Recommend'): 
    output = recommend(selected_movie_name) 
    # st.write('Top Recomendations>')
    for i in output:
        st.write(i)
