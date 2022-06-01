cheese = ['cheddar', 'stilton','cornish yarg']
print(cheese[1])
cheese[-1] = 'red leicester'
print(cheese)
# list is mutable
# printed stilton as item no 1 in the list
names = ['imaan','elle', 'kate']
print(names[-2])
print(names[-1])
print(names[2])
# from the left access start the index from 0, 1 ,2 ,3
# from the right acess start from index -1,-2,-3,-4
cheese = ['cheddar', ['camembert','brie'],'stilton']
print(cheese[1][0])
# multi-dimensional lists are just lists containing other lists
# nested lists