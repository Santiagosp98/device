from machine import ADC

MAX_LOOPS = 100
VOLTAGE = 5.0


class MQ9:
    def __init__(self, pin):
        self.pin = ADC(pin)
        self.value = 0
        self.voltage = 0
        self.r0 = 0
        self.rs_air = 0
        self.rs_gas = 0

        self.__calibrate()

    def __calibrate(self):
        for i in range(1, MAX_LOOPS):
            self.value += self.pin.read()

        self.value /= MAX_LOOPS

        self.voltage = (self.value / 1024) * VOLTAGE

        self.rs_air = (VOLTAGE - self.voltage) / self.voltage

        self.r0 = self.rs_air / 9.9

    def gas(self):
        self.value = self.pin.read()
        self.voltage = (self.value / 1024) * VOLTAGE
        self.rs_gas = (VOLTAGE - self.voltage) / self.voltage

        return self.rs_gas / self.r0
