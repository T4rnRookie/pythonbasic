num = int(input("enter your number: "))
check=int(input("give a number to divide by"))
if(num %4 ==0):
	print(num,"is a multiple of 4")
elif(num %2 ==0):
	print(num,"is an even number")
else:
	print(num,"is an odd number")

if(num % check ==0):
	print(num,"divides evenly by")
else:
	print(num,"does not divide evenly by",check)