from nio.block.base import Block
from nio.properties import VersionProperty, Property

import rainbowhat as rh


class AlphaDisplay(Block):

    version = VersionProperty('0.1.0')
    words = Property(title="Words to Screen", default=None, allow_none=True)
    # floats = Property(title="Floats to Screen", default=None, allow_none=True)

    def process_signals(self, signals):

        for signal in signals:
            rh.display.clear()
            rh.display.print_str(str(self.words(signal)))
        rh.display.show()
        self.notify_signals(signals)
