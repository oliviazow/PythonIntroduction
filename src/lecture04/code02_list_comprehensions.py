from pprint import pprint
# -----------------------------------------------------------------------------
# normal way to create a list
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# -----------------------------------------------------------------------------
# list comprehension
squares = [x**2 for x in range(10)]
print(squares)

# A list comprehension consists of brackets containing an expression followed
# by a for clause, then zero or more for or if clauses.

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
pprint(combs)

# Nested List Comprehensions

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
tranposed = [[row[i] for row in matrix] for i in range(4)]
pprint(tranposed)