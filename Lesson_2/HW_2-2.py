# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

sum_x_y = int(input('Введите сумму чисел: '))
multip_x_y = int(input('Введите произведение: '))
a = 0
for x in range(sum_x_y):
    for y in range(sum_x_y):
        if x + y == sum_x_y and x * y == multip_x_y:
            a += 1
            print(x, y)
if a == 0:
    print('Не корректные данные!')