import time

if __name__ == '__main__':
    t1 = time.time()
    for i in range(10):
        pass
    t2 = time.time()
    print(1000*(t2 - t1))