def list_replace(a):
	return set(a)




def list_add(a):
	b=[]
	for num in a:
		if num not in b:
			b.append(num)
	return b
a = [1,2,3,1,4,6,3,2]
#print(str(list(a)).replace('{','[]'))
print(list(list_replace(a)))
print(list_add(a))