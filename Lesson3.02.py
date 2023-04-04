# Задача 2. В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, 
# из которых 5 белых. Из первого ящика вытаскивают случайным образом два мяча, из второго - 4 мяча. 
# Какова вероятность того, что 3 мяча белые?


import numpy as np

def combinations(n, k):
    return (np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k)))

t1=combinations(8, 2)
t2=combinations(12, 4)


a1=combinations(5, 2)
a2=combinations(5, 1)
b2=combinations(7, 3)
p1=a1/t1
p2=(a2*b2)/t2
pa=p1*p2
print(f'2 белых из 2 и 1 белый из 4 = {pa: .4f}')


a1=combinations(5, 1)
b1=combinations(3, 1)
a2=combinations(5, 2)
b2=combinations(7, 2)
p1=(a1*b1)/t1
p2=(a2*b2)/t2
pb=p1*p2
print(f'1 белый из 2 и 2 белых из 4= {pb: .4f}')


a1=combinations(3, 2)
a2=combinations(5, 3)
b2=combinations(7, 1)
p1=a1/t1
p2=(a2*b2)/t2
pc=p1*p2
#print("2. 0 из 2х белые и 3 из 4 белые",pc)
print(f'0 белых из 2 и 3 белых из 4= {pc: .4f}')

p=pa+pb+pc
print(f'вероятность того, что 3 мяча белые {p: .4f}')