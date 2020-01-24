import Tello, time


def main():
    d = Tello.Tello()
    while 1:
        print(d.get_battery())
        time.sleep(1)

if __name__ == '__main__':
    main()
