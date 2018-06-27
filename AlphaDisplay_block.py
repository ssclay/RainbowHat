from nio.block.base import Block
from nio.properties import VersionProperty, Property

import rainbowhat as rh

class AlphaDisplay(Block):

    version = VersionProperty('0.1.0')
    words = Property(title="Words to Screen", default='AHOY')

    def process_signals(self, signals):
        for signal in signals:
            rh.display.clear()
            rh.display.print_str(self.words())
            rh.display.show()
        self.notify_signals(signals)
