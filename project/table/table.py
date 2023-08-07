from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.core.validator import Validator
from project.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value < self.min_table_number or value > self.max_table_number:
            raise ValueError(self.table_number_error_message)
        self.__table_number = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity cannot be less than or equal to zero!")
        self.__capacity = value

    @property
    @abstractmethod
    def min_table_number(self):
        pass

    @property
    @abstractmethod
    def max_table_number(self):
        pass

    @property
    @abstractmethod
    def table_number_error_message(self):
        pass

    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        ordered_food = sum(x.price for x in self.food_orders)
        ordered_drinks = sum(x.price for x in self.drink_orders)
        return ordered_food + ordered_drinks

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            result = f"Table: {self.table_number}\n"
            f"Type: {self.__class__.__name__}"
            f"Capacity: {self.capacity}"
            return result









