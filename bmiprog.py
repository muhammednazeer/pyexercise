test = " "
while test != "quit":
    test = input("Press Enter or any key to continue (or 'quit' to exit): ")
    if test == "quit":
        print ("...Exiting program.......")
    else:
        weight = float(input("Enter your weight in Kilograms: "))
        height = float(input("Enter your height in meters: "))
        bmi = (weight * 703)/height**2
        print ("You entered: {0}, weight and {1} height, your bmi is {2}".format(weight, height, bmi)) 
        if bmi < 18.5:
            print ("Underweight")
        elif bmi < 25:
            print ("Normal")
        elif bmi >= 25:
            print ("Overwight")
        else:
            print ("Enter a valid parameta")
