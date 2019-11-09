"""
Name: Jordan Belinsky
Assignment: 3B
Module: Navigation
"""

def movie_search(movies, query):
    """
    This function displays all movies based on an inputted search query
    from the user.

    Parameters: movies (list)
                query (string)

    Returns: a list of relevant movies and their details
    """
    # Define list and ordered list number
    search_list = []
    num = 1

    for i in range(len(movies)):
        if query.lower() in movies[i][0].lower():
            # Add applicable results to a list
            search_list.append(movies[i])

            # Print the list in ordered list format (1./2./3.)
            print(str(num)+"."+movies[i][0])
            num += 1

    return search_list

def movie_details(details):
    """
    This function processes a movie's details and prints them when a user
    selects the movie from a search.

    Parameters: details (list)

    Returns: None
    """
    # Define indexes
    title = details[0]
    year = details[3]
    length = details[2]
    rating = details[1]
    genre_list = details[4:]

    # Define genres
    genre_indexes = []
    genres = []
    genre_types = ["Action", "Adventure", "Animation", "Biography", "Comedy",\
                    "Documentary", "Drama", "Family", "Fantasy", "History",\
                    "Horror", "Musical", "Mystery", "Reality TV", "Romance",\
                    "Science Fiction", "Thriller", "War", "Western"]

    # Track genre indexes for the movie
    for i in range(len(genre_list)):
        if genre_list[i] == "1":
            genre_indexes.append(i)
    
    # Create a list of applicable genres
    for i in range(len(genre_indexes)):
        genres.append(genre_types[genre_indexes[i]])

    # Print output
    print("Movie Details:")
    print("Title:", title)
    print("Year:", year)
    print("Length:", length)
    print("Rating:", rating)
    print("Genres:", genres)

if __name__ == "__main__":
    # Testing
    movies = [["Avatar", 9.5], ["Endgame", 10.0]]
    query = "end"
    movie_search(movies, query)

    details = ["The Red Skeleton Show",7.3,420,2012,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    movie_details(details)