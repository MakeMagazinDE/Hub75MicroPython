import random
from interstate75 import Interstate75, DISPLAY_INTERSTATE75_64X64

#Displayobjekt und Buffer
matrix = Interstate75(display=DISPLAY_INTERSTATE75_64X64)
buffer = matrix.display

#Displaygröße
width = matrix.width
height = matrix.height

black = buffer.create_pen(0, 0, 0)

buffer.set_pen(black)
buffer.clear()

buffer.set_pen(buffer.create_pen(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
buffer.line(5,5,59,5)
buffer.set_pen(buffer.create_pen(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
buffer.rectangle(5,12,24,24)
buffer.set_pen(buffer.create_pen(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
buffer.circle(46,24,12)
buffer.set_pen(buffer.create_pen(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
buffer.polygon([(5,48),(10,40),(59,40),(15,60)])
buffer.set_pen(buffer.create_pen(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
buffer.pixel(50,50)
buffer.set_pen(buffer.create_pen(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
buffer.pixel(54,54)
buffer.set_pen(buffer.create_pen(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
buffer.pixel(47,56)

matrix.update(buffer)
