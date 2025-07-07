# Find sum of the series n - n2/3 + n4/5 - n8/7 .... m terms (1<=n<=4 and 2<=m<=10)

n_value = int(input("Enter the value of n in the series: "))
m_value = int(input("Enter the number of terms you want in the series: "))

sum = 0
for i in range(m_value):
    numerator   = n_value ** 2 ** i
    denominator = 2 * i + 1
    sign        = (-1) ** i

    term = (numerator / denominator) * sign

    sum = sum + term

print('The sum of ',m_value,'terms is: ',sum)

