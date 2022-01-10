fh = open('fear.txt', 'rt')  # r: read, t: text
for line in fh.readlines():
    print(line.strip())  # remove whitespace and print
fh.close()
