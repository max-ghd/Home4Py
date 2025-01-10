import random

num = 1

per_plus = 0
per_minus = 0
per_zero = 0
per_par = 0
per_niepar = 0
while num <= 100:
    rand = random.randint(-100, 100)
    print(f"{num}: {rand}")
    num += 1
    if 0 > rand:
        per_minus = per_minus+ 100/100
    elif 0< rand:
        per_plus +=100/100
    elif 0 == rand:
        per_zero += 100/100
    
    if rand % 2 == 0 :
        per_par += 100/100
    else:
        per_niepar += 100/100
print("\n")


print(f"{per_minus}% числ менших нуля")
print(f"{per_plus}% числ більше нуля")
print(f"{per_zero}% числа = 0")
print(f"{per_par}% парних чисел")
print(f"{per_niepar}% непарних чисел")
print("\n")

'''
num = 100
100 = 100%
rand_minus = ?
per = 
'''
    

        




  