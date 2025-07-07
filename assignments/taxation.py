Name = input("Enter your name: ")
EmpID = int(input("Enter your Employee ID: "))
Basic_Monthly_Salary = int(input("Enter your Basic Monthly Salary: "))
Special_Allowances = int(input("Enter your Special Allowances: "))
Bonus_Percentage = int(input("Enter your Bonus Percentage: "))

Gross_Monthly_Salary = Basic_Monthly_Salary + Special_Allowances

Bonus_Amount = (Bonus_Percentage * Gross_Monthly_Salary)/100

Annual_Gross_Salary = (Gross_Monthly_Salary * 12) + Bonus_Amount

print()
print("*" * 10)
print("The Name of the Employee is " + Name)
print("The Employee ID is", EmpID)
print("The Basic Monthly Salary is", "$", Basic_Monthly_Salary)
print("The Special Allowances are", "$", Special_Allowances)
print("The Bonus Percentage is", Bonus_Percentage, "%")
print("The Gross Monthly Salary is", "$", Gross_Monthly_Salary)
print("The Bonus Amount is", "$", Bonus_Amount)
print("The Annual Gross Salary is", "$", Annual_Gross_Salary)
print("*" * 10)


standard_deduction = 50000

taxable_income = Annual_Gross_Salary - standard_deduction

print()
print("*" * 10)
print("Gross Salary is", "$", Gross_Monthly_Salary)
print("Standard Deduction is", "$", standard_deduction)
print("Taxable Income is", "$", taxable_income)
print("*" * 10)

tax = 0
health_education_cess = 4

print()
print("*" * 10)
if taxable_income >= 0 and taxable_income <= 300000:
    print("There is no need to pay tax!!")
    print("Extra 4% tax is added for Health and Education Cess")
    total_tax_payable = tax + health_education_cess
elif taxable_income >= 300001 and taxable_income <= 600000:
    tax = 5
    print("You need to pay 5% tax.")
    print("Extra 4% tax is added for Health and Education Cess")
    total_tax_payable = tax + health_education_cess
elif taxable_income >= 600001 and taxable_income <= 900000:
    tax = 10
    print("You need to pay 10% tax.")
    print("Extra 4% tax is added for Health and Education Cess")
    total_tax_payable = tax + health_education_cess
elif taxable_income >= 900001 and taxable_income <= 1200000:
    tax = 15
    print("You need to pay 15% tax.")
    print("Extra 4% tax is added for Health and Education Cess")
    total_tax_payable = tax + health_education_cess
elif taxable_income >= 1200001 and taxable_income <= 1500000:
    tax = 20
    print("You need to pay 20% tax.")
    print("Extra 4% tax is added for Health and Education Cess")
    total_tax_payable = tax + health_education_cess
elif taxable_income > 1500000:
    tax = 30
    print("You need to pay 30% tax.")
    print("Extra 4% tax is added for Health and Education Cess")
    total_tax_payable = tax + health_education_cess
else:
    print("Your Salary is Invalid!!")

print("Total Tax Payable is", total_tax_payable, "%")
print("*" * 10)