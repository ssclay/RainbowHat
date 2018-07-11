from unittest.mock import patch, MagicMock, ANY

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

import sys


class TestAndroidThingsButton(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        sys.modules['rainbowhat'] = MagicMock()
        from ..android_things_button_block import AndroidThingsButton
        global AndroidThingsButton

    def test_AndroidThingsButtonmash(self):
        with patch(AndroidThingsButton.__module__ + '.rh.touch') as mock_touch:
            with patch(AndroidThingsButton.__module__ + '.rh.light') as mock_light:
                blk = AndroidThingsButton()
                self.configure_block(blk, {'incoming': 'pewpew'})
                blk.start()
                blk.process_signals([Signal({})])
                mock_touch.A.press()
                blk.stop()
                # self.assertDictEqual(
                    # self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
                    # {'channel': ANY, 'value': ANY})
