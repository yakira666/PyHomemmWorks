num = int(input("Введите целое число: "))
for i in range(num, 0, -1):
    for j in range(num):
        a = i - j
        if a > 0:
            print(a, "", end="")
    print()
