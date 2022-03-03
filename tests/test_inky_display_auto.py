from PIL import Image
import unittest
import os
import unittest.mock as mock
from unittest.mock import MagicMock
import inky

tk = type('',(object,),{"foo": 1})()
tk.Tk = MagicMock()
tk.PhotoImage = MagicMock()
tk.Canvas = MagicMock()

image_path = os.path.dirname(os.path.realpath(__file__)) + '/../examples/PIA03519_small.jpg'

class Test(unittest.TestCase):
    def test_mock_inky(self):
        with mock.patch.dict('sys.modules', tkinter=tk):
            epd = inky.mock.InkyMockWHAT('red')
            image = Image.open(image_path)
            
            pal_img = Image.new("P", (1, 1))
            pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 253)

            image = image.resize((epd.width, epd.height))
            image = image.convert("RGB").quantize(palette=pal_img)
            epd.set_image(image)
            epd.show()
            
            epd.disp_img_copy.save('test.png')
