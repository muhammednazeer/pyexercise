''' This program calculate the heating effect of electricity
         
The program accept 3 parameta via Current in amp,
  Resistance in ohms, Time in Minutes.'''


#Preamble text declaration

welcome = '''              Welcome to Program that Calculate
             the heating effect of electricity.

                  Presented by: ALIYU IDRIS M.
 Faculty of Computer Science and Information Technology.\n''' 

intro = '''            HEATING EFFECT OF ELECTRICITY:
    When electric current flows through a conductor, the
    resistance of the conductor changes electrical enerygy
    into heat energy just as friction changes mechanical energy
    into heat.

    It is this heating effect of an electric current that is
    utilized in such devices as electric pressig iron,
    electric toaster, electric coil, hair dryer and incadescent lamps.\n'''

print(welcome)

print(intro)

text = " " # variable to test the user input
while text != "quit":
    text = input("Press any key to continue (or 'quit' to exit): ")
    if text == "quit":   #If the user type quit, the program will exit
        print ("...exiting program\n")
        print ("GOODBYE!")
    else:  # If any key or value is entered apart from quit, the program will continue executing
        print("Enter the parametas in the following order;\n current (i), Resistance(R), Time (S)\n")
        current = float(input("Enter the value of Current in Amp: "))
        resistance = float (input("Enter the value of Resistance in Ohms: "))
        time = float (input("Enter the time in Minutes: "))
        heat = current**2*resistance*(time*60) # convrting time to second before calculation
        print ("The value of current :{0}amp; value of resistance is {1}Ohm and the value of time is{2} minutes".format(current, resistance, time))
        print ("The Heating effect is ", heat/1000, "KJ") #Heating effect will be zero if any of the inputed value is zero
    
        

