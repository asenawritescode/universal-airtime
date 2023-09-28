import time as t


def timer(f):
    def wrapper():
        print("Timer start !")
        st = t.time()
        f()
        et = t.time()
        print("Timer stop  !")
        print(f"The elapsed time is {et - st}")

    return wrapper


@timer
def hello():
    sum_x = 0
    for i in range(1000000):
        sum_x += i


hello()
