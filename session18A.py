#interview question

# when u need to pass variable input to function -> when u dont know how many number pass.( 1 no. to n numbers)

def add(*args):
    print(args)
    data = list(args)
    print(data)
    print(type(args))
    print(type(data))


add(10, 20, 30, 40, 50, "hi", "john", "hello")

print("-----------------------")

def numbers(**kwargs): #keyword argument
    print(kwargs)
    print(type(kwargs))

numbers(a = 10, b = 20, c = 30)

def fun(*args, **kwargs):
    print(args)
    print(kwargs)

add(10, 20, 30, 40, 50, "hi", "john", "hello", a = 10, b = 20, c = 30)
