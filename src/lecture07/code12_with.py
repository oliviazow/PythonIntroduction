with open("fear.txt") as f:
    for line in f:
        print(line, end="")
print(f.closed)

try:
    with open("NON_EXISTS.txt") as f:
        for line in f:
            print(line, end="")
finally:
    print(f.closed)
