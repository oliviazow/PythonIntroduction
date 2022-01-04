
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
print('orange' in basket)          # fast membership testing
print('crabgrass' in basket)


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                           # unique letters in a
print(a - b)                       # letters in a but not in b
print(a | b)                       # letters in a or b or both
print(a & b)                       # letters in both a and b
print(a ^ b)                       # letters in a or b but not both


# set comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)


# set is mutable
small_primes = set()    # empty set
small_primes.add(2)     # adding one element at a time
small_primes.add(3)
small_primes.add(5)
print(small_primes)
small_primes.add(1)     # Look what I've done, 1 is not a prime!
print(small_primes)
small_primes.remove(1)  # so let's remove it
print(small_primes)


# frozenset is immutable

small_primes = frozenset([2, 3, 5, 7])
bigger_primes = frozenset([5, 7, 11])

print(small_primes & bigger_primes)  # intersect, union, etc. allowed
# frozenset({5, 7})

small_primes.add(11)  # we cannot add to a frozenset
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'frozenset' object has no attribute 'add'

small_primes.remove(2)  # neither we can remove
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'frozenset' object has no attribute 'remove'
