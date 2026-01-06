a = input("Enter a string : ")
rev = ""
for x in a:
    rev = x + rev
if a == rev:
    print("Palindrome")
else:
    print("Not a plaindrome")
