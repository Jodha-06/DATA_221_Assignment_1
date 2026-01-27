from random import random

Random_Values = [random() for i in range(20)]
Value_of_X = random()

Random_Values.sort()
First_Matching_Index = None

for index in range(len(Random_Values)):
    if Random_Values[index] >= Value_of_X:
        First_Matching_Index = index
        break


print(f"Sorted List: {Random_Values}")
print(f"The Value of x is: {Value_of_X}")

if First_Matching_Index is not None:
    print(f"The first index in which the value is greater than or equal to x is: {First_Matching_Index}")
else:
    print("There is no value in the list which is greater than or equal to x")
