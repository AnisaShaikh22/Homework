def calculateLetterGrade():
    mid1 = int(input("Please enter midterm 1 grade \n"))
    while mid1<0 or mid1> 100:
        print("The grade of midterm 1 should be between 0 and 100. Please enter the proper grade")
        mid1 = int(input("Please enter midterm 1 grade \n"))

    mid2 = int(input("Please enter midterm 2 grade \n"))
    while mid2<0 or mid2> 100:
        print("The grade of midterm 2 should be between 0 and 100. Please enter the proper grade")
        mid2 = int(input("Please enter midterm 2 grade \n"))

    final = int(input("Please enter final grade \n"))
    while final<0 or final> 100:
        print("The grade of final should be between 0 and 100. Please enter the proper grade")
        final = int(input("Please enter final grade \n"))

    totalGrade = 0.3*mid1 + 0.3*mid2 + 0.4*final

    if totalGrade>= 90:
        print(str(totalGrade)+ " --> AA")

    elif totalGrade>= 85:
        print(str(totalGrade)+ " --> BA")

    elif totalGrade>= 75:
        print(str(totalGrade)+ " --> BB")

    elif totalGrade>= 65:
        print(str(totalGrade)+ " --> CB")

    elif totalGrade>= 50:
        print(str(totalGrade)+ " --> CC")

    else:
        print("Ufortunately you are failed!")


# Test
calculateLetterGrade()
