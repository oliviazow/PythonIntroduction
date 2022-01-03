
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1  # multiple assignment
while a < 20:  # while loop
    print(a)
    a, b = b, a+b
