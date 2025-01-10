num = int(input("Write number: "))
i = 0
suma = 0

while num > 0:
    suma += num % 10
    num //= 10
    i += 1

print(f"Кількість чисел {i}")
print(f"Сума чисел{suma}")