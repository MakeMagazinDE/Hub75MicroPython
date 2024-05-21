import time
import random
from interstate75 import Interstate75, DISPLAY_INTERSTATE75_64X64

matrix = Interstate75(display = DISPLAY_INTERSTATE75_64X64)
buffer = matrix.display

width = matrix.width
height = matrix.height

black = buffer.create_pen(0, 0, 0)
green = buffer.create_pen(0, 150, 0)

buffer.set_pen(black)
buffer.clear()
buffer.set_pen(green)

#In dieser abgewandelten Variante von text_umbruch.py
#könnt ihr mit die A-Taste am Interstate 75 drücken,
#um die Farbe des Textes zufällig zu ändern.
#0 steht für den Taster A.
SWITCH_A = 0

while True:


    if matrix.switch_pressed(SWITCH_A):
        buffer.set_pen(buffer.create_pen(random.randint(0, 255),
                                         random.randint(0, 255),
                                         random.randint(0, 255)))

    buffer.text("So lässt sich Text ganz leicht auf einer LED-Matrix darstellen.", 4, 11, wordwrap = 64, scale = 1)

    matrix.update(buffer)
    time.sleep(0.1)
