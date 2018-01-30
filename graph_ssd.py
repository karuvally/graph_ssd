#!/usr/bin/env python
# graph_ssd, alpha release
# Released under GNU General Public License

# TODO
# make the y_value from the base of OLED
# make x_position access the global variable

# import all the serious stuff
from lib_oled96 import ssd1306
from smbus import SMBus

# creates the OLED object
i2cbus = SMBus(1)
oled = ssd1306(i2cbus)


# the class which handles line graphs
class lineGraph:
    # all the instance variables
    def __init__(self):
        self.x_value = 0
        self.old_x_value = None
        self.old_y_value = None
    
    # draw each point in graph
    def draw(self, y_value):
        # convert y_value according to resolution of display
        y_value = float(y_value)
        y_value = (y_value/100)*64
        y_value = int(64 - y_value)

        oled.canvas.point((self.x_value, y_value), fill=1)
        oled.display()

        self.old_x_value = self.x_value
        self.old_y_value = y_value
        self.x_value += 1

        if self.old_x_value:
            pass
            #oled.canvas.line((self.old_x_value, self.old_y_value, self.x_value, y_value), fill=1, width=1)
