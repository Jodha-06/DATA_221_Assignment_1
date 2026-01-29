import math

def circleAreaCoverage(Radius_of_Circle_1, Radius_of_Circle_2):

    # Check that both inputs are integers
    if type(Radius_of_Circle_1) != int or  type(Radius_of_Circle_2) != int:
        return "Both radii must be positive integers"

    # Check that both integers are positive
    if Radius_of_Circle_1 <= 0 or Radius_of_Circle_2 <= 0:
        return "Both radii must be positive integers."

    # Calculate the area of each circle
    Area_of_Circle_1 = math.pi * math.pow(Radius_of_Circle_1, 2)
    Area_of_Circle_2 = math.pi * math.pow(Radius_of_Circle_2, 2)

    # If circle 1 is larger, compute the percentage that is covered by circle 2
    if Area_of_Circle_1 > Area_of_Circle_2:
        Percentage_of_Circle_1_Covered = round((Area_of_Circle_2 / Area_of_Circle_1) * 100,2)
        return Percentage_of_Circle_1_Covered

    ## If circle 2 is larger, compute the percentage that is covered by circle 1
    elif Area_of_Circle_2 > Area_of_Circle_1:
        Percentage_of_Circle_2_Covered = round((Area_of_Circle_1 / Area_of_Circle_2) * 100,2)
        return Percentage_of_Circle_2_Covered

    else:
        return 100


#Test cases
print(circleAreaCoverage(3, 5))
print(circleAreaCoverage(5, -2))
print(circleAreaCoverage(7, 5))
print(circleAreaCoverage(-6, 4))
print(circleAreaCoverage(5, 3.0))
print(circleAreaCoverage(4, 4))