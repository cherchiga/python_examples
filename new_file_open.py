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
    # notice the new way to format output
    print(f"{clean_line}")