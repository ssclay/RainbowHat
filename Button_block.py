from nio.block.base import Block
from nio.properties import VersionProperty, FloatProperty

import rainbowhat as rh


class Button(Block):

    version = VersionProperty('0.1.0')

    def process_signals(self, signals):

        @rh.touch.A.press()
        def touch_a(channel):
            touch_a = True
            rh.lights.rgb(255, 0, 0)

        @rh.touch.A.release()
        def release_a(channel):
            touch_a = True
            rh.lights.rgb(0, 0, 0)

        @rh.touch.B.press()
        def touch_b(channel):
            touch_b = True
            rh.lights.rgb(255, 0, 0)

        @rh.touch.B.release()
        def release_b(channel):
            touch_b = True
            rh.lights.rgb(0, 255, 0)

        @rh.touch.C.press()
        def touch_c(channel):
            touch_c = True
            rh.lights.rgb(0, 0, 255)

        @rh.touch.D.release()
        def release_d(channel):
            touch_d = True
            rh.lights.rgb(0, 0, 0)
        self.notify_signals(signals)