# Given a list of numbers, find the sum and average
list_num = [2,-5, 7, 11, -3, 12, -7]
sum = 0
for i in list_num:
    sum += i
print(f"Sum is : {sum}")
count = len(list_num)
avg = sum/count 
print(f"Average is : {round(avg,2)}")