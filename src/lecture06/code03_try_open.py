fh = open('fear.txt')  # rt is default
try:
    for line in fh:  # we can iterate directly on fh
        print(line.strip())
finally:
    fh.close()