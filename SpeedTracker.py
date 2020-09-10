#Speed Tracker
#takes a time for a car going past a speed camera,
#the time going past the next one
#the distance between them to calculate the average speed for the car in mph.
#The cameras are one mile apart.
#Extensions:
    #1:
        #Speed cameras know the timings of each car going past,
        #through number plate recognition.
        #Valid number plates are two letters,
        #two numbers and three letters afterwards, for
        #example XX77 787.
        #Produce a part of the program that checks whether a number plate matches
        #the given pattern. Tell the user either way.
    #2:
        #Create a program for creating a file of details for vehicles exceeding
        #the speed limit set for a section of road. You will need to create a
        #suitable file with test data, including
        #randomised number plates and times. You will then use the code you’ve
        #already written to process this list to determine who is breaking the
        #speed limit (70mph) and who has invalid number plates.

def capture_int(for_output = ""):
    captured_int = -1
    while captured_int < 0:
        try:
            captured_int = int(input(for_output))
            if captured_int < 0:
                raise Exception()

        except:
            print("Error: Please enter a valid number.\n")

    return captured_int

def capture_plate(for_output = ""):
    plate = ""
    while plate == "":
        try:
            plate = input("Enter plate (NN99 NNN): \n")
            plate1, plate2 = plate.split()
            if plate1[0].isalpha() \
                and plate1[1].isalpha() \
                and plate1[2].isnumeric() \
                and plate1[3].isnumeric:
                pass
            else:
                raise Exception("Format incorrect.")

            if plate2.isalpha() \
                and len(plate2) == 3:
                pass
            else:
                raise Exception("Format incorrect.")

        except ValueError:
            print("Error: Must have a space in plate.")
            plate = ""

        except Exception as inst:
            print("Error: " + str(inst.args[0]))
            plate = ""

    return plate

def main():

    first_cam = second_cam = 0

    first_cam = capture_int("Please enter time (seconds) for the first camera:\n")
    while second_cam <= first_cam:
        second_cam = capture_int("Please enter time (seconds) for the second camera:\n")
        if second_cam <= first_cam:
            print("Error: This program does not believe in time travel. Please try again.\n")

    time = (second_cam - first_cam) / 60
    speed = (1 / time) * 60
    print("Speed is: " + str(speed) + "mph")

    #Number plate validation: XX99 999
    ticket_given = "No"
    if speed > 70:
        ticket_given = "Yes"

    plate = capture_plate()
    try:
        file = open("SpeedTracker.txt", "a+")
        file.write("\nCar: " + plate + "\n"
                    + "Entry time: " + str(first_cam) + "\n"
                    + "Exit time: " + str(second_cam) + "\n"
                    + "Speed: " + str(speed) + "\n"
                    + "Ticket given (speed above 70)? " + ticket_given + "\n")
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as inst:
        print("Error: " + str(type(inst)) + " : " + str(inst.args[0]))
        file.close()




if __name__ == "__main__":
    main()
