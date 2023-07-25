import pickle



#loading Nmf model
with open('nmf_recommender.pkl', 'rb') as file:  # This "with open" mimic is a so-called "context manager".
    nmf_model = pickle.load(file)


