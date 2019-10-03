import random

class Sensor(object):

    _OFFSET = 16

    def sample_pressure(self):
        pressure_telemetry_value = self.simulate_pressure()
        return Sensor._OFFSET + pressure_telemetry_value

    @staticmethod
    def simulate_pressure():
        pressure_telemetry_value = 6 * random.random() * random.random()
        return pressure_telemetry_value

