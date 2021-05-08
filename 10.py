def is_Prime(num):
	for i in range(2,num):
		if(num%i==0):
			return 1


num = int(input('please enter a num: '))
flag = is_Prime(num)
if(flag==1):
	print('not prime')
else:
	print('it is a prime')