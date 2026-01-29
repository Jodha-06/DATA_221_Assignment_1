# Store the initial threshold value
Product_Threshold_Value = 100
# Initialize the Current Product Value to 1
Accumulated_Product_Value = 1
# Start multiplying from 1
Current_Multiplier = 1

#Continue multiplying until the product becomes larger than the threshold value
while Accumulated_Product_Value <= Product_Threshold_Value:
    Current_Multiplier += 1
    Accumulated_Product_Value *= Current_Multiplier

#print the final product
print(f"The final product is: {Accumulated_Product_Value}")
#print the integer that caused the product to exceed the threshold
print(f"The integer that cause the product to exceed the given threshold value is: {Current_Multiplier}")
