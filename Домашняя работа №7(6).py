a = int(input("Введите результат 1 дня: "))
b = int(input("Введите число желаемого результата: "))

day = 1
while a < b:
    if a<b:
        # print(day, "-й день:", a)
        day += 1
        a *= 1.1
    else:
        break
print("Ответ: на", day, "спортсмен достиг результата - не менее 3 км.")

