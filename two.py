c = int(input("Введіть початок діапазону в Цельсіях: "))
с1 = int(input("Введыть кынець дыапазону в Цельсіях: "))

while c <= с1:
    f= c * 1.8 + 32
    print(f"{c} Цельсий это {f} в Фаренгейтах")
    c += 1
    
    