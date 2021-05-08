list_a = [1,2,3,4,5]
#num = int(input('please enter your num: '))
def Islist():
	for i in list_a:
		if i == num:
			return True
		else:
			continue
			return False
#print(Islist())
def in_list(list,s):
	min = 0
	max = len(list)-1
	while(min<=max):
		mid = (min+max)//2
		if(list[mid]==s):
			return True
		if(list[mid]<s):
			min = mid+1
		else:
			max = mid-1
		return False
print(in_list([1,2,3,4,5,6],3))
print(in_list([1,2,3,4,5,6],7))