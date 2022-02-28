import unittest
import os
import pytest

from omni_epd import displayfactory
from PIL import Image


class TestInkyDisplay(unittest.TestCase):

    # @pytest.mark.xfail
    def test_auto_inky(self):
        """
        test auto loading real inky display
        """
        epd = displayfactory.load_display_driver('inky.auto')
        image = Image.open(os.path.dirname(os.path.realpath(__file__)) + '/../examples/PIA03519_small.jpg')
        image = image.resize((epd.width, epd.height))
        epd.display(image)

    def test_epd2in7b_V2(self):
        """
        test auto loading real waveshare 
        """
        epd = displayfactory.load_display_driver('waveshare_epd.epd2in7b_V2')
        image = Image.open(os.path.dirname(os.path.realpath(__file__)) + '/../examples/PIA03519_small.jpg')
        image = image.resize((epd.width, epd.height))
        epd.display(image)