# csv file, devices.txt, formatting:
# device_name,region,bandwidth_in,bandwidth_out

# 1. Sort the devices by bandwidth_in
# 2. Print the name and region of the devices once sorted
# We will use a dictionary
# dictionaries, unlike list, must be explicitally defined
devices = dict()

path = "./"
filename = "devices.txt"
# varible to store the mode used to open our file
# r = read only
# w = read and write
mode = "r"

# new and preferred way to open a file
# with does not require a close statement
with open(path+filename, mode) as f1:
  # for loop used to iterate over each line in the file
  for line in f1.readlines():
    # remove trailing carriage return
    clean_line = line.strip()
    # turn the line into a list using ',' as a separator
    list_line = clean_line.split(',')

    # we use a nested dictionary
    # the key of the external dictionary is the outgoing bandwidth
    # it will make ordering the elements much easier
    bwin = list_line[2]
    devices[bwin] = dict()
    devices[bwin]["name"] = list_line[0]
    devices[bwin]["region"] = list_line[1]
    devices[bwin]["bwout"] = list_line[3]

# we are creating a list containing the sorted outgoing bandwidths
# notice how we generate the list by using the keys() dictionary method.
sorted_bandwidths = sorted([bw for bw in devices.keys()])

for item in sorted_bandwidths:
    # print name and region using new formatting style
    print(f'Device: {devices[item]["name"]}. Region: {devices[item]["region"]}.')
    # the devices are sorted and can be easily referenced
    # since the keys in the device dictionary match the value
    # in sorted_bandwith list.