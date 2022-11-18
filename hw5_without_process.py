from time import time
from multiprocessing import Process


def factorize(*number):
    b_lst = []
    for num in number:
        i = 1
        s_lst = []
        while i <= num:
            if num % i == 0:
                s_lst.append(i)
                i += 1
            else:
                i += 1
                continue
        b_lst.append(s_lst)
    return tuple(b_lst)


start = time()
a, b, c, d = factorize(128, 255, 99999, 10651060)
end = time()

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


if __name__ == '__main__':
    with open('Результати до використання процесів.txt', 'a') as file:
        file.write(f'Час виконання: {round(end-start, 3)}\n')