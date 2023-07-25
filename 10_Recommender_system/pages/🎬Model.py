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
df=pd.read_csv("user_movie_data.csv")
movie_list=df.columns.tolist()

#movie dataframe
movie_df= pd.read_pickle("movie_df.pkl")



# NMF recommendation function
def nmf_recommender(query:dict,model=nmf_model,k=10)->list:
    
    Q =nmf_model.components_
    # 1. candidate generation
    data = list(query.values())   # the ratings of the new user
    row_ind = [0]*len(data)       # we use just a single row 0 for this user 
    col_ind = list(query.keys())
    
    # construct a user vector
    R_user = csr_matrix((data, (row_ind, col_ind)), shape = (1, Q.shape[1]))
    P_user = model.transform(R_user)
    # Q does not change
    R_recommended = np.dot(P_user, Q)
   
    # 2. scoring
    # convert to a pandas series
    scores = pd.Series(R_recommended[0])
    
    # give a zero score to movies the user has already seen
    scores[query.keys()] = 0
    
    # 3. ranking
    # sort the scores from high to low 
    scores = scores.sort_values(ascending=False)
    

    # filter out movies allready seen by the user
    # get the movieIds of the top 10 entries
    recommendations = scores.head(10).index
    
    # return the top-k highst rated movie ids or titles
    #movies = pd.read_csv('movies.csv')
    top10=movie_df.set_index('movieId').loc[recommendations]['title']
    return top10





# cosin similarity function to find recommendation
def recommend_cosin(query,k=10):
    df=pd.read_csv("user_movie_data.csv")
    df=df.fillna(value=0)
    df.set_index('userId',inplace=True)
    
    # initialize new user 
    new_user=np.zeros_like(df.columns)
    #(To go back to an array if you have a dictionary query)
    
    for index,item in enumerate(df.columns):
        if query.get(item):# <-- Return the value for key if key is in the dictionary
            #change the rating by input data
            new_user[index]=query[item]
    
    # new user dataframe
    new=pd.DataFrame([new_user],index=[len(df)+1],columns=df.columns)
    
    #add new user to df dataframe
    df=pd.concat([df,new],ignore_index=True)
    # We can turn this into a dataframe:
    cosine_sim_table2 = pd.DataFrame(cosine_similarity(df), index=df.index, columns=df.index)
    df2_t=df.T
    # choose an active user
    active_user = len(df)-1
    # create a list of unseen movies for this user
    unseen_movies = list(df2_t.index[df2_t[active_user] == 0])
    # Create a list of top 3 similar user (nearest neighbours)
    neighbours = list(cosine_sim_table2[active_user].sort_values(ascending=False).index[1:4])
    # create the recommendation (predicted/rated movie)
    predicted_ratings_movies = []

    for movie in unseen_movies:
    
        # we check the users who watched the movie
        people_who_have_seen_the_movie = list(df2_t.columns[df2_t.loc[movie] > 0])
    
        num = 0
        den = 0
        for user in neighbours:
            # if this person has seen the movie
            if user in people_who_have_seen_the_movie:
                #  we want extract the ratings and similarities
                rating = df2_t.loc[movie, user]
                similarity = cosine_sim_table2.loc[active_user, user]
            
                # predict the rating based on the (weighted) average ratings of the neighbours
                # sum(ratings)/no.users OR 
                # sum(ratings*similarity)/sum(similarities)
                num = num + rating*similarity
                den = den + similarity
        if den != 0:
            predicted_ratings = num/den
        else:
            predicted_ratings = 0
        predicted_ratings_movies.append([predicted_ratings,movie])
        # create df pred
    df_pred = pd.DataFrame(predicted_ratings_movies,columns = ['rating','movie'])
    recommendation=df_pred.sort_values(by=['rating'],ascending=False)['movie'].head(k)
    recommendation=recommendation
    return recommendation   


st.header("🎬 :orange[Movie Recommender] 🎬")
#st.image("https://i0.wp.com/thecleverprogrammer.com/wp-content/uploads/2020/06/Untitled.jpg?w=1400&ssl=1")
st.image("https://media.istockphoto.com/id/1412871535/photo/friends-watching-movies-together-at-home.webp?b=1&s=170667a&w=0&k=20&c=PPB8Uv-aSvT7gRHXxVWhBWvTZOfnuuob-N117ubcslE=")
# st.image("https://media.istockphoto.com/id/1478374885/photo/joyful-family-watching-movie-in-cinema.webp?b=1&s=170667a&w=0&k=20&c=dZNJ_vVc5AZqcFTbVIpVWQT2ev6sSyOrSxp1coAdAa8=")
st.write("select your favourite movie")
movie1=st.selectbox("Select movie",movie_list[1:],key=1)
rating1=st.selectbox("Rate movie from 1 to 5",[1,2,3,4,5],key=2)

movie2=st.selectbox("Select movie",movie_list[1:],key=3)
rating2=st.selectbox("Rate movie from 1 to 5",[1,2,3,4,5],key=4)

movie3=st.selectbox("Select movie",movie_list[1:],key=5)
rating3=st.selectbox("Rate movie from 1 to 5",[1,2,3,4,5],key=6)

if st.button("submit rating"):
    new_query={
        movie1:rating1,
        movie2:rating2,
        movie3:rating3
    }
    new={}
    for name,rating in new_query.items():
            movie_ids=movie_df.loc[movie_df['title']==name]["movieId"].tolist()
            for movie_id in movie_ids:
                new[movie_id] = rating
    
    st.balloons()
    st.success('Final result is', icon="✅")
    top5= recommend_cosin(new_query)
    st.subheader(":blue[Cosine Similarity Results:]")
    st.write(top5)

    top10=nmf_recommender(new)
    st.subheader(":blue[NMF Result:]")
    st.write(top10)

    





 



