def String_Analysis_Dictionary(List_of_Strings):

    #Create the final dictionary
    Final_Analysis_Dictionary = {}

    # Loop through each string that is in the list
    for Current_String in List_of_Strings:
        # Find the length of a selected string
        Current_String_Length = len(Current_String)

        #Determine if the length of the string is even or odd
        if Current_String_Length % 2 == 0:
            Parity_Value = "even"
        else:
            Parity_Value = "odd"

        # Store results in the final dictionary
        Final_Analysis_Dictionary[Current_String]={
            "length": Current_String_Length,
            "parity": Parity_Value
        }

    # Return the final dictionary
    return Final_Analysis_Dictionary

# Sample input list
Sample_List_of_Inputs= ["data", "science", "university", "code"]
Outputs_Dictionary = String_Analysis_Dictionary(Sample_List_of_Inputs)

# Print dictionary in the format outlined in the Assignment description
print("{")

for Current_Key in Outputs_Dictionary:
    Current_Value = Outputs_Dictionary[Current_Key]
    print(f"{Current_Key}: {Current_Value},")


print("}")