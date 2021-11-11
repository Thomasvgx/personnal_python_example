class QuickSort:
    def __init__(self, array):
        self.list_result = [x for x in array]

    def partition(self, array, start, end):
        i = (start - 1)
        pivot = array[end]
        for j in range (start, end):
            if array[j] <= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[end] = array[end], array[i+1]
        return i+1

    def quicksort(self, start, end):
        if len(self.list_result) == 1:
            return self.list_result
        if start < end:
            pi = self.partition(self.list_result, start, end)
            self.quicksort(start, pi-1)
            self.quicksort(pi+1, end)
        return self.list_result


