import random
# 1.
random_list : list[int] = []
for _ in range(50):
    random_list.append(random.randint(1, 100))
print(random_list)

# a.
print('bigger than 50 :', list(filter(lambda i: i > 50 , random_list)))

# b.
print('divided by 7 without remainder :',list(filter(lambda i: i % 7 == 0 , random_list)))

# c.
print('two digit numbers only :',list(filter(lambda i: 10 <= i <= 99 , random_list)))

# d.
print('yhidot = asarot :',list(filter(lambda i: 10 <= i <= 99 and (i % 10) == (i// 10) , random_list)))

# e.
print('sum yhidot and asarot = 9 :',list(filter(lambda i: 10 <= i <= 99 and (i % 10) + (i// 10) == 9 , random_list)))

# f.
print('bigger than average :',list(filter(lambda i: i > sum(random_list)/len(random_list) , random_list)))

# g.
max_number = max(random_list)
half_max = max_number / 2
print('bigger than half of the max number in list :',list(filter(lambda i: i > half_max , random_list)))
