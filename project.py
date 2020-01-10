''' Program that display the properties of all the transition metals
    developed by MUHAMMED HUSSANI NAZEER, Faculty of Computer Science and
    Information Technology.
    Bayero University, Kano.'''
import datetime
now = datetime.date.today()
print(now)
time = datetime.time()
print(time)

print ('''                                     WELCOME TO 
                  PROPERTIES OF TRANSITION METALS CHEACKER PROGRAM:\n
                                   Developed by:\n
                            MUHAMMED HUSSAINI NAZEER
                      Registration Number: CST/16/COM/00619\n
              FACULTY OF COMPUTER SCIENCE & INFORMATION TECHNOLOGY
                           Bayero University, Kano\n
        **********************************************************************''')
#String holding the general properties of Transition metals

defination = '''
Transition Metals is used as a term in Periodic Chemistry when classifying the
Chemical elements.Each element can usually be classified as a metal or non-metal
based on their general chemical and physical properties.

Transition Metals are any of the metalic elements within Groups 3 to 12 in the
periodic table that have partially filled d orbitals.
Their general electronic configuration is (n – 1)d1-10 ns1-2 where (n – 1)'''

t = input("Press any key to continue: ")
test = t.upper()
if test == " ":
    print()
    print("What is Transition Metal?")
print (defination)
print()

print ('''The following are the general properties of all the transition metals:\n
        Metallic Character
        Atomic radii
        Ionization enthalpy
        Oxidation state
        Magnetic properties
        Catalytic properties
        Formation of coloured compounds
        Formation of complexes''')
prop_collec = ["METALLIC CHARACTER", "ATOMIC RADII", "IONIZATION ENTHALPY",
               "OXIDATION STATE", "MAGNETIC PROPERTIES", "CATALYTIC PROPERTIES",
               "FORMATION OF COLOURED COMPOUNDS", "FORMATION OF COMPLEXES"]

trans_properties = {"METALLIC CHARACTER":''' Metallic character: All transition elements are metallic in nature,
i.e. they have strong metallic bonds. This is because of presence
of unpaired electrons. This gives rise to properties like high density,
high enthalpies of atomization and high melting and boiling points.''',
"ATOMIC RADII":''' Atomic radii: The atomic radii decrease from Sc to Cr because
the effective nuclear charge increases.''',
"IONIZATION ENTHALPY": '''Ionisation enthalpy: There is slight and irregular variation in
ionization energies of transition metals due to irregular variation
of atomic size.''',
"OXIDATION STATE":'''Oxidation state: Transition metals show variable oxidation states due to
tendency of (n-1)d as well as ns electrons to take part in bond formation.''',
"MAGNETIC PROPERTIES": '''Magnetic properties: Most of transition metals are paramagnetic in nature
due to presence of unpaired electrons.''',
"CATALYTIC PROPERTIES": '''Catalytic properties: Most of transition metals are used as catalyst because
of (i) presence of incomplete or empty d –orbitals, (ii) large surface area,
(iii) variable oxidation state.''',
"FORMATION OF COLOURED COMPOUNDS":'''Formation of coloured compounds: They form coloured ions due to presence of
incompletely filled d – orbitals and unpaired electrons by absorbing colour
from visible region and radiating complementary colour.''',
"FORMATION OF COMPLEXES": '''Formation of complexes: Transition metals form complexes due to
(i) presen ce of vacant d – orbitals of suitable energy (ii) smaller size
(iii) higher charge on cations.'''                    }


for counter in range(8):
    userinput = input("Enter any of the properties to learn more or ('X') to skip: ")
    properties = userinput.upper()
    if properties == "X":
        print()
        print("###**********************************************************************###")
        print("You are now moved to specific properties of Transition Metals section")
        print()
        break
    elif properties in prop_collec:
        print ()
        print (trans_properties[properties])
        print()
    else:
        print ("Wrong ! Type the propeties name corectly")
        

