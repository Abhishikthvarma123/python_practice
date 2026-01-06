num = int(input("Enter a number : "))
a,b = 0,1
count = 0
if num < 0:
    print("Invalid number")
elif num == 0:
    print("The fibonaccis series of 0 is")
    print(a)
else:
    print("The fibonacci series of the number is : ")
    while count < num:
        print(a,end="")
        a,b = b,a+b
        count += 1
