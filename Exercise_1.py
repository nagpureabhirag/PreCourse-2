# Python code to implement iterative Binary  
# Search. 

# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 

	#write your code here
	mid = int((l + (r-l)/2))

	while l <= r:
		mid = int((l + (r-l)/2))
		if arr[mid] == x:
			return mid
		if arr[mid] < x:
			l = mid + 1
		else:
			r = mid - 1

	return -1


# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
# arr = [10, 15]
# arr = [1, 10]
# arr = [10]
# arr = [10, 122, 123, 12412, 1253, 5454, 54545, 66666, 77777, 88888]
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
	print("Element is present at index % d" % result)
else: 
	print("Element is not present in array")