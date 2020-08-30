i = 0 
while i < 5:
    print(i)
    i += 1
i = None

for i in range(5):
    print(i)

for i in [1, 2, 3, 4]:
    print(i)

for c in 'hello':
    print(c)

for i,j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)

for i in range(5):
    if i==3:
        break
    print(i)

for i in range (1, 5):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    print('no multiples of 7 in the range')

for i in range(5):
    print('-----------------------------')
    try:
        10 / (i-3)
    except ZeroDivisionError:
        print('division by 0')
        continue
    finally:
        print("always run")
    print(i)

s = 'hello'
for i in range(len(s)):
    print(i, s[i])

for i, c in enumerate(s):
    print(i,c)