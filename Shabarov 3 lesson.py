#  Реализовать функцию, принимающую два числа (позиционные аргументы)
#  и выполняющую их деление.
#  Числа запрашивать у пользователя, предусмотреть обработку ситуации
#  деления на ноль.

def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y is'n be a zero"
    except ValueError:
        return "enter only number"
print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))

#  Выполнить функцию, которая принимает несколько параметров,
#  описывающих данные пользователя: имя, фамилия, год рождения,
#  город проживания, email, телефон. Функция должна принимать параметры
#  как именованные аргументы.
#  Осуществить вывод данных о пользователе одной строкой.

def print_user_data(**user_data) -> None:

    print(f'Имя: {user_data.get("name")}, '
          f'фамилия: {user_data.get("surname")},'
          f' год рождения: {user_data.get("birth_year")}, '
          f'город проживания: '
          f'{user_data.get("city")},'
          f' email: {user_data.get("email")}, '
          f'телефон: {user_data.get("phone")}')


if __name__ == '__main__':
    user = {
        'name': 'Ivan',
        'surname': 'Ivanov',
        'birth_year': '1900',
        'city': 'Moscow',
        'email': 'test@moscow-sity.ru',
        'zipcode': '100000',
    }

    print_user_data(**user)

# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму
# наибольших двух аргументов.

def my_func(x, y, z):
    sequence = [x, y, z]
    total = []
    max_1 = max(sequence)
    total.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    total.append(max_2)
    print(sum(total))
my_func(9, 3, 4)

# 4. Программа принимает действительное положительное
# число x и целое отрицательное число y.
# Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной
# функции возведения числа в степень.

def my_func(x, y):
    return 1 / x ** abs(y)
    #return x ** y
print(my_func(4, -4))

# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может
# продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы
# завершается. Если специальный символ введён после нескольких чисел, то
# вначале нужно добавить сумму этих чисел к полученной ранее сумме и после
# этого завершить программу.

def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Input numbers or Q for quit - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')


my_sum()

# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
# и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Используйте написанную ранее
# функцию int_func().

def int_func (*args):
    word = input("Input words ")
    print(word.title())
    return
int_func()
