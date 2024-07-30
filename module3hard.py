data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def isihard(*args):
    suma = 0
    for i in args:
        if isinstance(i, (list, tuple, set)):
            for j in i:
                suma += isihard(j)
        elif isinstance(i, (int)):
            for j in i:
                suma += i
        elif isinstance(i, (str)):
            for j in i:
                suma += len(i)


result = isihard(data_structure)
print(result)
