from nio.block.base import Block
from nio.properties import VersionProperty, Property

import rainbowhat as rh

class LedStrip(Block):

    version = VersionProperty('0.1.0')
    pixelrgb0 = Property(title='pixel 0 r g b', default=(0,0,0))
    pixelrgb1 = Property(title='pixel 1 r g b', default=(0,0,0))
    pixelrgb2 = Property(title='pixel 2 r g b', default=(0,0,0))
    pixelrgb3 = Property(title='pixel 3 r g b', default=(0,0,0))
    pixelrgb4 = Property(title='pixel 4 r g b', default=(0,0,0))
    pixelrgb5 = Property(title='pixel 5 r g b', default=(0,0,0))
    pixelrgb6 = Property(title='pixel 6 r g b', default=(0,0,0))
    pixelrgb7 = Property(title='pixel 7 r g b', default=(0,0,0))

    def process_signals(self, signals):

        for signal in signals:
            rh.rainbow.set_pixel(0, 
                        self.pixelrgb0(signal)[0], 
                        self.pixelrgb0(signal)[1], 
                        self.pixelrgb0(signal)[2])
            rh.rainbow.show()

        self.notify_signals(signals)
