def hello_world():
    print("Hello world!")


hello_world()


def sum(num1, num2):
    if type(num1) is not int or type(num2) is not int:
        return
    return num1 + num2


total = sum(7, 2)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sara")


def multiple_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


multiple_named_items(first="Dave", last="Gray")
