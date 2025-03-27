def calculate_tax(income, tax_rate):
    tax = income - tax_rate  #should be tax = income * tax_rate
    return tax

income = 50000
tax_rate = 0.2  
tax = calculate_tax(income, tax_rate)
print(f"The calculated tax is: {tax}")