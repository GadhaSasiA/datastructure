def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
     for j in range(0,n-i-1):
         if arr[j]> arr[j+1]:
             arr[j],arr[j+1]==arr[j+1],arr[j]

size = int(input("enter the size:"))
my_sort = []
for i in range(size):
    elements = int(input("Enter the elements"))
    my_sort.append(elements)

print("Unsorted array:",my_sort)
bubble_sort(my_sort)
print("Sorted array:",my_sort)
