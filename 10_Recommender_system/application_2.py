from flask import Flask,render_template,request
import pickle
from recommenders import recommend_cosin,nmf_recommender
import pandas as pd

my_movie_list = pickle.load(open('../my_movie_list.pkl', 'rb'))
movie_df= pd.read_pickle("movie_df.pkl")
def Convert(lst):
    res_dct = {lst[i]: float(lst[i + 1]) for i in range(1, len(lst), 2)}
    return res_dct


app=Flask(__name__)

@app.route("/")
def landing_page():
   
   return render_template("landing_page.html",full_movie_list=my_movie_list)


@app.route("/recommendation")
def recommendation_page():
   user_query=request.args.to_dict()
   print(user_query)
   new=list(user_query.values())
   model=new[0]
   new_query=Convert(new)
   print(new_query)
   if model=="cosim_model":
        top3=recommend_cosin(new_query)
   else:
       new={}
       for name,rating in new_query.items():
            movie_ids=movie_df.loc[movie_df['title']==name]["movieId"].tolist()
            for movie_id in movie_ids:
                new[movie_id] = rating
       top3=nmf_recommender(new)
   
    
   return render_template("recommender.html",movie_list=top3)

if __name__ == "__main__":
    app.run(debug=True)