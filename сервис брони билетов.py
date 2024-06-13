flights_data = [
    ['Москва - Сочи', 35, '15.07.2024', '12000 руб.'],
    ['Москва - Париж', 10, '20.07.2024', '45000 руб.'],
    ['Москва - Токио', 25, '05.08.2024', '75000 руб.']
]

def show_available_flights():
    print("===========================================")
    print("Добро пожаловать в систему бронирования авиабилетов!")
    print("Список доступных рейсов:")
    for flight in flights_data:
        print(f"{flight[0]} - свободных мест: {flight[1]}")
    print("===========================================")

def find_flight_by_route(route):
    for flight in flights_data:
        if route in flight[0]:
            return flight
    return None

def get_alternative_flight(excluded_flight):
    for flight in flights_data:
        if flight[1] > 0 and flight != excluded_flight:
            return flight
    return None

while True:
    show_available_flights()

    selected_route = input("Введите маршрут рейса из списка: ")
    chosen_flight = find_flight_by_route(selected_route)

    while not chosen_flight:
        print("Такого рейса нет в списке!")
        selected_route = input("Попробуйте снова: ")
        chosen_flight = find_flight_by_route(selected_route)

    if chosen_flight[1] > 0:
        print("На данном рейсе есть свободные места. Процесс бронирования начат.")
        chosen_flight[1] -= 1
        print("Вы успешно забронировали билет!")

        print("===========================================")
        print("Детали вашего бронирования:")
        print(f"Маршрут рейса: {chosen_flight[0]}")
        print(f"Дата отправления: {chosen_flight[2]}")
        print(f"Стоимость: {chosen_flight[3]}")
        print("===========================================")

    else:
        print("К сожалению, на выбранный рейс нет свободных мест.")
        alternative_flight = get_alternative_flight(chosen_flight)

        if alternative_flight:
            print("Мы можем предложить вам альтернативный рейс:")
            print(f"Маршрут: {alternative_flight[0]}, Дата отправления: {alternative_flight[2]}, Стоимость: {alternative_flight[3]}, Свободных мест: {alternative_flight[1]}")
            alternative_choice = input("Хотите забронировать этот рейс? (да/нет): ")
            
            if alternative_choice.lower() == 'да':
                alternative_flight[1] -= 1
                print("Билет на альтернативный рейс успешно забронирован!")

                print("===========================================")
                print("Детали вашего бронирования:")
                print(f"Маршрут рейса: {alternative_flight[0]}")
                print(f"Дата отправления: {alternative_flight[2]}")
                print(f"Стоимость: {alternative_flight[3]}")
                print("===========================================")
            else:
                print("Вы отказались от бронирования альтернативного рейса.")
        else:
            print("К сожалению, нет доступных альтернативных рейсов.")

    another_ticket = input("Хотите забронировать еще один билет? (да/нет): ")
    
    if another_ticket.lower() != 'да':
        break

print("Большое спасибо за использование нашей системы бронирования!")
