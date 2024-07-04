# Условная конструкция. Операторы if, elif, else.

# Задача "Все ли равны?"

# Программа выводит количество одинаковых чисел среди трёх введённых.

number = [1, 2, 3]
number_name = ['первое', 'второе', 'третье']

print('Введите, пожалуйста, по очереди три произвольных целых числа.')
for i in range(3):
    while True:
        output_str = 'Введите ' + number_name[i] + ' число: '
        input_str = input(output_str)
        if input_str.isdigit():
            number[i] = int(input_str)
            break
        else:
            print('К сожалению, Вы ошиблись.\nВведенные Вами данные не являются целым числом.')

first, second, third = number[0], number[1], number[2]

print('\nКоличество одинаковых чисел среди введённых:')
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)

print('\nБлагодарю Вас! Работа завершена.')