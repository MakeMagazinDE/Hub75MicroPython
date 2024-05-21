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

#Für Groß- und Kleinschreibung
#buffer.set_font("bitmap8")

buffer.text("So lässt sich Text ganz leicht auf einer LED-Matrix darstellen.", 4, 11, wordwrap = 64, scale = 1)

matrix.update(buffer)