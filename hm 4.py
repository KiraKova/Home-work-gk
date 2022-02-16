ch = int(input("Введите число: "))
x = 0
while(ch):
    if ch%10 > x:
        x = ch%10
    ch//=10

print(x)