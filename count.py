lst = [6, 4, 5, 6, 7, 4, 5, 3, 2, 98, 98, 0 ,1]

k = {}

def cntOfLst(a):
	for i in lst:
		if i in k: 
			k[i] += 1 
			print("if part---> ", k)
		else: 
			k[i] = 1
			print("else part---> ", k)
	return k

print(cntOfLst(lst), sep = '\n')





