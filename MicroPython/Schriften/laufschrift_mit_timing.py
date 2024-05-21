import time

from interstate75 import Interstate75, DISPLAY_INTERSTATE75_64X64

matrix = Interstate75(display=DISPLAY_INTERSTATE75_64X64)
buffer = matrix.display
width = matrix.width
height = matrix.height

text_scale = 2
pos_x = width+3
pos_y = 0
text_string = "Dieser Text bewegt sich von rechts nach links."
text_width = buffer.measure_text(text_string, scale = text_scale)

black = buffer.create_pen(0, 0, 0)
red = buffer.create_pen(255, 0, 0)

old_ticks = time.ticks_ms()
waiting_time = 100

while True:
  
  if ((time.ticks_ms() - old_ticks) >= waiting_time):
      old_ticks = time.ticks_ms()

      buffer.set_pen(black)
      buffer.clear()
      buffer.set_pen(red)
      buffer.text(text_string, pos_x, pos_y, scale = text_scale)
      
      if pos_x > -text_width:
        pos_x -= 1
      else:
        pos_x = width+3
        
      matrix.update(buffer)
