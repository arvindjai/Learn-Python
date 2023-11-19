import datetime
x = datetime.datetime.now()
y = datetime.datetime.strptime("17/09/1994 10:25","%d/%m/%y %H:%M")
print(x)
print(y.year)
print(y.strftime("%A"))
