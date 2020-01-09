"""
Name: Jordan Belinsky
Assignment: 4
Module: Main Program
"""

# Import modules
from counting_quad_sorts import *
from collect_function_performance_data import *
from file_chooser import *
from file_column_averages import *
from menu import *
from plotter import *

# Main menu
main_title = "Main Menu"
main_choices = ["Generate sort times files", "Plot average sort times"]

# Generate menu
generate_title = "Select a Sort"
generate_choices = ["Bubble sort", "Insertion sort", "Optimized bubble sort", "Selection sort"]

# Plot menu
plot_title = "Choose a File"

# Declare testing variables
MAX_N = 100
NUM_TESTS = 100

# Main program functionality
def main():

    # Establish the main menu UI
    main_select = do_menu(main_title, main_choices)
    
    # Generating test data for the user-selected sort
    if main_select == 1:
        generate_select = do_menu(generate_title, generate_choices)

        # Bubble sort
        if generate_select == 1:
            test_function(bubble_sort, MAX_N, NUM_TESTS)
            main()

        # Insertion sort
        if generate_select == 2:
            test_function(insertion_sort, MAX_N, NUM_TESTS)
            main()

        # Optimized bubble sort
        if generate_select == 3:
            test_function(optimized_bubble_sort, MAX_N, NUM_TESTS)
            main()

        # Selection sort
        if generate_select == 4:
            test_function(selection_sort, MAX_N, NUM_TESTS)
            main()

        # Exit
        if generate_select == None:
            main()
    
    # Visually plotting the test data for the user-selected sort
    if main_select == 2:
        
        # Read files
        file_path = get_file_path_and_name(pattern="*.txt")
        try:
            averages = get_file_column_averages(file_path[1])
        except:
            main()

        # Define graph parameters
        graph = plot(title=str(file_path[1]), origin_x=15, origin_y=15, scale_x=6, scale_y=0.11, bg="aquamarine")
        graph["draw_axes"](tick_length=4, tick_interval_y=100)
        graph["draw_axes"]()

        # Plot sorting algorithm points
        for x in range(len(averages)):
            graph["plot_point"](x, averages[x], diam=6, colour="red")

        # Plot worst-case function
        graph["plot_function"](lambda x: (x**2)/2, colour='navy', point_diam=3)

        # Plot formatting
        graph["put_text"]("Legend:", x=60, y=750, colour="black", size=20)
        graph["put_text"](u"T(n) = n\u00B2/2", x=60, y=550, colour="blue", size=20)
        graph["put_text"]("T(n) = "+str(file_path[1][:(len(file_path[1])-4)]), x=60, y=350, colour="red", size=20)
        graph["block"]()
        main()

# Execute the main program
main()