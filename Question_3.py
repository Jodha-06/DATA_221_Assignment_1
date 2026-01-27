import math

def Calculate_Power_Function(Base_Number, Exponent_Number):
    Final_Power_Result = pow(Base_Number , Exponent_Number)
    return Final_Power_Result

List_of_Numbered_Pairs = [[5,3],[-1,3],[4,5],[2,0],[6,3],[4,-3]]
List_of_Valid_Results = []

for Base_Number,Exponent_Number in List_of_Numbered_Pairs:
    if Exponent_Number >= 0:
        Current_Power_Result = Calculate_Power_Function(Base_Number, Exponent_Number)
        List_of_Valid_Results.append(Current_Power_Result)


print(List_of_Valid_Results)
