from nio.block.base import Block
from nio.properties import VersionProperty, Property

from time import sleep
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
            for r in range(0, 8):
                red = getattr(self, 'pixelrgb{}'.format(r))(signal)[0]
                green = getattr(self, 'pixelrgb{}'.format(r))(signal)[1]
                blue  = getattr(self, 'pixelrgb{}'.format(r))(signal)[2]
                print(r)
                print(red, green, blue)
                rh.rainbow.set_pixel(r,
                        red, 
                        green,
                        blue)
                rh.rainbow.show()

        self.notify_signals(signals)
