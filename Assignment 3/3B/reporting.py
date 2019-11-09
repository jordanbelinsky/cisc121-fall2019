"""
Name: Jordan Belinsky
Assignment: 3B
Module: Reporting
"""

def sort_by_name(movies):
    """
    This function sorts the movie database according to the rating index - [1].

    Parameters: movies (list)

    Returns: a list of all movies sorted by rating
    """
    length = len(movies)
    for i in range(length):
        for j in range(0, length-i-1):
            if (movies[j][1] > movies[j+1][1]):
                rating = movies[j]
                movies[j] = movies[j+1]
                movies[j+1] = rating
    movies.pop(len(movies)-1)
    return movies

def top_10_rating(movies):
    """
    This function generates a list of the top 10 rated movies in the database.

    Parameters: movies (list)

    Returns: None
    """
    movies = sort_by_name(movies)
    listings = []
    num = 1
    for i in range(len(movies)-10, len(movies)):
        listings.append(movies[i])
    listings.reverse()
    for i in range(len(listings)):
        print(str(num)+". "+listings[i][0]+" - "+listings[i][1])
        num += 1

def lengths(movies):
    """
    This function generates a report detailing the longest, shortest, and average
    movie length.

    Parameters: movies (list)

    Returns: None
    """
    # Sort movies by length
    listings = []
    for i in range(1,len(movies)):
        listings.append([int(movies[i][2]), movies[i][0]])
    listings.sort()
    length_sum = 0
    length_average = 0

    # Shortest movie
    for i in range(1):
        print("Shortest Movie: "+str(listings[i][1])+"- "+str(listings[i][0]))

    # Longest movie
    for i in range(len(listings)-1, len(listings)):
        print("Longest Movie: "+str(listings[i][1])+"- "+str(listings[i][0]))

    # Average length
    for i in range(len(listings)):
        length_sum += listings[i][0]
    length_average = length_sum/len(listings)
    print("Average Length: "+str(round(length_average)))
