from project.bakery import Bakery

bakery = Bakery("Random Name")

# errors
#print(bakery.add_food("Cake", "Carrot Cake", 2.4))
# print(bakery.add_food("Cake", "", 2.4))
#print(bakery.add_food("Cake", "kakaka", 0))
print(bakery.add_drink("Tea", "Ice", 300, "Dabov"))
print(bakery.add_drink("Water", "Spring", 250, "Gorna Banya"))
print(bakery.add_drink("Water", "Mineral", 500, "Bankya"))
print(bakery.add_table("InsideTable", 30, 10))
# InsideTable is between 1- 50 - Error
#print(bakery.add_table("InsideTable", 51, 15))
# OutsideTable between 51 -100
print(bakery.add_table("OutsideTable", 55, 15))
# currently we have 1 table number 30 for 15 people


print(bakery.add_food("Cake", "Carrot Cake", 3.4))
print(bakery.add_food("Bread", "BananaBread", 5.4))
print(bakery.add_food("Cake", "Chocolate Cake", 6.4))
# test order food
print(bakery.reserve_table(10))
print(bakery.reserve_table(5))
print(bakery.order_food(55, "Carrot Cake", "BananaBread", "Chocolate Cake", "Rice Pudding", "Pancakes"))
print(bakery.order_drink(55, "Spring", "Mineral", "Ice", "Coke", "Fanta"))
print(bakery.leave_table(55))

print(bakery.add_table("InsideTable", 13, 15))
print(bakery.add_table("OutsideTable", 59, 18))
print(bakery.get_free_tables_info())

print("---------------")

print(bakery.get_total_income())

