my_dict = {'name': 'David', "age": 30, 'birthplace': 'Detroit'}

nest_dict = {
    'a': {
        'apple':'a red fruit',
        'ant': 'a bug'
    },
    'b': {
        'banana': 'curvy fruit',
        'beetle': 'hercules of bugs'
    }
}

my_dict['job'] = 'full stack developer'
my_dict['name'] = 'DAP'
print(my_dict.items())
for i, j in my_dict.items():
    print('i, j',i, j)
# keys(), values(), items(), get()
print()