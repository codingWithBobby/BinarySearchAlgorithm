listData = [45, 125, 133, 192, 212, 256, 281, 283, 311, 358, 418 , 424, 451, 483, 503, 567, 597, 602, 628, 651, 652, 677, 643, 778, 800, 805, 823, 842, 930, 945]

def binarySearch(listData, value):
	low = 0
	high = len(listData) - 1
	while (low <= high):
		mid = round((low+high)/2)
		if (listData[mid] == value):
			return mid
		elif (listData[mid] < value):
			low = mid + 1
		else:
			high = mid - 1
	return 'Number is not in the Data'

print(binarySearch(listData, 418))
