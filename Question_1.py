Product_Threshold_Value = 100

Accumulated_Product_Value = 1
Current_Multiplier = 1


while Accumulated_Product_Value <= Product_Threshold_Value:
    Current_Multiplier += 1
    Accumulated_Product_Value *= Current_Multiplier


print(f"The final product is: {Accumulated_Product_Value}")
print(f"The integer that cause the product to exceed the given threshold value is: {Current_Multiplier}")
