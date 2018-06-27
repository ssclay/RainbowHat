from unittest.mock import patch, MagicMock

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

import sys

class TestLedStrip(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        sys.modules['rainbowhat'] = MagicMock()
        from ..LedStrip_block import LedStrip
        global LedStrip

    def test_led(self):
        with patch(LedStrip.__module__ +'.rh.rainbow') as mock_led:
            blk = LedStrip()
            self.configure_block(blk, {})
            blk.start()
            blk.process_signals([Signal({})])
            blk.stop()
            self.assertDictEqual(
                self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
                {})
