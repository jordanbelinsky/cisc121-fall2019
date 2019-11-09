"""
This module is used for building the classifier, which sets up the data models
and runs through the data to determine average attributes based on the data.
"""

def build_classifier(data):
    """
    This function pulls the given data and runs through it in order to evaluate points for each attribute
    within the data model. It then averages the attributes and returns a list for each data model respectively.

    Parameters:
        data: the set of data to run through for evaluation

        Returns: two lists which represent the <=50K and <>50K data models' attribute averages
    """
    # Data Model (<=50K) defined by making a dictionary for each data model entry type
    less_age = 0
    less_work_class = {"Private":0, "Self-emp-not-inc":0, "Self-emp-inc":0, \
        "Federal-gov":0, "Local-gov":0, "State-gov":0, "Without-pay":0, \
        "Never-worked":0}
    less_education_num = 0
    less_marital_status = {"Married-civ-spouse":0, "Divorced":0, "Never-married":0, \
        "Separated":0, "Widowed":0, "Married-spouse-absent":0, \
        "Married-AF-spouse":0}
    less_occupation = {"Tech-support":0, "Craft-repair":0, "Other-service":0, \
        "Sales":0, "Exec-managerial":0, "Prof-specialty":0, \
        "Handlers-cleaners":0, "Machine-op-inspct":0, "Adm-clerical":0, \
        "Farming-fishing":0, "Transport-moving":0, "Priv-house-serv":0, \
        "Protective-serv":0, "Armed-Forces":0}
    less_relationship = {"Wife":0, "Own-child":0, "Husband":0, "Not-in-family":0, \
        "Other-relative":0, "Unmarried":0}
    less_race = {"White":0, "Asian-Pac-Islander":0, "Amer-Indian-Eskimo":0, \
        "Other":0, "Black":0}
    less_sex = {"Female":0, "Male":0}
    less_capital_gain = 0
    less_capital_loss = 0
    less_hours_per_week = 0
    less_count = 0

    # Data Model (>50K) defined by making a dictionary for each data model entry type
    greater_age = 0
    greater_work_class = {"Private":0, "Self-emp-not-inc":0, "Self-emp-inc":0, \
        "Federal-gov":0, "Local-gov":0, "State-gov":0, "Without-pay":0, \
        "Never-worked":0}
    greater_education_num = 0
    greater_marital_status = {"Married-civ-spouse":0, "Divorced":0, "Never-married":0, \
        "Separated":0, "Widowed":0, "Married-spouse-absent":0, \
        "Married-AF-spouse":0}
    greater_occupation = {"Tech-support":0, "Craft-repair":0, "Other-service":0, \
        "Sales":0, "Exec-managerial":0, "Prof-specialty":0, \
        "Handlers-cleaners":0, "Machine-op-inspct":0, "Adm-clerical":0, \
        "Farming-fishing":0, "Transport-moving":0, "Priv-house-serv":0, \
        "Protective-serv":0, "Armed-Forces":0}
    greater_relationship = {"Wife":0, "Own-child":0, "Husband":0, "Not-in-family":0, \
        "Other-relative":0, "Unmarried":0}
    greater_race = {"White":0, "Asian-Pac-Islander":0, "Amer-Indian-Eskimo":0, \
        "Other":0, "Black":0}
    greater_sex = {"Female":0, "Male":0}
    greater_capital_gain = 0
    greater_capital_loss = 0
    greater_hours_per_week = 0
    greater_count = 0

    # For loop to go through the data file
    for i in range(len(data)):

        # Check for class >50K, add a point to the attrubute value
        if data[i]["class"] == ">50K":
            greater_age += data[i]["age"]
            greater_work_class[data[i]["workclass"]] += 1
            greater_education_num += data[i]["educationnum"]
            greater_marital_status[data[i]["marital"]] += 1
            greater_occupation[data[i]["occupation"]] += 1
            greater_relationship[data[i]["relationship"]] += 1
            greater_race[data[i]["race"]] += 1
            greater_sex[data[i]["sex"]] += 1
            greater_capital_gain += data[i]["capitalgain"]
            greater_capital_loss += data[i]["capitalloss"]
            greater_hours_per_week += data[i]["hours"]
            greater_count += 1

        # Check for class <=50K, add a point to the attrubute value
        elif data[i]["class"] == "<=50K":
            less_age += data[i]["age"]
            less_work_class[data[i]["workclass"]] += 1
            less_education_num += data[i]["educationnum"]
            less_marital_status[data[i]["marital"]] += 1
            less_occupation[data[i]["occupation"]] += 1
            less_relationship[data[i]["relationship"]] += 1
            less_race[data[i]["race"]] += 1
            less_sex[data[i]["sex"]] += 1
            less_capital_gain += data[i]["capitalgain"]
            less_capital_loss += data[i]["capitalloss"]
            less_hours_per_week += data[i]["hours"]
            less_count += 1

    # Calculate averages for >50K
    greater_age /= greater_count
    greater_education_num /= greater_count
    greater_capital_gain /= greater_count
    greater_capital_loss /= greater_count
    greater_hours_per_week /= greater_count

    # Run through the dictionary to calculate the average for each attribute
    for attribute in greater_work_class:
        greater_work_class[attribute] /= greater_count
    for attribute in greater_marital_status:
        greater_marital_status[attribute] /= greater_count
    for attribute in greater_occupation:
        greater_occupation[attribute] /= greater_count
    for attribute in greater_relationship:
        greater_relationship[attribute] /= greater_count
    for attribute in greater_race:
        greater_race[attribute] /= greater_count
    for attribute in greater_sex:
        greater_sex[attribute] /= greater_count
    
    # Calculate averages for <=50K
    less_age /= less_count
    less_education_num /= less_count
    less_capital_gain /= less_count
    less_capital_loss /= less_count
    less_hours_per_week /= less_count

    # Run through the dictionary to calculate the average for each attribute
    for attribute in less_work_class:
        less_work_class[attribute] /= less_count
    for attribute in less_marital_status:
        less_marital_status[attribute] /= less_count
    for attribute in less_occupation:
        less_occupation[attribute] /= less_count
    for attribute in less_relationship:
        less_relationship[attribute] /= less_count
    for attribute in less_race:
        less_race[attribute] /= less_count
    for attribute in less_sex:
        less_sex[attribute] /= less_count

    # Create lists to return
    greater_list = [greater_age, greater_work_class, greater_education_num, \
        greater_marital_status, greater_occupation, greater_relationship, \
        greater_race, greater_sex, greater_capital_gain, greater_capital_loss, \
        greater_hours_per_week]

    less_list = [less_age, less_work_class, less_education_num, \
        less_marital_status, less_occupation, less_relationship, \
        less_race, less_sex, less_capital_gain, less_capital_loss, \
        less_hours_per_week]

    return greater_list, less_list

