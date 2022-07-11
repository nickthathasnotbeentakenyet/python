import matplotlib.pyplot as plot
import numpy as np

осьx = np.array([11, 4, 2, 8, 9, 24, 41])
осьy = np.array([1,2,3,4,5,6,7])
дни = ['Понедельник','Вторник','Среда','Четверг', 'Пятница','Суббота','Воскресенье']
plot.yticks(осьy, дни)
plot.plot(осьx, осьy)
plot.savefig('plot.png')