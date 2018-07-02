from nio.block.base import Block
from nio.properties import VersionProperty, FloatProperty
from nio.signal.base import Signal

import rainbowhat as rh


class Button(Block):

    version = VersionProperty('0.1.0')

    def process_signals(self, signals):

        button_a = False
        button_b = False
        button_c = False

        @rh.touch.A.press()
        def touch_a(channel):
            button_a = True
            rh.lights.rgb(255, 0, 0)
            return button_a

        @rh.touch.A.release()
        def release_a(channel):
            button_a = False
            rh.lights.rgb(0, 0, 0)
            return button_a

        @rh.touch.B.press()
        def touch_b(channel):
            button_b = True
            rh.lights.rgb(0, 255, 0)
            return button_b

        @rh.touch.B.release()
        def release_b(channel):
            button_b = False
            rh.lights.rgb(0, 0, 0)
            return button_b

        @rh.touch.C.press()
        def touch_c(channel):
            button_c = True
            rh.lights.rgb(0, 0, 255)
            return button_c

        @rh.touch.C.release()
        def release_c(channel):
            button_c = False
            rh.lights.rgb(0, 0, 0)
            return button_c

        presses = {'button_a': button_a,
                   'button_b': button_b,
                   'button_c': button_c}

        self.notify_signals(Signal(presses))