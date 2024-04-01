num = []

for i in range(6):
    n = int(input("Ingrese un numero: "))
    num.append(n)


multiplos = []

for num in num:
    if num % 2 == 0:
        multiplos.append(num)

print("Los multiplos de 2 son:", multiplos)
