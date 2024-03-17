import matplotlib.pyplot as plt

goods_types_customs = ['Type A', 'Type B', 'Type C']
customs_duty_rates = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [12, 22, 32, 42]
]

incomes = [100000, 500000, 1000000, 5000000]

tax_amounts_type_a = [income * rate / 100 for income, rate in zip(incomes, customs_duty_rates[0])]
tax_amounts_type_b = [income * rate / 100 for income, rate in zip(incomes, customs_duty_rates[1])]
tax_amounts_type_c = [income * rate / 100 for income, rate in zip(incomes, customs_duty_rates[2])]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(incomes, tax_amounts_type_a, marker='o', color='skyblue', label='Type A')
ax.plot(incomes, tax_amounts_type_b, marker='o', color='lightgreen', label='Type B')
ax.plot(incomes, tax_amounts_type_c, marker='o', color='orange', label='Type C')

ax.set_xlabel('Income (₹)')
ax.set_ylabel('Customs Duty Tax Amount (₹)')
ax.set_title('Customs Duty Tax Amount for Different Goods Types')

ax.legend()

plt.tight_layout()
plt.show()
