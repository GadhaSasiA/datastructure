def bubble_sort(arr):
    n=len(arr)

    for i in range(n-1):
      for j in range(0,n-i-1):
         if arr[j]>arr[j+1]:
            arr[j],arr[j+1]==arr[j+1],arr[j]


my_list=[23,45,67,32,15,43]
print("original list",my_list)

bubble_sort(my_list)
print("sortes",my_list)


















