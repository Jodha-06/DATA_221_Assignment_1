def Convert_Seconds_Since_Midnight_Into_Readable_Time(Seconds_Since_Midnight):
    # Check for valid input range ( There are 86400 seconds in a day)
    if Seconds_Since_Midnight < 0 or Seconds_Since_Midnight >86400:
        return "Invalid Input. Input must be between 0 and 86399"

    # Calculate hours
    Hour_Value_in_Result = Seconds_Since_Midnight // 3600
    Remaining_Seconds_Value = Seconds_Since_Midnight % 3600

    # Calculate minutes and seconds
    Minute_Value_in_Result = Remaining_Seconds_Value // 60
    Final_Seconds_Value = Remaining_Seconds_Value % 60

    #Determine AM or PM
    if Hour_Value_in_Result >= 12:
        Period_of_the_Day = 'PM'
    else:
        Period_of_the_Day = 'AM'

    #Convert final time to 12 hour format
    if Hour_Value_in_Result == 0:
        Hour_Value_in_Result = 12
    elif Hour_Value_in_Result > 12:
        Hour_Value_in_Result = Hour_Value_in_Result - 12

    return f"{Hour_Value_in_Result}:{Minute_Value_in_Result}:{Final_Seconds_Value}:{Period_of_the_Day}"

#Test Case
Final_Time = Convert_Seconds_Since_Midnight_Into_Readable_Time(74280)
print(Final_Time)