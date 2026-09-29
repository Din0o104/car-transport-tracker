#создаем пустой словарь автопарк
fleet = {}

# функцию добавления автомобиля в автопарк
def create_car(fleet):
    vin = input('Введите VIN-номер: ').strip()
    if vin in fleet:
        print(f"Ошибка: Автомобиль с VIN {vin} уже существует!")
        return
    brand = input('Введите марку:  ').strip()
    model = input('Введите модель: ').strip()  
    status = input('Введите статус: ').strip()
    latitude = float(input('Введите широту: '))
    longitude = float(input('Введите долготу: '))

    fleet[vin] = {
        'brand': brand, 'model': model,
        'status': status, 'latitude': latitude, 'longitude': longitude
    }
    print('Автомобиль добавлен!')

def show_car(car_data):
    print(f"Автомобиль: {car_data['brand']}, {car_data['model']}")
    print(f"Статус: {car_data['status']}")
    print(f"Координаты: {car_data['latitude']}, {car_data['longitude']}")

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
    print("1 — Добавить автомобиль")
    print("2 — Найти и показать автомобиль")
    print("3 — Изменить статус автомобиля")
    print("4 — Списать (удалить) автомобиль")
    print("5 — Выйти из программы")

    choice = input('Выберите действие: ').strip()

    if choice == '1':
        create_car(fleet)

    elif choice == '2':
        find_car(fleet)
        
    elif choice == '3':
        update_car(fleet)
        
    elif choice == '4':
        delete_car(fleet)
        
    elif choice =='5':
        print('Завершение работы программы...')
        break

    else:
        print('Неверный ввод, введите пункт от 1 до 5')
    
