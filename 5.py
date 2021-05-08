import random
print(list(set([element for element in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if element in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]])))
x = list(random.sample(range (100),10))
y = list(random.sample(range (20),15))
print(list(set([element for element in x if element in y])))