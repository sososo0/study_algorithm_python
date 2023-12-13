array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8] 

for i in range(len(array)):
    minIndex = i
    for j in range(i+1, len(array)):
        if array[j] < array[minIndex]:
            minIndex = j 
    array[i], array[minIndex] = array[minIndex], array[i] 
    
print(array)