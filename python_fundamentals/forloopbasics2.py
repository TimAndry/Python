def biggieSize(arr):
  for i in range(0, len(arr)):
    if arr[i] > 0:
      arr[i] = "big"
  return arr 

biggieSize([1,2,3,-8,-7,3])


def countPositives(arr):
  count = 0
  for i in range(0, len(arr)):
    if arr[i] > 0:
      count = count + 1
  arr[len(arr)-1] = count
  return arr

countPositives([1,2,-3,-8,9,2,4,-5])


def sumTotal(arr):
  sum = 0
  for i in range(0, len(arr)):
    sum = sum + arr[i]
  return sum

sumTotal([1,2,3,4])


def average(arr):
  sum = 0
  for i in range(0, len(arr)):
    sum = sum + arr[i]
  avg = sum / len(arr)
  return avg

average([1,2,3,4])


def length(arr):
  return len(arr)

length([1,1,1,1,1])


def minimum(arr):
  mini = 0
  if len(arr) == 0:
    return 'false'
  for i in range(0, len(arr)):
    if arr[i] < mini:
      mini = arr[i]
  print(mini)
  return mini


minimum([1,2,3,4,5,6,0,2,3,-7,-4])


def maximum(arr):
  maxi = 0
  if len(arr) == 0:
    return 'false'
  for i in range(0, len(arr)):
    if arr[i] > maxi:
      maxi = arr[i]
  print(maxi)
  return maxi


maximum([1,2,3,4,5,6,0,2,3,-7,-4])


def ultimateAnalyze(arr):
  sumTotal = 0
  maxi = 0
  mini = 0
  length = len(arr)
  avg = 0
  for i in range(0, len(arr)):
    if arr[i] > maxi:
      maxi = arr[i]
    if arr[i] < mini:
      mini = arr[i]
    sumTotal = sumTotal + arr[i]
  avg = sumTotal/length
  dictionary = {"minimum":mini,"maximum":maxi, "sum":sumTotal, "average":avg, "length":length}
  return dictionary

ultimateAnalyze([3,3,3,3,3,3,3,3,3,10,18])


def reverseList(arr):
  for i in range(0, int(len(arr)/2)):
    #int must be used when making calculations in range parameters to convert float result into integer value
    temp = arr[i]
    arr[i] = arr[len(arr)-1-i]
    arr[len(arr)-1-i] = temp
  print(arr)

reverseList([1,2,3,4,5,6,8])