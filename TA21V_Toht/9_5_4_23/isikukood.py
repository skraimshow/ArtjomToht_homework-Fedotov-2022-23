def validate_estonian_pin(pin: str) -> bool:
    if not pin.isdigit() or len(pin) != 11:
        return False
    control_num = int(pin[-1])
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    total_sum = sum(int(digit) * weight for digit, weight in zip(pin[:-1], weights))
    remainder = total_sum % 11
    if remainder == 10:
        total_sum = sum(int(digit) * weight for digit, weight in zip(pin[:-1], [3, 4, 5, 6, 7, 8, 9, 1, 2]))
        remainder = total_sum % 11
    return control_num == remainder

# Usage example
#pin = "37507280238"
pin = input("Input pin: ")
if validate_estonian_pin(pin):
    print(f"The PIN {pin} is valid!")
else:
    print(f"The PIN {pin} is invalid!")



#1. Нужно добавить возможность повторно не перезапуская программу ввода персонального кода
#2. Чтобы в выводе писалось где ошибки в персональном коде  



#pin = input("Input pin: ")
