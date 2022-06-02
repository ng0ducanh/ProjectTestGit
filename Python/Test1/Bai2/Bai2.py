
from email import header
from info import Info
from tabulate import tabulate

import numpy as np

dns_file = open("DNSList.txt", "r")
arr = dns_file.read().replace("\t","").split("\n")

ip_arr = []
location_arr = []
status_arr = []
Reliability_arr = []

for i in arr:
    if "IP Address" in i :
        ip_arr.append(i.split(": ")[1])
    if "Location" in i :
        location_arr.append(i.split(" ")[1])
        # loction_string = i.split(": ")[1]
        # if "United" in loction_string :
        #     loction_string = "United"
    if "Status" in i:
        status_arr.append(i.split(": ")[1])
    if "IP Address" in i:
        Reliability_arr.append(i.split(": ")[2])

info_arr = []

for i in range (0, len(ip_arr)):
    info_arr.append(Info(ip_arr[i], location_arr[i], status_arr[i], Reliability_arr[i]))

set_location_arr = list(set(location_arr))
set_location_arr.sort()


count_arr = [0]*len(set_location_arr)
for i in range (0,len(set_location_arr)) :
    count_arr[i] = location_arr.count(set_location_arr[i])

# Cach 1:
table = tabulate({"Country": set_location_arr, 'Count':count_arr}, headers = 'keys', tablefmt="plain")
print(table)

# Cach 2:
print("{:<9}{:>8}".format('Country', 'Count'))
for i,j in zip(set_location_arr, count_arr) :
    print("{:<9}{:>8}".format(i, j))

dns_file.close()