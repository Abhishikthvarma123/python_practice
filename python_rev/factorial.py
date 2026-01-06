num = int(input("Enter a number : "))
fact = 1
if num < 0:
    print("Invalid number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for x in range(1,num+1):
        fact *= x
    print("The factorial of the number is :",fact)
