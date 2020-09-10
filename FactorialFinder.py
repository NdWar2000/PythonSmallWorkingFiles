# Factorial of +int is def:
# n, n-1, n-2 etc with 0 being 1.
# Solve using loop and recursion.

#recursive function:
def rec_factorial(number):
    if number == 1:
        return number
    else:
        return number * rec_factorial(number - 1)

# ensure int given is +ive
number = -1
while number < 0:
    try:
        number = int(input("Please provide a positive number: "))
        if number < 0:
            raise Exception()

    except ValueError:
        print("Error. Please enter a positive number.\n")
    except:
        print("Error. Please enter a positive number.\n")

# If int == 0 return 1
fact = 1
if number == 0:
    print("Result of 0! = 1")
else:
# else loop
    for i in range(1, number + 1):
        fact *= i

    print("Loop: Result of " + str(number) + "! = " + str(fact))

#recursive
#Already caught 0
    result = rec_factorial(number)
    print("Recurve: Result of " + str(number) + "! = " + str(result))

