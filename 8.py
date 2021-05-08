import random
num = int(input('please input one number: '))
realnum = random.randint(1,9)
if(num<realnum):
	print("too small")
elif(num>realnum):
	print("too big")
else:
	print("You r right")