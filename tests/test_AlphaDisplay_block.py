from unittest.mock import patch, MagicMock

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

import sys

class TestAlphaDisplay(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        sys.modules['rainbowhat'] = MagicMock()
        from ..AlphaDisplay_block import AlphaDisplay
        global AlphaDisplay

    def test_string(self):
        """Signals pass through block unmodified."""
        with patch(AlphaDisplay.__module__ +'.rh.display') as mock_display:
            blk = AlphaDisplay()
            self.configure_block(blk, {'words':'HIII'})
            blk.start()
            blk.process_signals([Signal({})])
            blk.stop()
            self.assert_num_signals_notified(1)
            mock_display.print_str.assert_called_with('HIII')
            mock_display.show.assert_called()
            self.assertDictEqual(
                self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
                {})
