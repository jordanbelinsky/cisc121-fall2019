"""
Name: Jordan Belinsky
Assignment: 4
Module: File Column Averages
"""

from ast import literal_eval

def get_file_column_averages(filename):
    """
    This function calculates the average of each column in a data set from a file

    Parameters: filename (string)

    Returns: a list of each column's average
    """
    # Declare variables and read file
    data = open(filename, "r")
    data_list = []
    data_str = data.read().strip()
    line_data = data_str.split("\n")
    rows = 0

    # Create list from csv file
    for line in line_data:
        row = literal_eval(line) # Solution found from stack overflow: https://stackoverflow.com/questions/29552950/when-to-use-ast-literal-eval
        rows += 1
        data_list.append(row)

    # Calculate the sum of each column
    col_sums = []
    for row in range(len(data_list)):
        for col in range(len(data_list[row])):
            try:
                col_sums[col] += data_list[row][col]
            except:
                col_sums.append(data_list[row][col])

    # Calculate the average of each column from sum/count
    averages = []
    for i in range(len(col_sums)):
        averages.append(col_sums[i]/rows)

    return averages
    

if __name__ == "__main__":
    filename = "test.txt"
    test = get_file_column_averages(filename)
    print(test)