isikukood = input("Введите персональный код: ")
#print(isikukood)
# Проверяет были ли введены только числа или нет 
try:
    val = int(isikukood)
except ValueError:
    print("That's not an int!")
# Проверяет длинну ввода ц
if len(isikukood) == 11:
    print("good")
else:
    print("bad")
# Проверяет входит ли первое число в диапозон
if  1 <= int(isikukood[0]) and int(isikukood[0])<= 6:
    print("good first number")
else:
    print("bad first number")



print(isikukood[1:7])

