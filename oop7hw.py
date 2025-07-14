print('1:')


def sum_numbers(*args):
    return print(sum(args))


sum_numbers(1, 2, 3, 4)

print('2:')


def print_user_info(**kwargs):
    return print(kwargs)


print_user_info(name="Dana", age=30, city="Tel Aviv")

print('3:')


def combine_values(*args, **kwargs):
    print(f'Sum:{sum(args)}')
    for key, value in kwargs.items():
        print(f"{key}: {value}")


combine_values(2, 4, 6, name="Tom", job="Dev")

print('4:')


def greet_user(**kwargs):
    if "name" in kwargs:
        print(f"Hello {kwargs['name']}!")
    else:
        print("Hello guest!")


greet_user(name="Lior")
greet_user()
