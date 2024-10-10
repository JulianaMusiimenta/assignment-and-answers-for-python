def calculateGrades():

    print("\n...student Grade calculations...")

    #capture student mark
    mark = int(input('Enter mark scored:\t'))

    #testing student mark
    if mark>=90 and mark<=100:
        print("Grade is A")

    elif mark>=80 and mark<=89:
        print("Grade is B")

    elif mark>=70 and mark<=79:
        print("Grade is C")

    elif mark>=60 and mark<=69:
        print("Grade is D")

    elif mark>=50 and mark<=59:
        print("Grade is E")

    else:
        print("Fail")

        # call the function
calculateGrades()