import matplotlib.pyplot as plt  

доход = [18000, 25000, 20000, 45000, 19500]
месяцы = ['Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь']
plt.ylabel("Доход")
plt.xlabel("Месяцы")
plt.plot(месяцы, доход)
plt.show()
plt.savefig('./FINANCES/доход.png')