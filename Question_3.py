import math

#Function that computes x to the power y
def Calculate_Power_Function(Base_Number, Exponent_Number):
    Final_Power_Result = pow(Base_Number , Exponent_Number)
    return Final_Power_Result

# Sample list of pairs (base,exponent)
List_of_Numbered_Pairs = [[5,3],[-1,3],[4,5],[2,0],[6,3],[4,-3]]
# List to store valid results
List_of_Valid_Results = []

#Loop through each pair
for Base_Number,Exponent_Number in List_of_Numbered_Pairs:
    # Skip pairs with negative exponents
    if Exponent_Number >= 0:
        Current_Power_Result = Calculate_Power_Function(Base_Number, Exponent_Number)
        List_of_Valid_Results.append(Current_Power_Result)

# Print the final list of valid results
print(List_of_Valid_Results)
