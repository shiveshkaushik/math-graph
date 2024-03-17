import matplotlib.pyplot as plt
import numpy as np

income_slabs = [100000, 500000, 1000000, 3000000]
tax_rates = [0.05, 0.20, 0.30, 0.30]

def calculate_tax(income):
    tax = 0
    for i in range(len(income_slabs) - 1):
        if income > income_slabs[i] and income <= income_slabs[i + 1]:
            tax += (income - income_slabs[i]) * tax_rates[i]
            break
        elif income > income_slabs[i + 1]:
            tax += (income_slabs[i + 1] - income_slabs[i]) * tax_rates[i]
    return tax

incomes = np.linspace(100000, 3000000, 100)

taxes = [calculate_tax(income) for income in incomes]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(incomes, taxes, color='skyblue')

ax.set_xlabel('Income (₹)')
ax.set_ylabel('Tax Paid (₹)')
ax.set_title('Tax Paid vs. Income')

ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:,.0f}'.format(x)))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:,.0f}'.format(y)))

plt.tight_layout()
plt.show()
