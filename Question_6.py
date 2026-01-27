def Distribution_Analysis_of_Numbers(List_of_Numbers):
    Dictionary_of_Numbers = {}
    Total_Elements_in_List = len(List_of_Numbers)

    List_of_Unique_Values = []

    for Individual_Numbers in List_of_Numbers:
        if Individual_Numbers not in List_of_Unique_Values:
            List_of_Unique_Values.append(Individual_Numbers)

    List_of_Unique_Values.sort()

    for Key_Values in List_of_Unique_Values:
        Less_Than_or_Equal_to = 0

        for Individual_Numbers in List_of_Numbers:
            if Individual_Numbers <= Key_Values:
                Less_Than_or_Equal_to += 1

        Percentage = round((Less_Than_or_Equal_to / Total_Elements_in_List) * 100,2)
        Dictionary_of_Numbers[Key_Values] = Percentage

    return Dictionary_of_Numbers


List_of_Numbers = [3,1,2,3,4,2]
Final_Result = Distribution_Analysis_of_Numbers(List_of_Numbers)
print(Final_Result)

