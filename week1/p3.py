# 1. Find the biggest digit in a number
number = input("Enter the number to find its highest digit: ")
list_num = []
for i in number:
    list_num.append(int(i))
biggest_number = 0
for number in list_num:
    if number > biggest_number:
        biggest_number = number
print('The biggest number in the digit is ',biggest_number)


# 2. Find the 2nd smallest digit in a number
number = input("Enter the number to find its highest digit: ")
list_num = []
for i in number:
    list_num.append(int(i))
list_num.sort()
new_list = list(set(list_num))
print('The Second smallest number in the digit is',new_list[1])


# 5. Find the Nth Fibo (HemaChandra) term. Assume 1st 2 terms are 1 and 2
fib_range = int(input("Enter the number of fibonacci term to be found: "))
first_term = 1
second_term = 2
for i in range(1,fib_range-1):
    fib = first_term + second_term
    first_term = second_term
    second_term = fib
print(fib)
