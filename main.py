from sort import quicksort
from sort import insertionsort

test_list = [2, 4, 19, 49, 23, 12, 7, 79, 102, 32, 65, 69, 15, 51, 6, 129, -3, 5, -7, 68]

print("base {}".format(test_list))

QS = quicksort.QuickSort(test_list)
print(QS.quicksort(0, len(test_list)-1))

print("base {}".format(test_list))

IS = insertionsort.InsertionSort(test_list)
print(IS.insertionsort())
