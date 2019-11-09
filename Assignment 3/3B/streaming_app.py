"""
Name: Jordan Belinsky
Assignment: 3B
Module: Main Program
"""

# Import modules
from fileIO import *
from navigation import *
from interface import *
from reporting import *
from recommender import *

# Initialize movie database and watchlist
movies = read_movies("movieData.txt")

# Initialize user
user = "testUser"
watchlist = read_watchlist(user)

# Main function
def main():
    main_menu()
    menu_option = int(input("What would you like to do: "))

    # 1. Search function
    if menu_option == 1:
        search = input("\nEnter the movie name: ")
        print("\nMovies containing '"+str(search)+"':")
        search_list = movie_search(movies, search)
        if len(search_list) == 0:
            print("No movies found. Returning to main menu.")
            main()
        details = int(input("Choose a movie (#): "))
        print()
        details_list = search_list[details-1]
        movie_details(details_list)
        print()
        watch(details_list, watchlist)
        main()

    # # 2. Ratings function
    if menu_option == 2:
        print("\nTop 10 Rated Movies Report:")
        top_10_rating(movies)
        main()

    # 3. Lengths function
    if menu_option == 3:
        print("\nLengths Report:")
        lengths(movies)
        main()

    # # 4. Reccomend function
    if menu_option == 4:
        print("\nRecommended Movies Based on Your Top Genres:")
        recommend(movies, watchlist)
        main()

    # 5. Quit function
    if menu_option == 5:
        write_watchlist(user, watchlist)

# Execute main function
main()