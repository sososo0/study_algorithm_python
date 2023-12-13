array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8] 

def bubbleSort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

bubbleSort(array)            
print(array)