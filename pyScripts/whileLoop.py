i = 0 
while i < 5:
    print(i)
    i += 1

i = 7
while True:
    print(i)
    if i >= 5:
        break

# min_length = 1
# name = input ("Please eneter your name:")

# while not (len(name) >= min_length and name.isprintable() and name.isalpha()):
#     name = input ("Please eneter your name:")
# print("Hello, {0}".format(name))

# refactor code above
min_length = 1

# while True:
#     name = input ("Please eneter your name:")
#     if len(name) >= min_length and name.isprintable() and name.isalpha():
#         break
# print("Hello, {0}".format(name))

a = 2
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)


a=0
b=10
try:
    a/b
except ZeroDivisionError:
    print("division error")
finally:
    print("Done")

a=0
b=10
while a < 4:
    print('---------------')
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError:
        print("{0}, {1} - division by Zero. format(a,b)".format(a,b))
        continue
    finally:
        print("{0}, {1} - always. format(a,b)")
    
    print("{0}, {1} - main loop".format(a,b))
else:
    print('Code executed without a zero division error')
        