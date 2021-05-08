import random
a=list(random.sample(range(10),10))
b=[a[0],a[9]]
print(b)
def list_ends(a_list):
	return[a_list[0],a_list[len(a_list)-1]]