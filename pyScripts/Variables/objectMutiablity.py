def process(s):
    print('Initial s # = {0}'.format(id(s)))
    s = s + 'world'
    print('Final s # = {0}'.format(id(s)))

my_var = 'hello'
print('my_var # = {0}'.format(id(my_var)))

print(process(my_var))

def modify_list(lst):
    print('Initial lst # = {0}'.format(id(lst)))
    lst.append(100)
    print('Final lst # = {0}'.format(id(lst)))

my_list = [1, 2, 3]
print(id(my_list))

my_tuple 