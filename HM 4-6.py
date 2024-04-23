# Напишите функцию, которая принимает кортеж num_tuple из 10 цифр num_tuple,
# и возвращает строку этих чисел в виде номера телефона str_phone.
# Например (Ввод --> Вывод) :
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)  => "(123) 456-7890"

def create_phone_number(num_tuple):
    str_phone = ''
    stroka_num_tuple = str(num_tuple)
    for i in range(1, len(stroka_num_tuple) - 1):
        if stroka_num_tuple[i] != ',' and stroka_num_tuple[i] != ' ':
            str_phone = str_phone + (stroka_num_tuple[i])
    str_phone = '(' + str_phone[0:3] + ') ' + str_phone[3:6] + '-' + str_phone[6:10]
    return str_phone

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 0),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 2, 3, 0, 5, 6, 0, 8, 9, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
]

test_data = [
    "(123) 456-7890", "(111) 111-1111", "(023) 056-0890", "(000) 000-0000"
]


for i, d in enumerate(data):
    assert create_phone_number(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')

num_tuple = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
str_phone = ''
stroka_num_tuple = str(num_tuple)
for i in range(1, len(stroka_num_tuple)-1):
    if stroka_num_tuple[i] != ',' and stroka_num_tuple[i] != ' ':
        str_phone = str_phone + (stroka_num_tuple[i])
str_phone = '(' + str_phone[0:3] + ') ' + str_phone[3:6] + '-' + str_phone[6:10]
print(str_phone)


print('\n            Задание 7')
lst = [1, 9, 5, 4, 8, 2]
k = 0
# сосчитаем сколько нулей в списке
for i in range(0, len(lst)):
    if lst[i] == 0:
        k = k + 1
# введем вспомогательный список
lst2 = []
# если элемент строки lst не равен нулю, помещаем его в конец списка lst2
for i in range(0, len(lst)):
    if lst[i] != 0:
        lst2.append(lst[i])
# в хвост списка lst2 добавляем k нулей
for i in range(1, k + 1):
    lst2.append(0)
lst = lst2
print(lst)
