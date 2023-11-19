# Create a Python function to check if a given string is apalindrome
num = input("Enter number: ")
reversed_num = num[::-1]
print(reversed_num)
if num == reversed_num:
    print("number is palindrome.")
else:
    print("Not palindrome")