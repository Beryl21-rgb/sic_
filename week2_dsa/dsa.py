N = int(input("Enter the number of elemwnts"))
try:
    numbers = [float(num) for num in input().split()]
    print(numbers)
except ValueError as err:
    print("The value entered cannot be converted to float")