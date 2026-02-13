#--------------------------------------
#
# Tornado Infographic
#
#--------------------------------------

#Main function to call welcome function and a loop to call other functions from the input
def main():
    welcome()
    x = 0
    while x < 1:
        print("Here are your options:")
        print("A) EF1")
        print("B) EF2")
        print("C) EF3")
        print("D) EF4")
        print("E) EF5")
        print("F) Tornado Alley game")
        y = input("Please choose one (or Q to quit)")
        if y == "A":
            eF1()
        elif y == "B":
            eF2()
        elif y == "C":
            eF3()
        elif y == "D":
            eF4()
        elif y == "E":
            eF5()
        elif y == "F":
            tornadoGame()
        elif y == "Q":
            x = x + 1
            print("\n"+"Goodbye")
        else:
            print("\n"+"Invalid input"+"\n")

#Welcome function to print welcome messages
def welcome():
    print("Welcome to the Tornado Informer.")
    print("I give information on each tornado on the Fujita scale.")
    print("I Also have a game to check if a state is in tornado alley.")
    print("Such as wind speed, size, and precautions to take to stay safe.")
    print("As well an example of a tornado that already happened.")
    print("Note: Tornados are usually rated after the tornado has happened.")

#eF1 function to print information about an EF1 tornado   
def eF1():
    print("\n"+"EF1 Tornado")
    print("Wind speed: 73-112 MPH"+"\n")
    print("Hazards:")
    print("Mobile homes rolled.")
    print("Cars pushed around.")
    print("Little to no home damage."+"\n")
    print("Precautions:")
    print("Go to a safe location (interior room, underground shelter, or public shelter).")
    print("Have your NOAA weather radio prepared.")
    print("Protect your head (blanket, helment, lay low to the ground.")
    print("If in a car or truck, try to steer out of its path.")
    print("Don't hide under a bridge."+"\n")
    
#eF2 function to print information about an EF2 tornado
def eF2():
    print("\n"+"EF2 Tornado")
    print("Wind speed: 113-157 MPH"+"\n")
    print("Hazards:")
    print("Little to moderate home damage.")
    print("Mobile homes destroyed.")
    print("light missiles generated."+"\n")
    print("Precautions:")
    print("Go to a safe location (interior room, underground shelter, or public shelter).")
    print("Have your NOAA weather radio prepared.")
    print("Protect your head (blanket, helment, lay low to the ground.")
    print("If in a car or truck, try to steer out of its path.")
    print("Don't hide under a bridge."+"\n")
    
#eF3 function to print information about an EF3 tornado
def eF3():
    print("\n"+"EF3 Tornado")
    print("Wind speed: 158-206 MPH"+"\n")
    print("Hazards:")
    print("Moderate home damage.")
    print("Trees uprooted.")
    print("Trains derailed."+"\n")
    print("Precautions:")
    print("Go to a safe location (interior room, underground shelter, or public shelter).")
    print("Have your NOAA weather radio prepared.")
    print("Protect your head (blanket, helment, lay low to the ground.")
    print("If in a car or truck, try to steer out of its path.")
    print("Don't hide under a bridge."+"\n")
    
#eF4 function to print information about an EF4 tornado
def eF4():
    print("\n"+"EF4 Tornado")
    print("Wind speed: 207-260 MPH"+"\n")
    print("Hazards:")
    print("High amounts of house damage.")
    print("Weak structures blown away.")
    print("Large missiles generated."+"\n")
    print("Precautions:")
    print("Go to a safe location (underground shelter or public shelter).")
    print("Have your NOAA weather radio prepared.")
    print("Protect your head (blanket, helment, lay low to the ground.")
    print("If in a car or truck, try to steer out of its path.")
    print("Don't hide under a bridge."+"\n")
    
#eF5 function to print information about an EF5 tornado
def eF5():
    print("\n"+"EF5 Tornado")
    print("Wind speed: 261-318 MPH"+"\n")
    print("Hazards:")
    print("Houses destroyed.")
    print("Automobile sized missiles.")
    print("steel reinforced structures badly damaged."+"\n")
    print("Precautions:")
    print("Go to a safe location (underground shelter or evacuate).")
    print("Have your NOAA weather radio prepared.")
    print("Protect your head (blanket, helment, lay low to the ground.")
    print("If in a car or truck, try to steer out of its path.")
    print("Don't hide under a bridge."+"\n")
    
#tornadoGame function to run the small game on if a state is in, near, or not in tornado alley
def tornadoGame():
    #Creates lists invvolving every state for if its in, close, outside of tornado alley
    alley = ["Mississippi", "Alabama", "Louisiana", "Tennessee"]
    close = ["Georgia", "Texas", "Kentucky", "Arkansas"]
    safe = ["Alaska", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    #Loop to ask for user input  and check for a state if its in tornado alley
    z = 0
    while z < 1:
        alOut = 0
        clOut = 0
        saOut = 0
        a = input("\n"+"Please input a state (Make sure the first letter is capitalized) (or Q to quit)")
        for state in alley:
            if a == state:
                alOut = alOut + 1
        for state in close:
            if a == state:
                clOut = clOut + 1
        for state in safe:
            if a == state:
                saOut = saOut + 1
        if alOut == 1:
            print("\n"+"This is a state in tornado alley.")
        elif clOut == 1:
            print("\n"+"This is a state near tornado alley.")
        elif saOut == 1:
            print("\n"+"This is a state not in tornado alley.")
        elif a == "Q":
            z = z + 1
            print("\n"+"Going back to main."+"\n")
        else:
            print("\n"+"Invalid input")
            
main()
