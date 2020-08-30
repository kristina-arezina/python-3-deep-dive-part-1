import time
# int object uses a variable number of bits
# how big can an integer get in python (memory)
# larger numbers = arithmetic gets slower


# print(type(100))

2**1000

# Small number
def calc(a):
    for i in range(1000000):
        a*2

start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(end - start)

# Medium number
def calc(a):
    for i in range(1000000):
        a*2

start = time.perf_counter()
calc(2**100)
end = time.perf_counter()
print(end - start)

# Large number
def calc(a):
    for i in range(1000000):
        a*2

start = time.perf_counter()
calc(2**10000)
end = time.perf_counter()
print(end - start)

