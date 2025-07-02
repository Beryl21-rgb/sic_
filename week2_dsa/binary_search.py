'''def binary_search(target_element,first_element,last_element,arr):
    mid_element = (first_element + last_element)/2
    while first_element <= last_element :
        if arr[mid_element] == target_element:
            return arr[mid_element]
        if arr[mid_element] > target_element:
            last_element = mid_element
            binary_search()
        else :
            first_element = mid_element
            binary_search()


array = [1,2,3,4,5,6,7,8,9,2,33,2,3,24,4,5,55,4,5,6]
arr = sorted(array)
first_element = 0
last_element = len(arr) - 1
target_element = int(input("Enter ther value to be searched: "))
binary_search(target_element,first_element,last_element,arr)
'''

# Bubble Sort
l = [1,3,43,5,46,3]
N = len(l)
for i in range(1,N-1):
    sorted = True
    for j in range(1, N-1):
        if l[j] > l[j+1] :
            l[j], l[j+1] = l[j+1], l[j]
            sorted = False
    if sorted:
        break
print(l)


#  Selection Sort
l = [1,3,43,5,46,3]
N = len(l)
for i in range(2,N):
    element = l[i-1]
    position = i-1
    for j in range(i-1, N):
        if l[j] < element :
            element = l[j]
            position = j
            l[position], l[i-1] = l[i-1], l[position]
print(l)


# l = [1,3,43,5,46,3]
# N = len(l)
# target_element = int(input("Enter the value to be searched"))
# first_element = 0
# last_element = len(l) - 1
# while first_element <= last_element:
#     if first_element or last_element == target_element
#     mid_element = (first_element + last_element)/2
#     if arr[mid_element] == target_element:
#             return arr[mid_element]
#     if arr[mid_element] > target_element:
#         last_element = mid_element
#         binary_search()
#     else :
#         first_element = mid_element


# Orange Partitioning
l = [4,3,8,6,1,1,9,5]
n = l[-1]
k= 0
for i in range(0,len(l)-1):
    if l[i] > n:
        i, n = n, i
print(l)
print(l[-1])
        