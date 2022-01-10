with open('write_x.txt', 'x') as fw:  # this succeeds
    fw.write('Writing line 1')
with open('write_x.txt', 'x') as fw:  # this fails
    fw.write('Writing line 2')