from nio import GeneratorBlock
from nio.block import output
from nio.properties import VersionProperty, FloatProperty
from nio.signal.base import Signal

import rainbowhat as rh

@output('press', label='Press')
@output('release', label='Release')
class Button(GeneratorBlock):

    version = VersionProperty('0.1.0')

    # def configure(self, context):
    #     super().configure(context)
    #     self._button[0] = False
    #     self._button[1] = False
    #     self._button[2] = False

    def _press(button):
        press_output = button
        self.notify_signals(press_ouput,'press')

    def _release(button):
        release_output = button
        self.notify_signals(release_output, 'release')

    
    rh.touch.A.press(_press)
    rh.touch.B.press(_press)
    rh.touch.C.press(_press)
    rh.touch.A.release(_release)
    rh.touch.B.release(_release)
    rh.touch.C.release(_release)
    
    def process_signals(self, signals):
        pass

        # self.notify_signals(Signal(presses))