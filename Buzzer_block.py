from nio.block.base import Block
from nio.properties import VersionProperty, Property

import rainbowhat as rh


class Buzzer(Block):

    def process_signals(self, signals):

        for signal in signals:
            pass
        self.notify_signals(signals)