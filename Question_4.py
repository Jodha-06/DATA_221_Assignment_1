from random import random

#Generate a list of 20 random values
Random_Values = [random() for i in range(20)]
# Generate a random value of x
Value_of_X = random()
# Sort the list
Random_Values.sort()
# Variable used to store the first matching index
First_Matching_Index = None
# Loop through the sorted list in order to find the first value that is >= x
for index in range(len(Random_Values)):
    if Random_Values[index] >= Value_of_X:
        First_Matching_Index = index
        break

# Print the sorted list and the value of x
print(f"Sorted List: {Random_Values}")
print(f"The Value of x is: {Value_of_X}")

# Print the result
if First_Matching_Index is not None:
    print(f"The first index in which the value is greater than or equal to x is: {First_Matching_Index}")
else:
    print("There is no value in the list which is greater than or equal to x")
