import os
import time
import sys
import psutil


def show_function_memory(f):
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        before = proc.memory_info().rss / 1000000
        f(*args, **kwargs)
        after = proc.memory_info().rss / 1000000
        print('Использовано {} памяти'.format(after - before))
    return wrapper


def show_function_time(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        stop = time.time()
        print('Затраченное время {}'.format(stop - start))
    return wrapper


@show_function_time
@show_function_memory
def generate_list(num):
    list_temp = []
    for i in range(num):
        list_temp.append(num)

    return list_temp


@show_function_time
@show_function_memory
def generate_generator(num):
    for i in range(num):
        yield list


print('Генерация списка')
print(generate_list(10**5))
print('Генерация генератора')
print(generate_generator(10**5))
