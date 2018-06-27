from nio.block.base import Block
from nio.properties import VersionProperty, Property

import rainbowhat as rh


class TemperatureSensor(Block):

    def process_signals(self, signals):

        for signal in signals:
            temp = rh.weather.temperature(signal)
            pressure = rh.weather.pressure(signal)
        self.notify_signals(signals)

