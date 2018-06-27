from nio.block.base import Block
from nio.properties import VersionProperty, Property

import rainbowhat as rh

class AlphaDisplay(Block):

    version = VersionProperty('0.1.0')
    words = Property(title="Words to Screen", default='AHOY')
    floats = Property(title="Floats to Screen", default='1337')

    def process_signals(self, signals):
        
	    if self.words():
	        for signal in signals:
	            rh.display.clear()
	            rh.display.print_str(self.words(signal))
	            rh.display.show()
	        self.notify_signals(signals)

	    if self.floats():
	        for signal in signals:
	            rh.display.clear()
	            rh.display.print_float(self.floats(signal))
	            rh.display.show()
	        self.notify_signals(signals)
