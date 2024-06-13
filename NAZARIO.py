import random

choices = ['камень', 'ножницы', 'бумага']

print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")

while True:
    computer_choice = random.choice(choices)
    player_choice = input("Пожалуйста, сделайте выбор (камень, ножницы, бумага): ").lower()

    if player_choice not in choices:
        print("Некорректный выбор. Пожалуйста, выберите 'камень', 'ножницы' или 'бумага'.")
        continue

    print(f"Компьютер выбрал: {computer_choice}")
    print(f"Вы выбрали: {player_choice}")

    if player_choice == computer_choice:
        print("Ничья!")
    elif (player_choice == 'камень' and computer_choice == 'ножницы') or \
         (player_choice == 'ножницы' and computer_choice == 'бумага') or \
         (player_choice == 'бумага' and computer_choice == 'камень'):
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")

    if input("Хотите сыграть еще раз? (да/нет): ").lower() != 'да':
        break

print("Спасибо за игру! До новых встреч!")