class SelectionSort:
    def __init__(self, array):
        self.list_result = array

    def selectionsort(self):
        N = len(self.list_result)
        for i in range(N):
            min_idx = i
            for j in range(i+1, N):
                if self.list_result[min_idx] > self.list_result[j]:
                    min_idx = j
            self.list_result[i], self.list_result[min_idx] = self.list_result[min_idx], self.list_result[i]

        return self.list_result
