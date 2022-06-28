def heap(array, a, b):
	largest = b 
	l = 2 * b + 1
	root = 2 * b + 2	 

	if l < a and array[b] < array[l]:
		largest = l

	if root < a and array[largest] < array[root]:
		largest = root

	if largest != b:
	    array[b], array[largest] = array[largest], array[b]
	    heap(array, a, largest)


def Heap_Sort(array):
	a = len(array)

	for b in range(a // 2 - 1, -1, -1):
		heap(array, a, b)

	for b in range(a-1, 0, -1):
		array[b], array[0] = array[0], array[b] 
		heap(array, b, 0)

 
array = [ 7, 2, 5, 6, 3, 1, 8, 4]
print(" original array : ", array)
Heap_Sort(array)
a = len(array)
print ("Array after sorting : ", array)
