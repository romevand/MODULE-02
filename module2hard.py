# Дополнительное практическое задание по модулю: "Основные операторы".

# Задача "Слишком древний шифр"

# Программа для любого целого числа, большего 2, вычисляет пароль, представляющий собой
# последовательность пар следующих друг за другом целых положительных чисел,
# сумме которых кратно введенное число.

def input_int ():
    while True:
        input_str = input ("\nВведите, пожалуйста, произвольное целое число, большее 2: ")
        if input_str.isdigit ():
            number = int (input_str)
            if number > 2:
                break
            else:
                print ('К сожалению, Вы ошиблись.\nВведенное Вами число меньше 3.')
        else:
            print ('К сожалению, Вы ошиблись.\nВведенные Вами данные не являются целым числом.')
    return (number)

print ("\nПрограмма для любого целого числа, большего 2, вычисляет пароль, представляющий собой")
print ("последовательность пар следующих друг за другом целых положительных чисел,")
print ("сумме которых кратно введенное число.")

n = input_int ()
matrix = []
for j in range (1, n):
    for k in range (j + 1, n):
        if n % (j + k) == 0:
            matrix.append (str (j) + str (k))

print ("\nПароль:", "".join (matrix))

print ('\nРабота завершена.')