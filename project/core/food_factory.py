class FoodFactory:
    food_types = {
        "Cake": Cake,
        "Bread": Bread
    }

    def create_food(self, food_type: str, name: str, price: float):
        return self.__class__.food_types[food_type](name, price)

