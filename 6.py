string = input("please input your string: ")
if(string[::-1]==string):
	print("it's a huiwen")
else:
	print("nope bro")
#loops
def reverse(word):
	x=''
	for i in range(len(word)):
		x+=word[len(word)-1-i]
	return x
word = input("give me")
if(word == reverse(word)):
	print("1")
else:
	print("0")