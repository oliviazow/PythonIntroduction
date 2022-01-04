# tuples.py

t = ()  # empty tuple
print(type(t))

one_element_tuple = (42, )  # you need the comma!
three_elements_tuple = (1, 3, 5)  # braces are optional here
a, b, c = 1, 2, 3  # tuple for multiple assignment
print(a, b, c)  # implicit tuple to print with one instruction
print(3 in three_elements_tuple)  # membership test


# swap
a, b = 1, 2
c = a  # we need three lines and a temporary var c
a = b
b = c
print(a, b)  # a and b have been swapped


# pythonic swap
a, b = 0, 1
a, b = b, a  # this is the Pythonic way to do it
print(a, b)
