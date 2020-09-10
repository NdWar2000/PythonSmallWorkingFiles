#Classification:
    #A simple classification system asks a series of Yes/No questions in order 
    #to work out what type of animal is being looked at.
    #Eg Does it have 4 legs? Does it eat meat? Does it have stripes?
    #These systems can often be drawn using a “tree” structure. 
    #Carry out some simple research on classification trees, 
    #then write a program to help the user decide between the following
    #horse, cow, sheep, pig, dog, cat, lion, tiger, whale, dolphin, seal, 
    #penguin, ostrich, sparrow, spider, ant, bee, wasp, termite, octopus, squid
    #Is there a better way to do this than using 101 IF...ELSE...END IFs?
    #Develop your classification system for your own area of interest
    
def choose_a_creature():
    j = 0

    creatures = ["horse", "cow", "sheep", "pig", "dog", "cat", "lion", 
                "tiger", "whale", "dolphin", "seal", "penguin", "ostrich", 
                "sparrow", "spider", "ant", "bee", "wasp", "termite", 
                "octopus", "squid"]

    print("Please choose a creature from this list:")
    
    for i in range(len(creatures)):
        spacer = 8
        a_space = ""
        spacer -= len(creatures[i])
        for k in range(spacer):
            a_space += " "
        print(" " + creatures[i] + a_space, end=" |")
        j += 1
        if j == 6:
            j = 0
            print("")
    
    
def capture_input(output_string = ""):
    captured = ""
    while captured == "":
        print("\n" + output_string)
        try:
            captured = input("(Y)es or (N)o? ").lower().strip()
            if captured == "y":
                return True
            elif captured == "n":
                return False
            else:
                raise Exception
        except:
            print("Error: Please enter a Y/N.\n")
            captured = ""

def main():
    choose_a_creature()
    print("\n")
    if capture_input("Is the creature an arthropod?"):
        if capture_input("Does the arthropod fly?"):
            if capture_input("Does the insect produce honey?"):
                print("The insect is a bee.")
            else:
                print("The insect is a wasp.")
        elif capture_input("Does the arthropod spin a web?"):
            print("The arthropod is a spider.")
        elif capture_input("Does the arthropod like wood?"):
            print("The arthropod is a termite.")
        else:
            print("The arthropod is an ant.")
    elif capture_input("Is the creature a type of bird?")
            

main()
