from unittest.mock import patch, MagicMock, ANY

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

import sys


class TestButton(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        sys.modules['rainbowhat'] = MagicMock()
        from ..Button_block import Button
        global Button

    def test_buttonmash(self):
        with patch(Button.__module__ + '.rh.touch') as mock_touch:
            with patch(Button.__module__ + '.rh.light') as mock_light:
                blk = Button()
                self.configure_block(blk, {'incoming': 'pewpew'})
                blk.start()
                blk.process_signals([Signal({})])
                mock_touch.A.press()
                blk.stop()
                # self.assertDictEqual(
                    # self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
                    # {'channel': ANY, 'value': ANY})