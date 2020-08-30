# integer is an object
type(10)
# help(int) # tells you what an int is

print(int(10.5)) # 10
print(int(10.99999)) # 10
print(int(True)) #1
print(int(False)) #0

import fractions
a = fractions.Fraction(22, 7)
print(float(a))