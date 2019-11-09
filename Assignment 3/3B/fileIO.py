"""
Name: Jordan Belinsky
Assignment: 3B
Module: File I/O
"""

def read_movies(filename):
    """
    This function reads in the movies data file and initializes the
    data into nested lists of movie information.

    Parameters: filename (string)

    Returns: a nested list containing data entries for each movie/tv show
    """
    # Open file and declare list
    movie_file = open(filename, "r")
    movie_list = []

    # Read line by line, splitting at commas
    for line in movie_file:
        movie_list.append(line.split(","))

    return movie_list

def read_watchlist(user):
    """
    This function reads in the watchlist file and imports the list of movies
    that the user has watched.

    Parameters: user (string)
                watchlist (list)

    Returns: a list of movie data for watched movies
    """
    # Open file and declare list
    try:
        watchlist_file = open(str(user)+"_watchlist.txt", "r")
    except:
        watchlist_file = open(str(user)+"_watchlist.txt", "w+")
    watchlist = []

    # Read line by line, splitting at commas
    for line in watchlist_file:
        watchlist.append(line.split(","))

    return watchlist

def write_watchlist(user, watchlist):
    """
    This function writes to the given user's watchlist file, updating the
    watchlist to reflect which movies have been watched during the current
    session.

    Parameters: user (string)
                watchlist (list)

    Returns: None
    """
    # Open/create watchlist file based on username
    watchlist_file = open(str(user)+"_watchlist.txt", "w")

    # Save names of watched movies to the file
    for i in range(len(watchlist)):
        # watchlist_file.write(str(watchlist[i])+"\n")
        s = ",".join(watchlist[i])
        watchlist_file.write(s)
        
    watchlist_file.close()

if __name__ == "__main__":
    # Testing
    movies = read_movies("movieData.txt")
    
    user = "testUser"
    watchlist = []
    
    watchlist = read_watchlist(user)
    write_watchlist(user, watchlist)
