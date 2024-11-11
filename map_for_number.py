import random
# 3.
random1_list : list[int] = []
for _ in range(20):
    random1_list.append(random.randint(-50, 50))
print(random1_list)

# a.
print("power 3: ", list(map(lambda x: x ** 3, random1_list)))

# b.
print("only hahadot: ", list(map(lambda x:abs(x) % 10, random1_list)))

# c.
print("fahrenheit: ", list(map(lambda x:x * 9/5 + 32, random1_list)))

# d.
print(list(map(lambda y:"positive" if y > 0 else "negative" , random1_list)))
