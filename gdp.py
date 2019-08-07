import matplotlib.pyplot as plt
import numpy as np

years = np.array([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2019])#годы
gdp = np.array([300.2, 543.3, 1075.9, 2862.5, 2862.5, 5979.6, 10289.7, 14958.3])#ВВП

#создаём линейную диаграмму: годы по оси Х, ВВП по оси У
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

#добавляем название для диаграммы
plt.title("Номинальный ВВП")

#добавить подпись к оси Y
plt.ylabel("Млрд $")
plt.show()