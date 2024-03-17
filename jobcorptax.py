import matplotlib.pyplot as plt
import numpy as np

income_slabs = [0, 1000000, 10000000, 50000000]
tax_rates = [0.25, 0.30, 0.30, 0.30]

incomes = np.linspace(0, 50000000, 100)

corporate_taxes = [income * rate for income, rate in zip(incomes, np.interp(incomes, income_slabs, tax_rates))]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(incomes, corporate_taxes, color='skyblue')

ax.set_xlabel('Income (₹)')
ax.set_ylabel('Corporate Tax Paid (₹)')
ax.set_title('Corporate Income Tax Paid vs. Income')

plt.tight_layout()
plt.show()
