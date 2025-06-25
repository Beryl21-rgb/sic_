# Check if a year is leap year
year = int(input("Enter the Year that is to be checkked: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a Leap Year")

#Check if a positive integer is a perfect square
positive_integer=int(int(input("Enter the posotive integer: ")))
if positive_integer > 0:
    for perfect_number in range(1,positive_integer):
        if perfect_number*perfect_number==positive_integer:
            print(positive_integer,"is a perfect square")
            
#Find the smallest of 3 distinct numbers
number_1=int(input("Enter the first number: "))
number_2=int(input("Enter the second number: "))
number_3=int(input("Enter the second number: "))
if number_1 < number_2 and number_1 < number_3:
    print(number_1,'is the smallest number')
elif number_2 < number_1 and number_2 < number_3:
    print(number_2,'is the smallest number')
else:
    print(number_3,'is the smallest number')
 
