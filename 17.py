import random

shuzi = str(random.randint(1000,9999))
cow=0
bull=0
num = str(input('plaease input your number: '))
list_shuzi = list(shuzi)
list_num = list(num)
for i in range(0,4):
	if(list_shuzi[i]==list_num[i]):
		cow=cow+1
	else:
		bull = bull+1
print("cow:"+str(cow),"bull: "+str(bull))