# Declaration of dictionary data structure holding the list of transition metals
trans_Metal = {"Iron": ["NAME:   Iron", "SYMBOL:   Fe", "ATOMIC NUMBER:   26",
                       "ATOMIC MASS:   55.845 amu", "MELTING POINT:   1535.0 C",
                       "BOILING POINT:   2750.0 C", "DENSITY:   7.86g/cm3",
                       "NUMBER OF NEUTRONS:   30", "COLOUR:   Silvery",
                       "CRYSTAL STRUCTURE:   Cubic", "OBTAIN FROM:   Iron ores"],
              "Zinc": ["NAME:   Zinc", "SYMBOL::   Zn", "ATOMIC NUMBER::   30",
                       "ATOMIC MASS:   65.39 amu", "MELTING POINT:   419.58C",
                       "BOILING POINT:   907.0 C", "DENSITY:   7.133g/cm3",
                       "NUMBER OF NEUTRONS:   30", "COLOUR:   Bluish",
                       "CRYSTAL STRUCTURE:   Hexegonal", "OBTAIN FROM:   Calamine"],
              "Copper": ["NAME:   Copper", "SYMBOL::   Cu", "ATOMIC NUMBER::   29",
                       "ATOMIC MASS:   63.546 amu", "MELTING POINT:   1083.08C",
                       "BOILING POINT:   2567.0 C", "DENSITY:   8.96g/cm3",
                       "NUMBER OF NEUTRONS:   35", "COLOUR:   Red/Orange",
                       "CRYSTAL STRUCTURE:   Cubic", "OBTAIN FROM:   Coveline"],
              "Platinum": ["NAME:   Platinum", "SYMBOL::   Pt", "ATOMIC NUMBER::   78",
                       "ATOMIC MASS:   195.078amu", "MELTING POINT:   1772.0C",
                       "BOILING POINT:   3827.0C", "DENSITY:  21.45g/cm3",
                       "NUMBER OF NEUTRONS:   117", "COLOUR:   Silverish",
                       "CRYSTAL STRUCTURE:   Cubic", "OBTAIN FROM:   Platinum ores"],
              "Nickel": ["NAME:   Nickel", "SYMBOL::   Ni", "ATOMIC NUMBER::   28",
                       "ATOMIC MASS:   65.39 amu", "MELTING POINT:   1453.0C",
                       "BOILING POINT:   2732.0 C", "DENSITY:   8.902g/cm3",
                       "NUMBER OF NEUTRONS:   31", "COLOUR:   White",
                       "CRYSTAL STRUCTURE:   Cubic", "OBTAIN FROM:   Pentlandite"],
              "Cobalt": ["NAME:   Cobalt", "SYMBOL::   Co", "ATOMIC NUMBER::   27",
                       "ATOMIC MASS:   58.9332 amu", "MELTING POINT:   1495.0 C",
                       "BOILING POINT:   2870.0 C", "DENSITY:   8.9g/cm3",
                       "NUMBER OF NEUTRONS:   32", "COLOUR:   Silver",
                       "CRYSTAL STRUCTURE:   Hexagonal", "OBTAIN FROM:   Sulphur"],
              "Gold": ["NAME:   Gold", "SYMBOL::   Au", "ATOMIC NUMBER:   79",
                       "ATOMIC MASS:   196.9665 amu", "MELTING POINT:   1064.43C",
                       "BOILING POINT:   2807.0 C", "DENSITY:   19.32g/cm3",
                       "NUMBER OF NEUTRONS:   118", "COLOUR:  Gold",
                       "CRYSTAL STRUCTURE:   Cubic", "OBTAIN FROM:   Crust of the earth"],
              "Mercury": ["NAME:   Mercury", "SYMBOL::   Hg", "ATOMIC NUMBER:   80",
                       "ATOMIC MASS:   200.59 amu", "MELTING POINT:   -38.87 C",
                       "BOILING POINT:   356.58C", "DENSITY:   13.456g/cm3",
                       "NUMBER OF NEUTRONS:   121", "COLOUR:  Silver",
                       "CRYSTAL STRUCTURE:   Rhombohedral", "OBTAIN FROM:   Cinnabar ore"],
              "Silver": ["NAME:   Siver", "SYMBOL::   Ag", "ATOMIC NUMBER::   47",
                       "ATOMIC MASS:   107.86amu", "MELTING POINT:   961.93C",
                       "BOILING POINT:   2212.0C", "DENSITY:  10.5g/cm3",
                       "NUMBER OF NEUTRONS:   61", "COLOUR:   Silver",
                       "CRYSTAL STRUCTURE:   Cubic", "OBTAIN FROM:   argentite ores"],
              "Manganese": ["NAME:   Manganese", "SYMBOL::   Mn", "ATOMIC NUMBER::   25",
                       "ATOMIC MASS:   54.938amu", "MELTING POINT:   1245.0C",
                       "BOILING POINT:   1962.0 C", "DENSITY:   7.43g/cm3",
                       "NUMBER OF NEUTRONS:   30", "COLOUR:   grayish",
                       "CRYSTAL STRUCTURE:   Cubic", "OBTAIN FROM:   pyrolusite"],
              "Chromium": ["NAME:   Chromium", "SYMBOL::   Cr", "ATOMIC NUMBER::   24",
                       "ATOMIC MASS:   51.99amu", "MELTING POINT:   1857.0 C",
                       "BOILING POINT:   2672.0 C", "DENSITY:   7.19g/cm3",
                       "NUMBER OF NEUTRONS:   28", "COLOUR:   Gray",
                       "CRYSTAL STRUCTURE:   Cubic", "OBTAIN FROM:   Chromite"],
              "Tungsten": ["NAME:   Tungsten", "SYMBOL::   W", "ATOMIC NUMBER:   74",
                       "ATOMIC MASS:   183.84amu", "MELTING POINT:   3410.0",
                       "BOILING POINT:   5660C", "DENSITY:   19.3g/cm3",
                       "NUMBER OF NEUTRONS:   110", "COLOUR:  Silver",
                       "CRYSTAL STRUCTURE:   Cubic", "OBTAIN FROM:   Sheelite"],
              "Tantalum": ["NAME:   Tantalum", "SYMBOL::   Ta", "ATOMIC NUMBER:   73",
                       "ATOMIC MASS:   180.94amu", "MELTING POINT:  2996C",
                       "BOILING POINT:   5425.0C", "DENSITY:   16.654g/cm3",
                       "NUMBER OF NEUTRONS:   108", "COLOUR:  gray",
                       "CRYSTAL STRUCTURE:   Cubic", "OBTAIN FROM:   Tantalite"],
              "Zirconium": ["NAME:   Zirconium", "SYMBOL::   Zr", "ATOMIC NUMBER:   40",
                       "ATOMIC MASS:   91.224amu", "MELTING POINT:  1852.0C",
                       "BOILING POINT:   4377.0C", "DENSITY:   6.49g/cm3",
                       "NUMBER OF NEUTRONS:   51", "COLOUR:  grayish",
                       "CRYSTAL STRUCTURE:   Hexagonal", "OBTAIN FROM:   Zircon"]}

print("You can learn more about the sepcific properties any Transition metal here")
while True:
    test = input("Enter the name of transition metal or('Quit')to exit: ")
    test = test.capitalize()
    if test == "Quit":
        print ("...Exiting the program")
        break
    elif test in trans_Metal.keys():
        value = trans_Metal[test]
        for val in value:
            print (val)
        print()

