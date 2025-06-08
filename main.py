import random
print("Вітаю! Я загадав ціле число від 1 до 100. За скільки проб ти його вгадаєшь?")
sprob = int(input(())
x = random.randint(1, 100)
counts = 1
while counts <= sprob:
    print("Введіть Ваше припущення: \")
    n = input()
    if n > x:
        print("Занадто велике!")
    elif n < x:
        print("Занадто маленьке!")
    elif n = x:
        print("Ви вгадали! Це число", x)
        exit()
    countdown = sprob - counts
    print("Залишилося спроб:",countdown)
    count += 1
print("Ви програлі, я загадав число",x)