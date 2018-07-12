from unittest.mock import patch, MagicMock, ANY

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

import sys


class TestAndroidThingsRGB(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        sys.modules['rainbowhat'] = MagicMock()
        from ..android_things_rgb_block import AndroidThingsRGB
        global AndroidThingsRGB

    def test_AndroidThingsRGBmash(self):
        with patch(AndroidThingsRGB.__module__ + '.rh.lights.red.on') as mock_light:
            blk = AndroidThingsRGB()
            self.configure_block(blk, {'red': True})
            blk.start()
            blk.process_signals([Signal({})])
            self.assertEqual(mock_light.call_count, 1)
            blk.stop()