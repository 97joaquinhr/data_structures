arr = [1, 5, 7, -1, 5]
sum = 6

def printPairs(arr,sum):
	m = {}
	n = len(arr)
	for i in range(0,n):
		rem = sum - arr[i]
		count = m.get(rem)
		if(count!=None):
			for j in range(0,count):
				print("("+str(rem)+", "+str(arr[i])+")")
		if(m.get(arr[i])!=None):
			m[arr[i]]+=1
		else:
			m[arr[i]]=1

printPairs(arr,sum)