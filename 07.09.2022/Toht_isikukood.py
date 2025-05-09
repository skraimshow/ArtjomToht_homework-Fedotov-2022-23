def is_leap_year(year):
    """Проверка високосного года"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def validate_isikukood(isikukood):
    """Проверка корректности персонального кода"""

    # Проверка, что код состоит только из цифр
    if not isikukood.isdigit():
        print("не корректное написание")
        return False

    # Проверка длины кода
    if len(isikukood) != 11:
        print("не корректное количество чисел")
        return False

    # Проверка первого числа (пол)
    first_digit = int(isikukood[0])
    if first_digit < 1 or first_digit > 6:
        print("не корректный пол")
        return False

    # Определение века и года рождения
    if first_digit in [1, 2]:
        century = 1800
    elif first_digit in [3, 4]:
        century = 1900
    elif first_digit in [5, 6]:
        century = 2000

    # Год рождения
    year = century + int(isikukood[1:3])
    if first_digit == 6 and year > 2022:
        print("не корректный год")
        return False

    # Проверка високосного года
    leap_year = is_leap_year(year)

    # Проверка месяца (должен быть в диапазоне от 1 до 12)
    month = int(isikukood[3:5])
    if month < 1 or month > 12:
        print("не корректный месяц")
        return False

    # Проверка дня в месяце с учетом високосного года
    day = int(isikukood[5:7])
    days_in_month = [31, 29 if leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < 1 or day > days_in_month[month - 1]:
        print("не корректное количество дней в месяце")
        return False

    # Проверка контрольной суммы
    first_weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    second_weights = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    # Вычисление первой контрольной суммы
    checksum = sum(int(isikukood[i]) * first_weights[i] for i in range(10)) % 11
    if checksum == 10:
        # Если первая сумма не подходит, используем второй набор весов
        checksum = sum(int(isikukood[i]) * second_weights[i] for i in range(10)) % 11

    # Проверка, совпадает ли контрольная сумма с последней цифрой
    if checksum == 10 or checksum != int(isikukood[-1]):
        print("последние число не совпадает с ответом")
        return False

    # Если все проверки пройдены
    print("Персональный код правильный")
    return True

# Основной цикл программы
while True:
    isikukood = input("Введите персональный код: ")
    if validate_isikukood(isikukood):
        break






