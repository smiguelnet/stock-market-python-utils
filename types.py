import os

words = "sergio miguel information".split()
[print(word) for word in words]

print(str('#=' * 50))

path = 'stock-price.csv'

if os.path.exists(path):
    print(' path {0} exists'.format(path))
else:
    print('the path {0} DO NOT EXISTS'.format(path))

info = 1
print(type(info))

info = "smiguelnet"
print(type(info))

# raise ValueError('new exception forced to thrown')

info = []

if isinstance(info, str):
    print('string datatype')
elif isinstance(info, int):
    print('int datatype')
else:
    print('some other thing that I dont know...')
    


