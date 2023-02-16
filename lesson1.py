
class Transport:
    def __init__(self, the_model, the_year, the_color):
        # object attributes/fields
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        # constructor matching
        super().__init__(the_model, the_year, the_color)


class Car(Transport):
    # class atributes
    number_of_wheels = 4
    counter = 0

    # constructor
    def __init__(self, the_model, the_year, the_color, penalties=0):
        # object attributes/fields
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    number_of_wheels = 10
    def __init__(self, the_model, the_year, the_color, penalties=0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, type, weight):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity}')
        else:
            print(f'Cargo of {type} was successfully loaded on '
                  f'{self.model} with weight {weight}')


print(f'We need {Car.number_of_wheels * 10 * 5000} soms for winter lastics.')
print(f'Was created: {Car.counter} cars.')

bmw_car = Car('BMW X7', 2022, 'White')
print(bmw_car)
print(f'Model: {bmw_car.model} year: {bmw_car.year} color: {bmw_car.color} '
      f'penalties: {bmw_car.penalties}')

nissan_car = Car(the_year=2020, the_model='Nissan Silvia',
                 the_color='Blue', penalties=900)
print(f'Model: {nissan_car.model} year: {nissan_car.year} color: {nissan_car.color} '
      f'penalties: {nissan_car.penalties}')
# nissan_car.color = 'Black'
nissan_car.change_color('Black')
print(f'Model: {nissan_car.model} year: {nissan_car.year} new color: {nissan_car.color} '
      f'penalties: {nissan_car.penalties}')
nissan_car.drive('Osh')
bmw_car.drive('Tokmok')

print(f'Was created: {Car.counter} cars.')

boeing_plane = Plane('Boeing 347', 2023, 'White')
print(f'Model: {boeing_plane.model} year: {boeing_plane.year} '
      f'color: {boeing_plane.color}')

volvo_truck = Truck('Volvo 345', 1999, 'Brown', 1200, 25000)
print(f'Model: {volvo_truck.model} year: {volvo_truck.year} '
      f'color: {volvo_truck.color} penalties: {volvo_truck.penalties} '
      f'load capacity: {volvo_truck.load_capacity}')
volvo_truck.load_cargo('Apples', 30000)
volvo_truck.load_cargo('Apples', 20000)
volvo_truck.drive('LA')
print(f'Truck has {Truck.number_of_wheels} wheels')
Truck.number_of_wheels = 12
print(f'Truck has {Truck.number_of_wheels} wheels')





