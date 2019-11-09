"""
This module is used for testing the classifier I created with
the test data which was established in the extracting data file.
"""

def test_classifier(data, greater, less):
    """
    This function reads the test data created and compares it with the >50K and <=50K lists created from
    the targetData function. It then determines which class each attribute is closer to, giving a final output
    for accuracy based upon correct and incorrect guesses.

    Parameters: 
        data: the source of the test data to compare to

        greater: the >50K list

        less: the <=50K list

        Returns: print output for correct/incorrect guesses, and overall accuracy (%)
    """

    # Establish variable to track guesses
    correct_guesses = 0

    # Sweep through data entries to find which class the entry is closer to
    for entry in data:
        less_points = 0
        greater_points = 0

        # Run through each attribute in the entry and score whether or not the guess is correct
        for attribute in entry:
            if attribute == "age":
                if (abs(entry[attribute] - less[0]) < \
                    abs(entry[attribute] - greater[0])):
                    less_points += 1
                else:
                    greater_points += 1

            elif attribute == "workclass":
                if (less[1][entry[attribute]] > \
                    greater[1][entry[attribute]]):
                    less_points += 1
                else:
                    greater_points += 1

            elif attribute == "educationnum":
                if (abs(entry[attribute] - less[2]) < \
                    abs(entry[attribute] - greater[2])):
                    less_points += 1
                else:
                    greater_points += 1

            elif attribute == "marital":
                if (less[3][entry[attribute]] > \
                    greater[3][entry[attribute]]):
                    less_points += 1
                else:
                    greater_points += 1

            elif attribute == "occupation":
                if (less[4][entry[attribute]] > \
                    greater[4][entry[attribute]]):
                    less_points += 1
                else:
                    greater_points += 1

            elif attribute == "relationship":
                if (less[5][entry[attribute]] > \
                    greater[5][entry[attribute]]):
                    less_points += 1
                else:
                    greater_points += 1

            elif attribute == "race":
                if (less[6][entry[attribute]] > \
                    greater[6][entry[attribute]]):
                    less_points += 1
                else:
                    greater_points += 1

            elif attribute == "sex":
                if (less[7][entry[attribute]] > \
                    greater[7][entry[attribute]]):
                    less_points += 1
                else:
                    greater_points += 1
            
            elif attribute == "capitalgain":
                if (abs(entry[attribute] - less[8]) < \
                    abs(entry[attribute] - greater[8])):
                    less_points += 1
                else:
                    greater_points += 1

            elif attribute == "capitalloss":
                if (abs(entry[attribute] - less[9]) < \
                    abs(entry[attribute] - greater[9])):
                    less_points += 1
                else:
                    greater_points += 1

            elif attribute == "hours":
                if (abs(entry[attribute] - less[10]) < \
                    abs(entry[attribute] - greater[10])):
                    less_points += 1
                else:
                    greater_points += 1

            else:
                if entry[attribute] == "<=50K":
                    is_less = True
                else:
                    is_less = False

        # Define guesses both correct and incorrect
        guess = True if less_points > greater_points else False
        correct = True if guess == is_less else False

        if correct:
            correct_guesses += 1

    # Calculate the accuracy (%) based upon correct and incorrect guesses
    accuracy = (correct_guesses / len(data)) * 100

    # Correct formatting for output of guesses and accuracy within the main function/module
    print("Correct Guesses: ", correct_guesses)
    print("Incorrect Guesses: ", len(data) - correct_guesses)
    print("Accuracy: "+str(round(accuracy,2))+"%")

            
