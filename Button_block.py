from nio.block.base import Block
from nio.properties import VersionProperty, FloatProperty
from nio.signal.base import Signal

import rainbowhat as rh


class Button(Block):

    version = VersionProperty('0.1.0')

    def configure(self, context):
        super().configure(context)
        self.button_a = False
        self.button_b = False
        self.button_c = False

    @rh.touch.A.press()
    def touch_a(self, channel):
        self.button_a = True
        rh.lights.rgb(255, 0, 0)


    @rh.touch.A.release()
    def release_a(self, channel):
        self.button_a = False
        rh.lights.rgb(0, 0, 0)

    @rh.touch.B.press()
    def touch_b(self, channel):
        self.button_b = True
        rh.lights.rgb(0, 255, 0)

    @rh.touch.B.release()
    def release_b(self, channel):
        self.button_b = False
        rh.lights.rgb(0, 0, 0)

    @rh.touch.C.press()
    def touch_c(self, channel):
        self.button_c = True
        rh.lights.rgb(0, 0, 255)

    @rh.touch.C.release()
    def release_c(self, channel):
        self.button_c = False
        rh.lights.rgb(0, 0, 0)
 
    
    def process_signals(self, signals):
        presses = {'button_a': self.button_a,
                   'button_b': self.button_b,
                   'button_c': self.button_c}

        self.notify_signals(Signal(presses))