def String_Analysis_Dictionary(List_of_Strings):
    Final_Analysis_Dictionary = {}

    for Current_String in List_of_Strings:
        Current_String_Length = len(Current_String)

        if Current_String_Length % 2 == 0:
            Parity_Value = "even"
        else:
            Parity_Value = "odd"

        Final_Analysis_Dictionary[Current_String]={
            "length": Current_String_Length,
            "parity": Parity_Value
        }

    return Final_Analysis_Dictionary

Sample_List_of_Inputs= ["data", "science", "university", "code"]
Outputs_Dictionary = String_Analysis_Dictionary(Sample_List_of_Inputs)

print("{")

for Current_Key in Outputs_Dictionary:
    Current_Value = Outputs_Dictionary[Current_Key]
    print(f"{Current_Key}: {Current_Value},")


print("}")