path = "./"
filename = "devices.txt"
# varible to store the mode used to open our file
# r = read only
# w = read and write
mode = "r"

f1 = open(path+filename, mode)
# for loop used to iterate over each line in the file
for line in f1.readlines():
    # remove trailing carriage return
    clean_line = line.strip()
    # notice the new way to format output
    print(f"{clean_line}")

# do not forget to relase the file handler once done
f1.close()