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
        elif isinstance(i, int):
            suma += i
        elif isinstance(i, str):
            suma += len(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                suma += isihard(key,value)
    return suma


result = isihard(data_structure)
print(result)
