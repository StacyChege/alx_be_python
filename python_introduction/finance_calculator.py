monthlyIncome = int(input("Enter your monthly income: "))
totalMonthlyExpenses = int(input("Enter your total monthly expenses: "))

monthlySavings = monthlyIncome - totalMonthlyExpenses
print("Your monthly savings are:", monthlySavings)

projectedAnnualSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)
print("Projected savings after one year, with interest, is: $", projectedAnnualSavings)