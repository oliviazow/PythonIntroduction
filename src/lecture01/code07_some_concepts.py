# -------------------------------------------------------------------------------------------------
# Comments

# this is a comment

# This is a long comment
# and it extends
# to multiple lines

"""This is a
   a perfect
   multiple line comment too"""

# -------------------------------------------------------------------------------------------------
# Python Identifiers
# An identifier is a name given to entities like class, functions, variables, etc. It helps to
# differentiate one entity from another.
#
# Rules for writing identifiers
#
# 1. Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or
#    digits (0 to 9) or an underscore _. Names like myClass, var_1 and print_this_to_screen, all
#    are valid example.
# 2. An identifier cannot start with a digit. 1variable is invalid, but variable1 is a valid name.
# 3. Keywords cannot be used as identifiers.

global = 1  # SyntaxError: invalid syntax

# 4. Special symbols like !, @, #, $, % etc. cannot be used in an identifier.

a@ = 0  # SyntaxError: invalid syntax

# -------------------------------------------------------------------------
# Python Variables
# A variable is a named location used to store data in the memory. It is
# helpful to think of variables as a container that holds data that can be
# changed later in the program.
number = 10
print('number = ', number)
number = 1000000
print('number = ', number)

# -------------------------------------------------------------------------
# Python is a case-sensitive language.
a = 1
A = 2
print('a = ', a, ', A = ', A)


# -------------------------------------------------------------------------
# Statements
# Instructions that a Python interpreter can execute are called statements.
a = 1
print('a = ', a)

# multi-line statement
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print('a = ', a)

# multi-statements in 1 line
a = 1; b = 2; c = 3
print('a = ', a, ' b = ', b, ' c = ', c)

# Expressions are special statements: only contain identifiers, literals,
# operators and calls to functions, mostly used interactively.
1 + 2

# -------------------------------------------------------------------------
# Python Indentation
# Python uses indentation to define a block of code.

a = 0
while a < 10:
    a += 1
    if a % 2:
        print('Do not print odd numbers')
        continue
    print(a)
