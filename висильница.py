import random

words = 'аист акула бабуин барсук бобр бык верблюд волк воробей гусь заяц зебра змея коала корова кот крокодил крыса лиса лев медведь муравей носорог обезьяна овца олень панда паук питон пчела рысь свинья скунс слон тигр утка феникс черепаха шакал ящерица'.split()
max_attempts = 7

print("Добро пожаловать в игру 'Виселица'! Угадайте слово.")

while True:
    missed_letters = []
    correct_letters = []
    secret_word = random.choice(words).upper()
    game_is_done = False

    while not game_is_done:
        print("\nОшибочные буквы:", " ".join(missed_letters))
        blanks = [letter if letter in correct_letters else '_' for letter in secret_word]
        print("Слово: ", " ".join(blanks))

        guess = input("Введите букву: ").upper()
        while len(guess) != 1 or guess in missed_letters + correct_letters or not ('А' <= guess <= 'Я'):
            if len(guess) != 1:
                print("Пожалуйста, введите одну букву.")
            elif guess in missed_letters + correct_letters:
                print("Вы уже пробовали эту букву. Попробуйте другую.")
            elif not ('А' <= guess <= 'Я'):
                print("Пожалуйста, введите русскую букву.")
            guess = input("Введите букву: ").upper()

        if guess in secret_word:
            correct_letters.append(guess)
            if all(letter in correct_letters for letter in secret_word):
                print(f"Отлично! Вы угадали слово: {secret_word}")
                game_is_done = True
        else:
            missed_letters.append(guess)
            if len(missed_letters) == max_attempts:
                print("\nОшибочные буквы:", " ".join(missed_letters))
                print("Слово: ", " ".join(secret_word))
                print(f"Вы исчерпали все попытки! Загаданное слово было: {secret_word}")
                game_is_done = True

    if not input("Хотите сыграть еще раз? (да/нет): ").lower().startswith('д'):
        break

print("Спасибо за игру! До новых встреч!")
