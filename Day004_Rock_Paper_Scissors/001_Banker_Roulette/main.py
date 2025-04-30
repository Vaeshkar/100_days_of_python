import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_num = random.randint(1, len(friends))
# print(random_num) # expected: 1 to 5

# # expected friends names, random
# if random_num == 1:
#     print(friends[0])
# elif random_num == 2:
#     print(friends[1])
# elif random_num == 3:
#     print(friends[2])
# elif random_num == 4:
#     print(friends[3])
# elif random_num == 5:
#     print(friends[4])

# # Different version using random.choice()
# print(random.choice(friends))

# Different version using random[index]
random_index = random_num
print(friends[random_index])