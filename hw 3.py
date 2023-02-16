class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__memory = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def __eq__(self, other):
        return self.__memory == other.memory

    def __ne__(self, other):
        return self.__memory != other.memory

    def __lt__(self, other):
        return self.__memory < other.memory

    def __gt__(self, other):
        return self.__memory > other.memory

    def __le__(self, other):
        return self.__memory <= other.memory

    def __ge__(self, other):
        return self.__memory >= other.memory

    def make_computations(self):
        a = self.__cpu + self.__memory
        b = self.__cpu - self.__memory
        c = self.__cpu * self.__memory
        d = self.__cpu / self.__memory
        return f'cpu:{self.__cpu} + memory: {self.__memory} = {a}\n' \
               f'cpu:{self.__cpu} - memory: {self.__memory} = {b}\n' \
               f'cpu:{self.__cpu} * memory: {self.__memory} = {c}\n' \
               f'cpu:{self.__cpu} / memory: {self.__memory} = {d}'

    def __str__(self):
        return f'cpu: {self.__cpu} memory {self.__memory}'


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        self.sim_card_number = sim_card_number
        self.call_to_number = call_to_number
        return f'Идет звонок на номер {self.call_to_number} с сим-карты - {self.sim_card_number} ' \
               f'- {self.__sim_cards_list[self.sim_card_number]}'

    def __str__(self):
        return f'Sim-card list: {self.__sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        self.__location = location
        return f'Проложен маршрут до пункта: {self.__location}'


Computer_1 = Computer(3, 5)
Phone_1 = Phone(['MegaCome', "O!", "Beeline"])
# Только первый родительский класс выводится потому что он стоит первым
SmartPhone_1 = SmartPhone(3, 4, ['MegaCome', "O!", "Beeline"])
SmartPhone_2 = SmartPhone(12, 5, ['MegaCome', "O!", "Beeline"])
print(Computer_1)
print(Phone_1)
print(SmartPhone_1)
print(SmartPhone_2)
# Обробока методов класса
# Class Computer
print(Computer_1.make_computations())
# Class Phone
print(Phone_1.call(1, 556271202))
# Class SmartPhone
print(SmartPhone_2.use_gps('ЦУМ'))

print(Computer_1 > SmartPhone_1)
print(Computer_1 < SmartPhone_1)
print(Computer_1 != SmartPhone_1)
print(Computer_1 == SmartPhone_1)
print(Computer_1 >= SmartPhone_1)
print(Computer_1 <= SmartPhone_1)
