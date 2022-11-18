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


if __name__ == '__main__':

    start = time()
    a = Process(target=factorize, args=(128,))
    b = Process(target=factorize, args=(255,))
    c = Process(target=factorize, args=(99999,))
    d = Process(target=factorize, args=(10651060,))
    a.start()
    b.start()
    c.start()
    d.start()
    end = time()
    print(f'Time: {round(end-start, 3)}')