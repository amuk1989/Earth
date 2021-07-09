import serial


class Connect_controller:
    def __init__(self):
        self.ser = serial.Serial()

    def connect(self, port="COM1", speed=115200) -> bool:
        try:
            self.ser.port = port
            self.ser.baudrate = speed
            self.ser.open()
            return self.ser.isOpen()
        except BaseException:
            print('error')
            return False

    def send(self, time: int, mode: int):
        print(f'Задано {time} микросекунд, режим {mode}')