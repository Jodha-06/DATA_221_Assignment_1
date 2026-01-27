import pandas as pd

Data_for_the_Data_Frame = {
    "A":[1,2,2,1],
    "B":[3.1,4.2,1.5,6.3],
    "C":[800,150,400,210]
}

Final_Data_Frame = pd.DataFrame(Data_for_the_Data_Frame)

Final_Data_Frame["D"] = Final_Data_Frame["A"]*Final_Data_Frame["B"]

print(Final_Data_Frame)