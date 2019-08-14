data = [2,3,4,5,6,7,10,12,14,15,23,34,45,56]

target = 13

def binary_search_iterative(data, target):
	low = 0
	high = len(data)-1
	while low<=high:
		mid = (low+high)//2
		if(data[mid]<target):
			low = mid+1
		elif data[mid]>target:
			high = mid-1
		else:
			return mid
	return -1

def binary_search_recursive(data, target, low, high):
	if low>high:
		return False
	else:
		mid = (low+high)//2
		if target == data[mid]:
			return mid
		elif target<data[mid]:
			return binary_search_recursive(data,target,low,mid-1)
		else:
			return binary_search_recursive(data,target,mid+1,high)


print(binary_search_iterative(data,0))
print(binary_search_recursive(data,12,0,len(data)-1))
print(binary_search_recursive(data,11,0,len(data)-1))