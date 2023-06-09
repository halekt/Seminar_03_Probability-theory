# В университет на факультеты A и B поступило равное количество студентов, 
# а на факультет C студентов поступило столько же, сколько на A и B вместе.
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
# Студент сдал первую сессию. Какова вероятность, что он учится:
# a). на факультете A б). на факультете B в). на факультете C?

a=0.25
b=0.25
c=0.5

pa=0.8
pb=0.7
pc=0.9

pd=a*pa+b*pb+c*pc
print(f'Полная вероятность наступления события  = {pd: .4f}')


pa1=a*pa/pd
print(f'факультет А = {pa1: .4f}')

pa2=b*pb/pd
print(f'факультет B = {pa2: .4f}')

pa3=c*pc/pd
print(f'факультет С = {pa3: .4f}')