days = {"Mo": "Monday", "Tu": "Tuesday", "We": "Wednesday", "Th": "Thursday",
        "Fr": "Friday", "Sa": "Saturday", "Su": "Sunday"}
for day in days.items():
    for eachitem in day:
        print (eachitem, end = ",  ")
value = input("The abbr. of day: ")
if value in days.values():
    print(value, " is a day in the week\n")

kanoCentral = ["Kano Municipal", "Tarauni", "Kumbotso", "Gwale", "Nasarawa", "Dala",
               "Fagge", "Ungogo"]
kanoNorth = ["Dawakin Tofa", "Tofa", "Rimi-Gado", "Gabasawa", "Gezewa", "Munijibir",
             "Bagwai", "Dambatta", "Makoda", "Shanono", "Kunchi", "Tsanyaisa",
             "Gwarzo", "Bichi", "Karaye", "Rogo", "Kabo"]
kanoSouth = ["Takai", "Wudil", "Sumaila", "Bebeji", "Rano", "Bunkure", "Kibiya",
             "Warawa", "Ajingi", "Garko", "Tudun Wada", "Doguisa", "Madobi", "Kura",
             "Garun Mallam", "Dawakin Kudu", "Kiru", "Gaya", "Albasu"]
local = "" #Initializing 
while local != "quit": 
    local = input("Enter LGA name(or 'quit' to exit: ")
    if local == "quit": #checking the user input to determine if the program will run or exit
        print ("...exiting the Program")
    else:  #Main program block
        local_sen = local.title()
        if local_sen in kanoCentral:
            print ("You entered ", local_sen, " it is in Kano Central Senatorial District")
        elif local_sen in kanoNorth:
            print ("You entered ", local_sen, " it is in Kano North Senatorial District")
        elif local_sen in kanoSouth:
            print ("You entered ", local_sen, " it is in Kano South Senatorial District")
        else:
            print ("You entered ", local_sen, " \n Not a Local Government in Kano State.")
