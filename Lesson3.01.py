#1.Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
#Посчитать (желательно без использования статистических методов наподобие std, var, mean):
#а) среднее арифметическое,
#б) среднее квадратичное отклонение,
#с) смещенную и несмещенную оценки дисперсий для данной выборки.


import numpy as np

salaries = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

salaries_mean = salaries.sum() / salaries.size
print(f'Среднее арифметическое для данной выборки = {salaries_mean: .2f}')

square=(np.sum((salaries - salaries_mean)**2) / salaries.size)**0.5
print(f'Среднее квадратичное отклонение для данной выборки = {square: .2f}')

np.sum((salaries - salaries_mean)**2) / salaries.size
dispers = np.sum((salaries - salaries_mean)**2) / salaries.size
print(f'Смещенная оценка дисперсии для данной выборки = {dispers: .2f}')

dispers_no =np.sum((salaries - salaries_mean)**2) / (salaries.size - 1)
print(f'Несмещенная оценка дисперсии для данной выборки = {dispers_no: .2f}')