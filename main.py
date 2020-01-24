from Tello import *
import time


def main():
    d = Tello()
    s = Server()
    while 1:
        print(s.parse())
        time.sleep(0.1)


if __name__ == '__main__':
    main()
