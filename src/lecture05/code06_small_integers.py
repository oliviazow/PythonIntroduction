
# Python cached small integers to improve the performance
# -5 ~ 256
for a, b in zip(range(-10, 260), range(-10, 260)):
    print(a, id(a) == id(b))

# also for short strings
a = 'Hello!'
b = 'Hello!'
print('Hello!', id(a) == id(b))

# Output
# -10 False
# -9 False
# -8 False
# -7 False
# -6 False
# -5 True
# -4 True
# -3 True
# -2 True
# -1 True
# 0 True
# ...
# 254 True
# 255 True
# 256 True
# 257 False
# 258 False
# 259 False
# Hello! True
