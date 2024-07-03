# Цикл for. Элементы списка. Полезные функции в цикле.

# Задача "Всё не так уж просто"

# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15].
# Программа, используя исходный список, составляет второй список primes содержащий только простые числа.
# А также третий список not_primes, содержащий все непростые числа.
# И выводит списки primes и not_primes на консоль.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print('Исходный список чисел:')
print(numbers)

primes = []
not_primes = []
for i in range(1, len(numbers)):
    is_prime = True
    for j in range(1, i):
        if numbers[i] % numbers[j] == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print('\nСписок простых чисел:')
print(primes)
print('Список непростых чисел:')
print(not_primes)

print('\nРабота завершена.')