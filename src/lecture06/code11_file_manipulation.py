# file manipulation
from collections import Counter
from string import ascii_letters
from pprint import pprint

# ascii letters
chars = ascii_letters + ' '
print(chars)


def sanitize(s, chars):
    return ''.join(c for c in s if c in chars)


def reverse(s):
    return s[::-1]


# read lines
with open('fear.txt') as stream:
    lines = [line.rstrip() for line in stream]
pprint(lines)

# let's write the mirrored version of the file
with open('raef.txt', 'w') as stream:
    stream.write('\n'.join(reverse(line) for line in lines))

with open('raef.txt') as stream:
    reversed = stream.readlines()
pprint(reversed)

# now we can calculate some statistics
lines = [sanitize(line, chars) for line in lines]
whole = ' '.join(lines)
reversed_lines = [sanitize(line, chars) for line in reversed]
reversed_whole = ' '.join(reversed_lines)

# we perform comparisons on the lowercased version of 'whole'
cnt = Counter(whole.lower().split())
# we can print the N most common words
print(cnt.most_common(3))

# we perform comparisons on the lowercased version of 'whole'
cnt = Counter(reversed_whole.lower().split())
# we can print the N most common words
print(cnt.most_common(3))
