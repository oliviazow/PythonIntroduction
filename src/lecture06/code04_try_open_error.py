fh = open('fear.txt')  # rt is default
try:
    for line in fh:  # we can iterate directly on fh
        print(line.strip())
        raise Exception('Ah oh! Something Wrong!')
finally:
    fh.close()
    print('File handle closed!!!!!!!!!!!!!')