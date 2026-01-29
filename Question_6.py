def Distribution_Analysis_of_Numbers(List_of_Numbers):
    # Dictionary to store final results
    Dictionary_of_Numbers = {}
    # Total number of elements in a given list
    Total_Elements_in_List = len(List_of_Numbers)

    # List to store unique values
    List_of_Unique_Values = []

    # Find unique values from the list
    for Individual_Numbers in List_of_Numbers:
        if Individual_Numbers not in List_of_Unique_Values:
            List_of_Unique_Values.append(Individual_Numbers)

    #Sort the unique values
    List_of_Unique_Values.sort()

    #Calculate percentage for each unique value
    for Key_Values in List_of_Unique_Values:
        Less_Than_or_Equal_to = 0

        for Individual_Numbers in List_of_Numbers:
            if Individual_Numbers <= Key_Values:
                Less_Than_or_Equal_to += 1

        Percentage = round((Less_Than_or_Equal_to / Total_Elements_in_List) * 100,2)
        Dictionary_of_Numbers[Key_Values] = Percentage

    return Dictionary_of_Numbers

# Test Case
List_of_Numbers = [3,1,2,3,4,2]
Final_Result = Distribution_Analysis_of_Numbers(List_of_Numbers)
print(Final_Result)

