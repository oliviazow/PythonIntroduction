# Example on Python list methods

my_list = [3, 8, 1, 6, 8, 8, 4]

# Add 'a' to the end
my_list.append('a')

# Output: [3, 8, 1, 6, 0, 8, 4, 'a']
print(my_list)

# Index of first occurrence of 8
print(my_list.index(8))   # Output: 1

# Count of 8 in the list
print(my_list.count(8))  # Output: 3

my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)