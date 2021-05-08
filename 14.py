teststring = input('please enter your string: ')
result = teststring.split(" ")
print((result[::-1]))
def reverseWord(w):
	return ' '.join(w.split()[::-1])

print(reverseWord(teststring))