from nio.block.base import Block
from nio.properties import VersionProperty, Property
from nio.signal.base import Signal

import rainbowhat as rh


class TemperatureSensor(Block):

    version = VersionProperty('0.1.0')

    def process_signals(self, signals):

        for signal in signals:
            temp = rh.weather.temperature()
            pressure = rh.weather.pressure()
        self.notify_signals([Signal({'temp': temp, 'pressure': pressure})])

