"""
Name: Jordan Belinsky
Assignment: 3B
Module: Recommender
"""

import random

def top_genres(watchlist):
    """
    This function finds the top 2 genres of movies that
    the user watched.

    Parameters: watchlist (list)

    Returns: a list of the genres
    """
    # Define lists and dictionary
    genre_list = []
    genre_indexes =  []
    genre_types = ["Action", "Adventure", "Animation", "Biography", "Comedy",\
                    "Documentary", "Drama", "Family", "Fantasy", "History",\
                    "Horror", "Musical", "Mystery", "Reality TV", "Romance",\
                    "Science Fiction", "Thriller", "War", "Western"]
    genre_dict = {"Action": 0, "Adventure": 0, "Animation": 0, "Biography": 0, \
                    "Comedy": 0, "Documentary": 0, "Drama": 0, "Family": 0, \
                    "Fantasy": 0, "History": 0, "Horror": 0, "Musical": 0, \
                    "Mystery": 0, "Reality TV": 0, "Romance": 0, "Science Fiction": 0, \
                    "Thriller": 0, "War": 0, "Western": 0}

    # Separate genre indexes from each movie listing
    for i in range(len(watchlist)):
        genre_list.append(watchlist[i][4:])

    # Add a to the dictionary value for each genre as it is watched
    for i in range(len(genre_list)):
        for j in range(len(genre_list[i])):
            if genre_list[i][j] == "1":
                genre_dict[genre_types[j]] += 1

    # Sort the dictionary by genre value (descending)
    sorted_genres = sorted(genre_dict.items(), key=lambda x: x[1], reverse=True)

    # Choose the top two genres from the sorted list
    top_two = [sorted_genres[0][0], sorted_genres[1][0]]
    
    top_two_index = []
    for i in range(len(top_two)):
        for j in range(len(genre_types)):
            if top_two[i] == genre_types[j]:
                top_two_index.append(j)

    return top_two_index
    
def recommend(movies, watchlist):
    """
    This function recommends 10 movies based upon the user's
    top watched genre.

    Parameters: movies (list)
                watchlist (list)

    Returns: None
    """
    # Define lists
    genres = top_genres(watchlist)
    genre_index = genres[0]
    relevant = []
    recommendations = []
    
    # Find all relevant movies based on genre
    for i in range(len(movies)):
        if movies[i][genre_index+4] == '1':
            relevant.append(movies[i])

    # Randomly select 10 movies from the relevant list
    for i in range(10):
        recommendations.append(random.choice(relevant))

    # Display 10 movies in ordered list format
    num = 1
    for i in range(len(recommendations)):
        print(str(num)+". "+recommendations[i][0])
        num += 1
