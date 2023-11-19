# Calculate the compound interest for a given principal amount, interest rate, and time period
principle = 10000
rate = 10
n = 1
t = 1
expo = n*t
amount = principle*(1 + (rate/n))**expo
print(amount)