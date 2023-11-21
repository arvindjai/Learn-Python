# Given a list of integers, find the sum of all positive numbers.

list_num = [2,-5, 7, 11, -3, 12, -7]
sum = 0
for i in list_num:
    if i > 0:
        sum = sum + i
print(sum)