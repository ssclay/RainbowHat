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

        if rh.touch.A.press():
            button_a = True
            rh.lights.rgb(255, 0, 0)

        # @rh.touch.A.release()
        # def release_a(channel):
        #     button_a = False
        #     rh.lights.rgb(0, 0, 0)

        if rh.touch.B.press():
            button_b = True
            rh.lights.rgb(0, 255, 0)

        # @rh.touch.B.release()
        # def release_b(channel):
        #     button_b = False
        #     rh.lights.rgb(0, 0, 0)

        if rh.touch.C.press():
            button_c = True
            rh.lights.rgb(0, 0, 255)

        # @rh.touch.C.release()
        # def release_c(channel):
        #     button_c = False
        #     rh.lights.rgb(0, 0, 0)

        presses = {'button_a': touch_a,
                   'button_b': touch_b,
                   'button_c': touch_c}

        self.notify_signals(Signal(presses))