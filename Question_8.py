import pandas as pd

#Dictionary containing the data for the Data Frame
Data_for_the_Data_Frame = {
    "A":[1,2,2,1],
    "B":[3.1,4.2,1.5,6.3],
    "C":[800,150,400,210]
}

# Create the Data Frame using values from the Dictionary
Final_Data_Frame = pd.DataFrame(Data_for_the_Data_Frame)

# Create a new column "D" by multiplying columns "A" and "B"
Final_Data_Frame["D"] = Final_Data_Frame["A"]*Final_Data_Frame["B"]

#Print the final Data Frame
print(Final_Data_Frame)