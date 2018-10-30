def selectionSort(arr):
  for i in range(0, len(arr)):
    temp = arr[i]
    for j in range(i, len(arr)):
      if arr[j] < temp:
        temp = arr[j]
        arr[j] = arr[i]
      arr[i] = temp
  print(arr)
*10)




 7 4 3 1 5 9 6
 4 7 3 1 5 9 6
 3 7 4 1 5 9 6
 1 7 4 3 5 9 6...
 1 4 7 3 5 9 6...
 1 3 7 4 5 9 6
 1 3 4 7 5 9 6
 1 3 4 5 7 9 6...
 1 3 4 5 6 9 7