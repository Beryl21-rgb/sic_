# rotate right problem (pronlem 1))
original_str = input("Enter original string: ")
rotated_str = input("Enter string to check if it is rotated of original: ")
if original_str == rotated_str:
    temp_str = rotated_str * 2
    try :
        if temp_str.find(original_str) > 0 :
            print('1')
    except ValueError as err :
        print('-1')
else :
    print("Invalid input")


#Server problem (problem 2)





# 3. 
'''Read N,  X  and Y
X + Y = N

numbers = []
Read N numbers in to numbers

sort numbers (ascending)
p = numbers[y] - nunmbers[y-1] - 1
print p'''

numbers = []
N = int(input("Enter range"))
for i in range(0,N):
    n = int(input("Enter value: "))
    numbers.append(n)
sorted_numbers = numbers.sort()
x_size = int(input())
