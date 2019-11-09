"""
Name: Jordan Belinsky
Assignment: 3B
Module: User Interface
"""

def main_menu():
    """
    This function consolidates main menu options into a singular function.

    Parameters: None

    Returns: None
    """
    print("\n\nJetflix Menu:")
    print("1. Search for a movie by title.")
    print("2. Show the top 10 highest rated movies.")
    print("3. Show the shortest, longest, and average length of all movies.")
    print("4. Reccommend a movie based on your viewing history.")
    print("5. Exit to desktop.\n")

def watch(movie_data, watchlist):
    """
    This function marks a movie as watched, moving it to the user's watchlist.

    Parameters: movie_data (list)
                watchlist (list)

    Returns: None
    """
    # Prompt to watch movie once selected in search
    play = input("Would you like to watch this? (y/n): ")

    # Add to watchlist and print confirmation for user
    if play.lower() == "y":
        watchlist.append(movie_data)
        print("\nMovie playing. Added "+str(movie_data[0])+" to your watchlist.\n")
    
    # Return to application main menu
    if play.lower() == "n":
        print("\nReturning to main menu.\n")

if __name__ == "__main__":
    # Testing
    movie_data = ["The Red Skeleton Show",7.3,420,2012,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    watchlist = [] 
    watch(movie_data, watchlist)