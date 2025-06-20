# *args

def add_all(*args):
    total = sum(args)
    print("total:", total)

add_all(2, 3, 5, 4)
add_all(7, 8,3,3,2,5,9)

def get_user(**kwagrs):
    for i, values in kwagrs.items():
        print(i,'=', values)

get_user(name="Abdu", age=21, city="Addis Ababa")

def demo(a, *args, **kwargs):
    print("a: ", a)
    print("args: ", args)
    print("kwargs: ", kwargs)


demo( 2, 5, 3, x=10, y=20)