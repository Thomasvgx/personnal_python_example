class InsertionSort():
    def __init__(self, array):
        self.list = array

    def insertionsort(self):
        for i in range(1, len(self.list)):
            key = self.list[i]
            j = i-1
            # print(self.list)
            while j >= 0 and key < self.list[j]:
                self.list[j+1] = self.list[j]
                j -= 1
            self.list[j+1] = key
        return self.list
