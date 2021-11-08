class QuickSort:
    def __init__(self, list):
        self.list_result = [x for x in list]

    def partition(self, list, start, end):
        i = (start - 1)
        pivot = list[end]
        for j in range (start, end):
            if list[j] <= pivot:
                i = i + 1
                list[i], list[j] = list[j], list[i]
        list[i+1], list[end] = list[end], list[i+1]
        return i+1

    def quicksort(self, list, start, end):
        if len(self.list_result) == 1:
            return self.list_result
        if start < end:
            pi = self.partition(self.list_result, start, end)
            self.quicksort(self.list_result, start, pi-1)
            self.quicksort(self.list_result, pi+1, end)
        return self.list_result


