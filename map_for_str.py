
# 4.
fruits = ["Apple", "Banana", "Orange", "Mango" ,"Strawberry","Pineapple ","Grapes","Watermelon"]
print(fruits)

# a.
print("reversed letters order: ", list(map(lambda fruit: fruit[::-1], fruits)))

# b.
print("first letter in a word: ", list(map(lambda fruit: fruit[0], fruits)))

# c.
print("fruit in upper: ", list(map(lambda fruit: fruit.upper(), fruits)))

# d.
print("middel letter in fruit: ", list(map(lambda fruit:  fruit[len(fruit) // 2] if len(fruit) % 2 != 0 else fruit[len(fruit) // 2 - 1], fruits)))

# e
print("if fruit end with 's': ", list(map(lambda fruit: fruit + '!' if fruit.endswith("s") else fruit , fruits)))