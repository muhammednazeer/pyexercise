print ('''         THIS IS A PROGRAM THAT INDICATE THE SENATORIAL DISTRICT
                    IN KANO STATE A LOCAL GOVERNMENT BELONGS TO\n
                                Presented by:\n
                              SHAMSUDEEN DAUDA
             Faculty of Computer Science and Information Technology
                         Bayero University, Kano\n''')
#lIST to hold the local governments in each of the senatorial district
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
            if local_sen == "Kano Municipal": #Testing for Local government in Kano Central
                print ("You entered ", local_sen, " it is in Kano Central Senatorial District")
            elif local_sen == "Tarauni":
                print ("You entered ", local_sen, " it is in Kano Central Senatorial District")
            elif local_sen == "Kumbotso":
                print ("You entered ", local_sen, " it is in Kano Central Senatorial District")
            elif local_sen == "Gwale":
                print ("You entered ", local_sen, " it is in Kano Central Senatorial District")
            elif local_sen == "Nasarawa":
                print ("You entered ", local_sen, " it is in Kano Central Senatorial District")
            elif local_sen == "Dala":
                print ("You entered ", local_sen, " it is in Kano Central Senatorial District")
            elif local_sen == "Fagge":
                print ("You entered ", local_sen, " it is in Kano Central Senatorial District")
            elif local_sen == "Ungogo":
                print ("You entered ", local_sen, " it is in Kano Central Senatorial District")
                #End of Kano Central LGA
        elif local_sen in kanoNorth:   #Kano North LGA block
            if local_sen == "Dawakin Tofa":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Tofa":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Rimi-Gado":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Gabasawa":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Gezewa":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Munijibir":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Bagwai":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Dambatta":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Makoda":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Shanono":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Gezewa":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Kunchi":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")  
            elif local_sen == "Tsanyaisa":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Gwarzo":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Bichi":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Karaye":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Rogo":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
            elif local_sen == "Kabo":
                print ("You entered ", local_sen, " it is in Kano North Senatorial District")
        elif local_sen in kanoSouth:  #Kano south LGA block
            if local_sen == "Takai":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")  
            elif local_sen == "Wudil":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Sumaila":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Bebeji":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Rano":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Bunkure":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Kibiya":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Warawa":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Ajingi":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Garko":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")  
            elif local_sen == "Tudun Wada":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Doguisa":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Madobi":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Kura":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Garun Mallam":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Dawakin Kudu":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Kiru":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Gaya":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
            elif local_sen == "Albasu":
                print ("You entered ", local_sen, " it is in Kano South Senatorial District")
        else:
            print ("Enter a valid Local Government name to know the Senatorial District")
            #Clause to execute if value is not in the list
            
        
