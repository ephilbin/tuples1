d = {'foo': 1, 'bar': 2, 'baz':3} #dictionary with three tuples (like sets, such as 'foo': 1)
while d: #while d is true or filled with data
    print(d.popitem()) #popitem is a function that removes the last added item in a dictionary
print('Done.')
#pop