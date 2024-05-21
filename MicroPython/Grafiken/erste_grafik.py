from interstate75 import Interstate75, DISPLAY_INTERSTATE75_64X64

matrix = Interstate75(display=DISPLAY_INTERSTATE75_64X64)
buffer = matrix.display
width = matrix.width
height = matrix.height

black = buffer.create_pen(0, 0, 0)
white = buffer.create_pen(255, 255, 255)

buffer.set_pen(black)
buffer.clear()

buffer.set_pen(white)
buffer.circle(int(width/2), int(height/2), 10)
matrix.update(buffer)