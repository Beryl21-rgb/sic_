# 1. Check if a year is leap year
year = int(input("Enter the Year that is to be checkked: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a Leap Year")



# 2. Check if a positive integer is a perfect square
positive_integer=int(int(input("Enter the posotive integer: ")))
if positive_integer > 0:
    for perfect_number in range(1,positive_integer):
        if perfect_number*perfect_number==positive_integer:
            print(positive_integer,"is a perfect square")
            
# 3. Find the smallest of 3 distinct numbers
number_1=int(input("Enter the first number: "))
number_2=int(input("Enter the second number: "))
number_3=int(input("Enter the second number: "))
if number_1 < number_2 and number_1 < number_3:
    print(number_1,'is the smallest number')
elif number_2 < number_1 and number_2 < number_3:
    print(number_2,'is the smallest number')
else:
    print(number_3,'is the smallest number')
 
#Taxation
#input
employee_name = input("Enter the employee name: ")
employee_ID = input("Enter the employee ID: ")
monthly_salary = int(input("Enter the basic monthly salary: "))
special_allowance = int(input("Enter the special allowance: "))
bonus = int(input("Enter the bonus (per year in %): "))
bonus/=100
gross_monthly_salary = monthly_salary + special_allowance 
gross_annual_salary = gross_monthly_salary * 12
gross_annual_salary += gross_annual_salary *bonus

#display
print("Employee ID: ",employee_ID)
print("Monthly salary is: ",gross_monthly_salary)
print("Gross annual salary(including bonus): ",gross_annual_salary)

#taxable income and standard deduction 
gross_annual_salary -= 50000
tax = 0
if gross_annual_salary >= 0 and gross_annual_salary <= 300000:
    tax = gross_annual_salary*0
elif gross_annual_salary <= 600000:
    tax = gross_annual_salary*(5/100)
elif gross_annual_salary <= 900000:
    tax  = gross_annual_salary*(10/100)
elif gross_annual_salary <= 1200000:
   tax = gross_annual_salary*(15/100)
elif gross_annual_salary <= 1500000:
    tax = gross_annual_salary*(20/100)
else:
    tax = gross_annual_salary*(30/100)

#rebate     
if gross_annual_salary <= 700000:
    tax = 0
tax += gross_annual_salary*(4/100)

print("Tax applied for you (including health and educaion tax)", tax)
net_annual_salary = gross_annual_salary - tax
print("The net salary after deduction of all taxes: ", net_annual_salary)
