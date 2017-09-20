import threading
from time import sleep
import random

def do_one():
        print 'do one: ' + str(random.randint(1, 10))
        sleep(1)
        print 'on over'

def do_two():
        print 'do two: ' + str(random.randint(10, 20))
        sleep(2)
        print 'two over'

def test():
    t1 = threading.Thread(target=do_two)
    t2 = threading.Thread(target=do_one)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    test()

