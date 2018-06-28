from nio.block.base import Block
from nio.properties import VersionProperty, Property

import rainbowhat as rh


class TemperatureSensor(Block):

    version = VersionProperty('0.1.0')

    def process_signals(self, signals):

        for signal in signals:
            temp = rh.weather.temperature(signal)
            pressure = rh.weather.pressure(signal)
        self.notify_signals([{'temp': temp, 'pressure': pressure}])

