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


# 3. Count number of Prime digits in a number
digit = input("Enter the digits to find the number of primes in it: ")
numbers = []
count = 0
for num in digit:
    number = int(num)
    for n in range (2, num):
        if num%n == 0:
            count +=1
            break
print(count)


# 6. Find sum of thye series n - n2/3 + n4/5 - n8/7 .... m terms (1<=n<=4 and 2<=m<=10)
n_element = int(input("Enter the N-th element: "))
m_element = int(input("Enter the M-th element: "))
sum_of_series = 0
if (n_element >= 1 or n_element <=4) and (m_element >= 2 or m_element <= 10):
    for i in range (0, m_element+1):
        numerator = n_element ** (2*i)
        denomenator = (2 * i)+1
        sign = -1**i
        sum_of_series += (numerator / denomenator) * sign
print(sum_of_series)
        
    
#4. Print the Prime numbers in decreasing order between m and n (m < n)
n = int(input("Enter the starting range: "))
m = int(input("Enter the endig range "))
prime_numbers = []
for num in range(n, m+1):
    for i in range(i+1,m+1):
        if num % i == 0:
            prime_numbers.append(num)
print(prime_numbers)
