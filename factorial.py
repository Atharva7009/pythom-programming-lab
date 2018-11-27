def factorial(num):
    """This is a recursive function that calls
   itself to find the factorial of given number"""
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)

num = int(input("Enter a Number: "))

if num < 0:
    print("Factorial cannot be found for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", num, "is: ", factorial(num))
