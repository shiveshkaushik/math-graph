import matplotlib.pyplot as plt

goods_types = ['Essential Goods', 'Standard Goods', 'Luxury Goods']
gst_rates = [
    [5, 5, 5, 5],
    [12, 12, 12, 12],
    [28, 28, 28, 28]
]

quarterly_volumes = [1000000, 2000000, 3000000, 4000000]

fig, ax = plt.subplots(figsize=(10, 6))

for i, rates in enumerate(gst_rates):
    tax_amounts = [volume * rate / 100 for volume, rate in zip(quarterly_volumes, rates)]
    ax.plot(quarterly_volumes, tax_amounts, marker='o', label=goods_types[i])

ax.set_xlabel('Quarterly Volume (₹)')
ax.set_ylabel('GST Tax Amount (₹)')
ax.set_title('Goods and Services Tax (GST) Tax Amount for Different Goods')

ax.legend()

plt.tight_layout()
plt.show()
