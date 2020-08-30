import gc

def ref_count(address):
    return ctypes.c_long.from_address.value

def object_by_id(object_id):
    for obj in gc.get_object():
        if id(obj) == object_id:
            return "Object exists"
        return "Not found"


# Two classes with a circular reference   
class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b:{1}'.format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a:{1}'.format(hex(id(self)), hex(id(self.a))))

my_var = A()
print (my_var)

print(hex(id(my_var)))

print(my_var.b)

