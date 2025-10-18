list = [7,3,8,1,4,2,6,5]
def insertion_sort(arr):
      for i in range(1, len(arr)):
        j=i
        while arr[j-1] > arr[j] and j>0:
            arr[j - 1], arr[j] = arr[j], arr [j - 1]
            j = j - 1

      return arr
insertion_sort(list)
print(insertion_sort(list))