import socket, threading


class Tello:
    def __init__(self):
        self.local_ip = ''
        self.local_port = 8889
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))
        self.tello_ip = '192.168.10.1'
        self.tello_port = 8889
        self.tello_address = (self.tello_ip, self.tello_port)
        self.MAX_TIME_OUT = 15.0
        self.response = None
        self.socket.sendto(b'command', self.tello_address)
        self._receive_thread = threading.Thread(target=self.receive_thread)
        self._receive_thread.daemon = True
        self._receive_thread.start()

    def flip(self, direction):
        """
        :param direction: Direction to flip, 'l', 'r', 'f', 'b'.
        :return: Response from Tello, 'OK' or 'FALSE'.
        """
        return self.send_command('flip %s' % direction)

    def land(self):
        """
        :return: Response from Tello, 'OK' or 'FALSE'.
        """
        return self.send_command('land')

    def move(self, direction, distance):
        distance = int(round(float(distance) * 100))
        return self.send_command('%s %s' % (direction, distance))

    def move_up(self, distance):
        return self.move('up', distance)

    def move_backward(self, distance):
        return self.move('back', distance)

    def move_down(self, distance):
        return self.move('down', distance)

    def move_forward(self, distance):
        return self.move('forward', distance)

    def move_left(self, distance):
        return self.move('left', distance)

    def move_right(self, distance):
        return self.move('right', distance)

    def set_speed(self, speed):
        speed = int(round(float(speed) * 27.7778))
        return self.send_command('speed %s' % speed)

    def get_battery(self):
        battery = self.send_command('battery?')
        try:
            battery = int(battery)
        except Exception as e:
            print(e)
        return battery

    def get_speed(self):
        speed = self.send_command('speed?')
        try:
            speed = float(speed)
        except Exception as e:
            print(e)
        return speed

    def get_height(self):
        height = self.send_command('height?')
        try:
            height = float(height)
        except Exception as e:
            print(e)
        return height

    def receive_thread(self):
        while True:
            try:
                self.response, ip = self.socket.recvfrom(4096)
                print(self.response)
            except socket.error as exc:
                print("Caught exception socket.error : %s" % exc)

    def send_command(self, command):
        print("-> sent cmd: {}".format(command))
        last = self.response
        self.socket.sendto(command.encode(), self.tello_address)
        while self.response == last:
            pass
        return self.response


if __name__ == '__main__':
    pass
