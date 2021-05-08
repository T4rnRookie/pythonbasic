with open('flag.txt','a') as f:
	f.write('\n'+'flag{1233123}')
	#print('ok')

with open('flag.txt','r') as f:
	print(f.read())
