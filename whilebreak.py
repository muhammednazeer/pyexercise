while True:
    text = input ("Enter a chemical formular (or quit to exit): ")
    if text == "quit":
        print ("...exiting program")
        print ("Thanks for using the program")
        break
    elif text == "H2O":
        print (text, " is Water!")
    elif text == "NH3":
        print (text, " is Amonia!")
    elif text == "CH4":
        print (text, " is Methane!")
    else:
        print ("Enter a valid compound name")
