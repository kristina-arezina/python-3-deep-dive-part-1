# int + int = int
# int - int = int
# int * int = int
# int ** int = int
# int / int = float (always)
#  // called floor division
#  % modulo operator
#  n = d * (n // d) + (n % d)

# Floor division, of real number a is largest 

type (1 +1 )

type ( 2/3)

type (10/2)

import math

# floor() method returns the floor of x i.e. the largest integer not greater than x
print(math.floor(3.15)) # Prints 3
print(math.floor(-3.15)) # Prints -4
print(math.floor(-3.0000001)) # Prints -4
print(math.floor(-3.0000000000000001)) # Prints -3 due to floating points

a = 33
b = 16
print (a/b) # 2.0625
print (a//b) # 2
print (math.floor(a//b)) # 2

a = -33
b = 16
print (a/b) # -2.0625
print (a//b) # -3
print (math.floor(a//b)) # -3

a = -33
b = 16
print (a/b) # -2.0625
print (a//b) # -3
# Note: Floor and trunc are not the same thing
print (math.floor(a/b)) # -3
print (math.trunc(a/b)) # -3

# mod operator
# equation a = b*(a//b) + (a %b)
a = 13
b =-4
print('__________')
print('{0}/{1} = 2'.format(a, b, a/b)) 
print('{0}//{1} = 2'.format(a,b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print( a == b * (a//b) + (a%b))

