import random


def get_unique_list_numbers(min_=-10, max_=10, num=15) -> list[int]:
    random_list = []
    while len(random_list) != num:
        val = random.randint(min_, max_)
        if val not in random_list:
            random_list.append(val)

    return random_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
