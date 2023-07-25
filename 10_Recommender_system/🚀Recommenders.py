"""
Here lives our movie recommenders functions
"""
import pandas as pd
import numpy as np
from utils import nmf_model
from scipy.sparse import csr_matrix
from sklearn.decomposition import NMF
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import pickle
import streamlit as st

#st.number_input("rate movie as 1 to 5",1,5)
# total movie name list
#st.snow()

st.title(":orange[Week 10 & 11 ] " )
st.title(":orange[Recommender system] :rocket:")
st.image("https://images.unsplash.com/photo-1536440136628-849c177e76a1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bW92aWV8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=800&q=60")
st.write("---")
st.subheader("Steps we followed for this project :pencil:")
st.markdown("1. Download data from the MovieLens-dataset")
st.markdown("2. Cleaning & EDA")
st.markdown("3. Recommendation Model:")
st.markdown("   I. NMF Model")
st.markdown("   II. Cosine similarity Model")
st.markdown("4. Flask web interface")
st.markdown("5. Streamlit interface")
st.write("---")

df=pd.read_csv("user_movie_data.csv")
movie_list=df.columns.tolist()

#movie dataframe
with st.expander("See Dataset"):
    movie_df= pd.read_pickle("movie_df.pkl")
    st.subheader("Movie dataframe")
    st.dataframe(movie_df)
    rating=pd.read_csv("ratings.csv")
    st.subheader("Rating Dataframe")
    st.dataframe(rating)







