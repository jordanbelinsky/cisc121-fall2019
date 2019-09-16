"""
This module provides functions that return the Air Quality Health Index (as
calculated for Canada) and corresponding Risk level based on external input.

Functions:

aqhi (o3, no2, pm25)
    Returns the Air Quality Health Index (AQHI) associated with these
    parameters: ozone , nitrougen dioxide, and fine particulate matter.

risk_level (aqhi)
    Returns a string representing the Risk level (low, moderate, high, or
    very high) associated with aqhi, a number representing an Air Quality
    Health Index.

R. Linley
2019-08-30
"""

import math

def calc_aqhi (o3, no2, pm25):
    """
    Returns the Air Quality Health Index (AQHI) associated with these
    parameters: ozone , nitrougen dioxide, and fine particulate matter.

    Arguments:

    o3 - A number representing a three-hour average concentration of
        ground-level ozone, measured in parts per billion (ppb).

    no2 - A number representing a three-hour average concentration of
        nitrogen dioxide, measured in ppb.

    pm25 - A number representing a three-hour average concentration of fine
        (2.5 micrometres or less diameter) particulate matter, measured in
        micrograms per cubic metre.

    Calculation source:
    https://en.wikipedia.org/wiki/Air_Quality_Health_Index_(Canada)#Calculation
    """
    result = (1000/10.4)*((math.exp(0.000537*o3)-1)+\
        (math.exp(0.000871*no2)-1)+(math.exp(0.000487*pm25)-1))
    rounded_result = round(result)
    if result < 1:
        return 1
    return rounded_result

def risk_level (aqhi):
    """
    Returns a string representing the Risk level (low, moderate, high, or
    very high) associated with aqhi, a number representing an Air Quality
    Health Index.
    """
    if aqhi >= 1 and aqhi <= 3:
        return "low"
    elif aqhi >= 4 and aqhi <= 6:
        return "moderate"
    elif aqhi >= 7 and aqhi <= 9:
        return "high"
    elif aqhi >= 10:
        return "very high"


if __name__ == '__main__':
    for i in range(60):
        val = calc_aqhi(i, i, i)
        print (i, val, '(' + risk_level(val) + ')')