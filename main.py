#создаем пустой словарь автопарк
fleet = {}

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число (напривер 52.25)")

# функцию добавления автомобиля в автопарк
def create_car(fleet):
    vin = input('Введите VIN-номер: ').strip()
    if vin in fleet:
        print(f"Ошибка: Автомобиль с VIN {vin} уже существует!")
        return
    brand = input('Введите марку:  ').strip()
    model = input('Введите модель: ').strip()  
    status = input('Введите статус: ').strip()
    latitude = get_float_input('Введите широту: ')
    longitude = get_float_input('Введите долготу: ')

    fleet[vin] = {
        'brand': brand, 'model': model,
        'status': status, 'latitude': latitude, 'longitude': longitude
    }
    print('Автомобиль добавлен!')

def show_car(car_data):
    print(f"Автомобиль: {car_data['brand']}, {car_data['model']}")
    print(f"Статус: {car_data['status']}")
    print(f"Координаты: {car_data['latitude']}, {car_data['longitude']}")

def list_cars(fleet, status_filter = None):
    if not fleet:
        print('Автопарк пуст.')
        return

    found_count = 0
    print("\n--- СПИСОК АВТОМОБИЛЕЙ ---")

    for vin, car_data in fleet.items():
        if status_filter is None or car_data['status'].lower() == status_filter.lower():
            print(f"\nVIN: {vin}")
            show_car(car_data)
            found_count += 1
    if found_count == 0:
        print(f"Машин со статусом '{status_filter}' не найдено.")

def find_car(fleet):
    vin = input('Введите VIN-номер для поиска машины: ').strip()
    if vin in fleet:
        print('Машина найдена: ')
        show_car(fleet[vin])
    else:
         print('Машина с таким VIN-номером не найдена. Введите корректный VIN-номер')
def update_car(fleet):
    vin = input('Введите VIN-номер для поиска машины: ').strip()
    if vin in fleet:
        print('Машина с таким VIN-номером найдена!')
        new_status = input('Введите новый статус: ').strip()
        fleet[vin]['status'] = new_status
        print('Статус успешно обновлен')
    else:
        print('Машина с таким VIN-номером не найдена. Введите корректный VIN-номер')
def delete_car(fleet):
    vin = input('Введите VIN-номер для удаления: ').strip()
    if vin in fleet:
        print('Машина с таким VIN-номером найдена!')
        del fleet[vin]
        print('Машина с таким VIN-номером успешно удалена из автопарка!')
    else:
        print('Машина с таким VIN-номером не найдена. Введите корректный VIN-номер')
while True:
    print("\n=== СИСТЕМА УПРАВЛЕНИЯ АВТОПАРКОМ ===")
    print("1 - Добавить автомобиль")
    print("2 - Найти и показать автомобиль")
    print("3 - Изменить статус автомобиля")
    print("4 - Списать (удалить) автомобиль")
    print("5 - Показать автомобили(все / по фильтру)")
    print("6 — Выйти из программы")

    choice = input('Выберите действие: ').strip()

    if choice == '1':
        create_car(fleet)

    elif choice == '2':
        find_car(fleet)
        
    elif choice == '3':
        update_car(fleet)
        
    elif choice == '4':
        delete_car(fleet)

    elif choice == '5':
        mode = input("1 - Показать все машины, 2 - Фильтр по статусу: ").strip()
        if mode == '1':
            list_cars(fleet)
        elif mode == '2':
            desired_status = input("Введите статус (например, free / in_use): ").strip()
            list_cars(fleet, status_filter=desired_status)
        else:
            print("Неверный режим просмотра.")

    elif choice =='6':
        print('Завершение работы программы...')
        break

    else:
        print('Неверный ввод, введите пункт от 1 до 6')
    
