import services


def get_float_input(prompt):
    """Безопасный ввод чисел с плавающей точкой."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число (например, 55.75).")


def print_car(vin, car):
    """Форматированный вывод карточки одного автомобиля."""
    print(f"\nVIN: {vin}")
    print(f"Автомобиль: {car['brand']} {car['model']}")
    print(f"Статус: {car['status']}")
    print(f"Координаты: {car['latitude']}, {car['longitude']}")


def handle_add_car():
    print("\n--- ДОБАВЛЕНИЕ АВТОМОБИЛЯ ---")
    vin = input("Введите VIN: ").strip()
    brand = input("Марка: ").strip()
    model = input("Модель: ").strip()
    status = input("Статус: ").strip()
    lat = get_float_input("Широта: ")
    lon = get_float_input("Долгота: ")

    try:
        services.add_car(vin, brand, model, status, lat, lon)
        print("Автомобиль успешно добавлен в автопарк!")
    except ValueError as error:
        print(f"Ошибка: {error}")


def handle_find_car():
    vin = input("Введите VIN для поиска: ").strip()
    car = services.get_car(vin)
    if car:
        print_car(vin, car)
    else:
        print(f"Автомобиль с VIN '{vin}' не найден.")


def handle_list_cars():
    mode = input("Показать: 1 — Все машины, 2 — Фильтр по статусу: ").strip()
    status_filter = None

    if mode == "2":
        status_filter = input("Введите статус (например, free / in_use): ").strip()
    elif mode != "1":
        print("Неверный режим просмотра.")
        return

    cars = services.get_cars(status_filter)
    if not cars:
        print("Автомобили не найдены.")
        return

    print(f"\nНайдено автомобилей: {len(cars)}")
    for vin, car_data in cars.items():
        print_car(vin, car_data)


def handle_update_status():
    vin = input("Введите VIN для обновления статуса: ").strip()
    new_status = input("Введите новый статус: ").strip()

    try:
        services.update_car_status(vin, new_status)
        print("Статус успешно обновлен!")
    except ValueError as error:
        print(f"Ошибка: {error}")


def handle_delete_car():
    vin = input("Введите VIN для удаления: ").strip()

    try:
        services.delete_car(vin)
        print(f"Автомобиль с VIN '{vin}' успешно списан.")
    except ValueError as error:
        print(f"Ошибка: {error}")


def run_cli():
    """Главный цикл консольного интерфейса."""
    while True:
        print("\n=== СИСТЕМА УПРАВЛЕНИЯ АВТОПАРКОМ ===")
        print("1 — Добавить автомобиль")
        print("2 — Найти автомобиль по VIN")
        print("3 — Изменить статус автомобиля")
        print("4 — Списать (удалить) автомобиль")
        print("5 — Список автомобилей (все / фильтр)")
        print("6 — Выход")

        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            handle_add_car()
        elif choice == "2":
            handle_find_car()
        elif choice == "3":
            handle_update_status()
        elif choice == "4":
            handle_delete_car()
        elif choice == "5":
            handle_list_cars()
        elif choice == "6":
            print("Завершение работы программы...")
            break
        else:
            print("Неверный ввод. Выберите число от 1 до 6.")