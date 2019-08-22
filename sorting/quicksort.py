# Average: O(nlog(n))
# Worst case: O(n^2)
# As long as we are smart on how we pick the pivots.

data = [7,4,2,9,1,3,5,6,1]

def partition(data,left,right,pivot):
	while(left<=right):
		while(data[left]<pivot):
			left+=1
		while(data[right]>pivot):
			right-=1
		if(left<=right):
			data[left],data[right]=data[right],data[left]
			left+=1
			right-=1
	return left

def quicksort(data,left,right):
	if(left>=right):
		return
	pivot = data[(left+right)//2]
	index = partition(data,left,right,pivot)
	quicksort(data,left,index-1)
	quicksort(data,index,right)

quicksort(data,0,len(data)-1)
print(data)