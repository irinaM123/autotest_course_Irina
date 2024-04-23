# Напишите функцию sum_digits, которая принимает положительное число num,
# и возвращает сумму цифр our_sum.
# Например (Ввод --> Вывод) :
#
# 39 --> 12
# 999 --> 27
# 4 --> 4

def sum_digits(num):
    # Переведем число num в строку
    s = str(num)
    our_sum = 0
    # в цикле от 0 до длины строки num суммируем к our_sum символ с индексом i
    for i in range(0, len(s), 1):
        our_sum = our_sum + int(s[i])
    return our_sum

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    39, 4, 25, 999, 5050, 222333444
]

test_data = [
    12, 4, 7, 27, 10, 27
]


for i, d in enumerate(data):
    assert sum_digits(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')

