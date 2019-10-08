import flask
from flask import render_template, request
app = flask.Flask(__name__)
app.config["DEBUG"]= True

@app.route('/')
def a():
    return render_template("project2.html")

@app.route('/submit',methods=['GET'])
def home():
     user = request.args.get('movie')
     #option=request.form['options']
     #print(user)
     import pandas as pd
     import numpy as np
     from sklearn.feature_extraction.text import CountVectorizer
     from sklearn.metrics.pairwise import cosine_similarity
     ###### helper functions. Use them when needed #######
     def get_title_from_index(index):
         return df[df.index == index]["title"].values[0]

     def get_index_from_title(title):
         return df[df.title == title]["index"].values[0]




     df = pd.read_csv("https://raw.githubusercontent.com/codeheroku/Introduction-to-Machine-Learning/master/Building%20a%20Movie%20Recommendation%20Engine/movie_dataset.csv")
     # print df.column
     ##Step 2: Select Features

     features = ['keywords', 'cast', 'genres', 'director']
     ##Step 3: Create a column in DF which combines all selected features
     for feature in features:
         df[feature] = df[feature].fillna('')
     def combine_features(row):
         try:
             return row['keywords'] + " " + row['cast'] + " " + row["genres"] + " " + row["director"]
         except:
             print("Error:", row)

     df["combined_features"] = df.apply(combine_features, axis=1)


         #df["combined_features"] = df.apply(combine_features,axis=1)

     # print "Combined Features:", df["combined_features"].head()

     ##Step 4: Create count matrix from this new combined column
     cv = CountVectorizer()

     count_matrix = cv.fit_transform(df["combined_features"])

     ##Step 5: Compute the Cosine Similarity based on the count_matrix
     cosine_sim = cosine_similarity(count_matrix)
     movie_user_likes = user
     #df[feature] = df[feature].fillna('')


     ## Step 6: Get index of this movie from its title
     movie_index = get_index_from_title(movie_user_likes)

     similar_movies = list(enumerate(cosine_sim[movie_index]))

     ## Step 7: Get a list of similar movies in descending order of similarity score
     sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True)[1:]
     b=[]
     ## Step 8: Print titles of first 50 movies
     i = 0
     for j in sorted_similar_movies:
         a=get_title_from_index(j[0])
         #print(a)
         #return '%s'%a
         b.append(a)
         i = i + 1
         if i > 3:
             break
     #print(b)


     return 'Similar movies are: %s' %b

if __name__ == '__main__':
     app.run()
     #action=/submit method=get