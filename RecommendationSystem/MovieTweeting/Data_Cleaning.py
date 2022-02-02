#import libraries
import numpy as np
import pandas as pd
import datetime

print("reading data")
#read data into pandas dataframe
movies = pd.read_csv('movies.dat', delimiter='::', header=None, names=['movie_id', 'movie', 'genre'], dtype={'movie_id': object}, engine='python')
reviews = pd.read_csv('ratings.dat', delimiter='::', header=None, names=['user_id', 'movie_id', 'rating', 'timestamp'], dtype={'movie_id': object, 'user_id': object, 'timestamp': object}, engine='python')

def movies_data_cleaning(movies):
    """
    # pull date if it exists and create a new column 'date'
    #Dummy the date column with 1's and 0's for each century of a movie (1800's, 1900's, and 2000's)
    # Return century of movie as a dummy column
    """
    create_date = lambda val: val[-5:-1] if val[-1] == ')' else np.nan
    movies['date'] = movies['movie'].apply(create_date)

    # a function to split elements in genre
    genres = []
    for val in movies.genre:
        try:
            genres.extend(val.split('|'))
        except AttributeError:
            pass

    genres = set(genres)

    #Creating Dummy variables for year centuries 18's, 19's & 20's "
    def add_movie_year(val):
        if val[:2] == yr:
            return 1
        else:
            return 0

    # Apply function
    for yr in ['18', '19', '20']:
        movies[str(yr) + "00's"] = movies['date'].apply(add_movie_year)

    def split_genres(val):
        try:
            if val.find(g) > -1:
                return 1
            else:
                return 0
        except AttributeError:
            return 0

    for g in genres:
        movies[g] = movies['genre'].apply(split_genres)

    return movies

    #return movies

def reviews_data_cleaning(reviews):
    change_timestamp = lambda val: datetime.datetime.fromtimestamp(int(val)).strftime('%Y-%m-%d %H:%M:%S')

    reviews['date'] = reviews['timestamp'].apply(change_timestamp)
    reviews['month'] = pd.DatetimeIndex(reviews['date']).month
    reviews['year'] = pd.DatetimeIndex(reviews['date']).year
    reviews = pd.get_dummies(reviews, columns = ['month','year'])

    return reviews




def main():

        print("reading movies data into pandas dataframe")
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        movies = pd.read_csv('movies.dat', delimiter='::', header=None, names=['movie_id', 'movie', 'genre'], dtype={'movie_id': object}, engine='python')

        print('cleaning movie data...')
        cleaned_data = movies_data_cleaning(movies)

        print('view first few lines of movie dataframe...')
        print(cleaned_data.head())


        print('movie data set Done')
        print()
        print("Now cleaning reviews dataset")

        reviews = pd.read_csv('ratings.dat', delimiter='::', header=None, names=['user_id', 'movie_id', 'rating', 'timestamp'], dtype={'movie_id': object, 'user_id': object, 'timestamp': object}, engine='python')
        cleaned_data_rev = reviews_data_cleaning(reviews)

        print('view first few lines of reviews dataframe...')
        print(cleaned_data_rev.head())



if __name__ == "__main__":
    main()
