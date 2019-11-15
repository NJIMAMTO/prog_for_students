#6枚目の課題 fizzbuzz問題

#3と5を15と解釈して解く
for i in range(1, 101):
    if i % 15 == 0:
        print("Fizz Buzz!")
    elif i % 3 == 0:
        print("Fizz!")
    elif i % 5 == 0:
        print("Buzz!")
    else:
        print(i)

#3と5をそのままの条件で書く
for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("Fizz Buzz!")
    elif i % 3 == 0:
        print("Fizz!")
    elif i % 5 == 0:
        print("Buzz!")
    else:
        print(i)