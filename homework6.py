my_dict={'Rustam':1991,'Laura':1994, 'Arslan':2011}
print(my_dict)
print(my_dict['Laura'])
print(my_dict.get('Alan'))
my_dict.update({'Alina':1993,
                'Kamil':1993})
del my_dict ['Kamil']
print(my_dict)
my_set={1,2,3,1,3,4,7,'w','t','w',(1,2,3)}
my_set.add('c')
my_set.add(9)
my_set.discard('w')
print(my_set)