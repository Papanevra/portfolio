import random

print("Добро пожаловать в игру 'Угадай число'!")

while True:
    number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Я загадал число от 1 до 100. Попробуйте угадать!")

    while not guessed:
        guess = int(input("Введите ваше предположение: "))
        attempts += 1

        if guess < number:
            print("Слишком мало. Попробуйте снова.")
        elif guess > number:
            print("Слишком много. Попробуйте снова.")
        else:
            print(f"Поздравляем! Вы угадали число за {attempts} попыток.")
            guessed = True

    if input("Хотите сыграть еще раз? (да/нет): ").lower() != 'да':
        break

print("Спасибо за игру! До новых встреч!")
