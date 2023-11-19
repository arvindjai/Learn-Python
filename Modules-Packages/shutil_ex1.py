import shutil
import psutil



# print(dir(shutil))
du = shutil.disk_usage("/")
print(du)
total,used,free = du
used_percent = (used / total ) * 100
free_percent = free/total * 100
print("Disk used : {}".format(round(used_percent,2)))
print("Disk free : {}".format(round(free_percent,2)))

pu = psutil.cpu_percent(0.5)
print(pu)