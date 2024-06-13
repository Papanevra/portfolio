flights = [
    ['Москва - Питер', 41, '22.08.2005', '14000 rub'],
    ['Москва - Дубай', 0, '29.08.2005', '40000 rub'],
    ['Москва - Казань', 29, '01.09.2005', '25000 rub']
]

while True:
    # Вывод информации о доступных рейсах
    print("===========================================")
    print("Добро пожаловать в приложение 'Бронирование билетов на самолет'!")
    print("Доступные рейсы:")
    for flight in flights:
        print(f"{flight[0]} - свободные места: {flight[1]}")
    print("===========================================")

    # Запрос на выбор рейса
    chosen_flight = input("Выберите рейс из списка: ")
    while not any(chosen_flight in flight[0] for flight in flights):
        print("Такого рейса нет в списке!")
        chosen_flight = input("Выберите рейс из списка: ")

    # Поиск выбранного рейса
    selected_flight = None
    for flight in flights:
        if chosen_flight in flight[0]:
            selected_flight = flight
            break

    # Проверка наличия свободных мест
    if selected_flight and selected_flight[1] > 0:
        print("Места на рейсе доступны. Вы можете забронировать билет.")
        selected_flight[1] -= 1
        print("Билет успешно забронирован!")

        # Вывод информации о бронировании
        print("===========================================")
        print("Информация о бронировании:")
        if selected_flight:
            print(f"Рейс: {selected_flight[0]}")
            print(f"Дата: {selected_flight[2]}")
            print(f"Цена: {selected_flight[3]}")
        print("===========================================")

    else:
        print("На выбранный рейс нет доступных мест.")

        # Поиск альтернативного рейса
        alternative_flight = None
        for flight in flights:
            if flight[1] > 0 and flight != selected_flight:
                alternative_flight = flight
                break

        if alternative_flight:
            print("Предлагаем альтернативный рейс:")
            print(
                f"Рейс: {alternative_flight[0]}, Дата: {alternative_flight[2]}, Цена: {alternative_flight[3]}, Свободные места: {alternative_flight[1]}")
            choice = input(f"Хотите забронировать альтернативный рейс? (да/нет): ")
            if choice.lower() == 'да':
                alternative_flight[1] -= 1
                print("Билет успешно забронирован!")

                # Вывод информации о бронировании
                print("===========================================")
                print("Информация о бронировании:")
                print(f"Рейс: {alternative_flight[0]}")
                print(f"Дата: {alternative_flight[2]}")
                print(f"Цена: {alternative_flight[3]}")
                print("===========================================")
            else:
                print("Вы отказались от альтернативного рейса.")
        else:
            print("К сожалению, нет доступных альтернативных рейсов.")

    # Проверяем, хочет ли пользователь забронировать ещё один билет
    answer = input("Хотите забронировать ещё один билет? (да/нет): ")
    if answer.lower() != 'да':
        break

print("Спасибо за использование нашего сервиса!")
