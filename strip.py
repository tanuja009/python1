file = open('file1.txt', 'r')
for line in file:
    print(line.strip())  # strip() removes any extra newline characters
file.close()
