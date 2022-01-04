tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])

# delete
del tel['sape']
tel['irv'] = 4127
print(tel)

# cast
print(list(tel))
print(sorted(tel))

# in
print('guido' in tel)
print('jack' not in tel)

# create from list of tuples
d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d)

# comprehension
d = {x: x**2 for x in (2, 4, 6)}
print(d)

# create using kwargs
d = dict(sape=4139, guido=4127, jack=4098)
print(d)