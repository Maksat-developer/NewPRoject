food = {"door": "key", "drinks": "Coca-cola", "Shool": "Teacher"}

fast_food = {"Быстрое приготовление": ["Gamburgerov", "Shaurma"]}



get1 = food.get("door")

get2 = fast_food.get("Быстрое приготовление")

keys1 = fast_food.keys()

values = food.values()

items = food.items()

food.update({"Smartphone": "Iphone"})

keys2 = food.keys()

cherta = "|-------------------------------------------------------------------------------------|"

print(get1, " - \n", "\t", food)
print(cherta)
print(get2, " - \n", "\t", fast_food)
print(cherta)
print(values)
print(cherta)
print(items)
print(cherta)

print(food)

