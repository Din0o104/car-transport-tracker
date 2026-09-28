def create_car():
    car = {
        'vin': input('Введите VIN: ').strip(),
        'brand': input('Введите марку: ').strip(),
        'model': input('Введите модель: ').strip(),
        'status': input('Введите статус: ').strip(),
        'latitude': float(input('Введите широту: ')),
        'longitude': float(input('Введите долготу: '))
    }

    return car


def show_car(car):
    print(f"\nАвтомобиль: {car['brand']} {car['model']}")
    print(f"VIN: {car['vin']}")
    print(f"Статус: {car['status']}")
    print(f"Координаты: {car['latitude']}, {car['longitude']}")


def update_location(car, latitude, longitude):
    car['latitude'] = latitude
    car['longitude'] = longitude


def update_status(car, status):
    car['status'] = status


car = create_car()

while True:
    print('\n1 — данные автомобиля')
    print('2 — обновить координаты')
    print('3 — изменить статус')
    print('4 — выйти')

    choice = input('Выберите действие: ')

    if choice == '1':
        show_car(car)

    elif choice == '2':
        latitude = float(input('Новая широта: '))
        longitude = float(input('Новая долгота: '))
        update_location(car, latitude, longitude)
        print('Координаты обновлены')

    elif choice == '3':
        status = input('Новый статус: ')
        update_status(car, status)
        print('Статус обновлён')

    elif choice == '4':
        print('Программа завершена')
        break

    else:
        print('Неизвестная команда')