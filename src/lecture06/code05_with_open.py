# Using a context manager to open a file
with open('fear.txt') as fh:
    for line in fh:
        print(line.strip())