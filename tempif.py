temp = 1
while temp != 00:
    temp = int(input("Enter temperature value (or 00 to quit: "))
    if temp == 00:
        print ("...exiting program")
    elif temp > 86:
        print ("It's hot!")
    elif temp > 32:
        print ("It's cold!")
    else:
        print ("It's freezing!")

print ("Have a nice day")
