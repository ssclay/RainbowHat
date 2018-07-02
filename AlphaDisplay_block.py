from time import sleep
from nio.block.base import Block
from nio.properties import VersionProperty, Property

import rainbowhat as rh


class AlphaDisplay(Block):

    version = VersionProperty('0.1.0')
    words = Property(title="Words to Screen", default=None, allow_none=True)

    def configure(self, context):
        super().configure(context)
        rh.display.clear()
        rh.display.show()

    def process_signals(self, signals):

        for signal in signals:
            r0 = 0
            r = 4
            while r <= len(self.words(signal)):
                rh.display.print_str(str(self.words(signal)[r0:r]))
                rh.display.show()
                sleep(0.5)
                r0 = r
                r += 4
        self.notify_signals(signals)

    def stop(self):
        rh.display.clear()
        rh.display.show()
        super().stop()
