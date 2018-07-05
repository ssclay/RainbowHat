from nio.block.base import Block
from nio.properties import VersionProperty, FloatProperty
from nio.signal.base import Signal

import rainbowhat as rh


class Button(Block):

    version = VersionProperty('0.1.0')

    CHANNEL_MAP = {
        0: 'A',
        1: 'B',
        2: 'C',
    }

    def configure(self, context):
        super().configure(context)
        rh.touch.A.press(self.pressed)
        rh.touch.B.press(self.pressed)
        rh.touch.C.press(self.pressed)
        rh.touch.A.release(self.released)
        rh.touch.B.release(self.released)
        rh.touch.C.release(self.released)

    def pressed(self, channel):
        ch = self.CHANNEL_MAP[channel]
        self.notify_signals(Signal({'channel': ch, 'value': True}))
        if channel == 0:
            rh.lights.red.on()
        if channel == 1:
            rh.lights.green.on()
        if channel == 2:
            rh.lights.blue.on()

    def released(self, channel):
        ch = self.CHANNEL_MAP[channel]
        self.notify_signals(Signal({'channel': ch, 'value': False}))
        rh.lights.rgb(0,0,0)

