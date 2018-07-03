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
        rh.touch.A.press(self.foo)
        rh.touch.B.press(self.foo)
        rh.touch.C.press(self.foo)
        rh.touch.A.release(self.bar)
        rh.touch.B.release(self.bar)
        rh.touch.C.release(self.bar)

    def foo(self, channel):
        ch = self.CHANNEL_MAP[channel]
        self.notify_signals(Signal({'channel': ch, 'value': True}))
        rh.lights.rgb(255,255,255)

    def bar(self, channel):
        ch = self.CHANNEL_MAP[channel]
        self.notify_signals(Signal({'channel': ch, 'value': False}))
        rh.lights.rgb(0,0,0)

