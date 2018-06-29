from nio.block.base import Block
from nio.properties import VersionProperty, Property
from nio.signal.base import Signal
from nio.block.mixins.enrich.enrich_signals import EnrichSignals

import rainbowhat as rh


class TemperatureSensor(EnrichSignals, Block):

    version = VersionProperty('0.1.0')

    def process_signals(self, signals):
        new_signals = []
        for signal in signals:
            temp = rh.weather.temperature()
            pressure = rh.weather.pressure()
        self.notify_output_signals([{'temp_c':temp, 'pressure_Pa':pressure}], signals)

