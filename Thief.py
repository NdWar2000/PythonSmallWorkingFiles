#Thief:
    #A thief has managed to find out the four digits for an online PIN code, 
    #but doesn’t know the correct sequence needed to hack into the account.
    #Design and write a program that displays all the possible combinations 
    #for any four numerical digits entered by the user. 
    #The program should avoid displaying the same combination more than once.
    #Submit a fully detailed Showcase for your program
    
# enter four digit number
def cap_int(output_str = ""):
    num = 0
    while not len(str(num)) == 4:
        try:
            num = int(input("Please enter a four digit number: "))
            if not len(str(num)) == 4:
                raise Exception
        except:
            print("Error: Needs to be a four digit number.\n")
            
    return str(num)
            
def main():
    code = cap_int()
    
    for i in range(4):
        for j in range(4):
            if i == j:
                pass
            else:
                for k in range(4):
                    if i == k or j == k:
                        pass
                    else:
                        for l in range(4):
                            if i == l or j == l or k == l:
                                pass
                            else:
                                print(code[i] + code[j] +  code[k] + code[l])

    
main()
