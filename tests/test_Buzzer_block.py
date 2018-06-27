from unittest.mock import patch, MagicMock, ANY

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

import sys


class TestBuzzer(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        sys.modules['rainbowhat'] = MagicMock()
        from ..Buzzer_block import Buzzer
        global Buzzer

    def test_buzzer(self):
        with patch(Buzzer.__module__ + '.rh.buzzer') as mock_buzz:
            blk = Buzzer()
            self.configure_block(blk, {})
            blk.start()
            blk.process_signals([Signal({'incoming': 'pewpew'})])
            blk.stop()
            self.assertDictEqual(
                self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
                {'incoming': 'pewpew'})