import random
import time
from interstate75 import Interstate75, DISPLAY_INTERSTATE75_64X64

#Displayobjekt und Buffer
matrix = Interstate75(display=DISPLAY_INTERSTATE75_64X64)
buffer = matrix.display

#Displaygröße
width = matrix.width
height = matrix.height

black = buffer.create_pen(0, 0, 0)
color1 = buffer.create_pen(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
color2 = buffer.create_pen(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

clip_width = 32
clip_height = 20
clip_pos_x = 16
clip_pos_y = 22

#Einstellungen Laufschrift 1
old_ticks = time.ticks_ms()
scroll_speed = 30 #kleiner ist schneller
text_scale = 3
pos_x = clip_width+3
pos_y = clip_height
text_string = "Man kann Texte auch in separaten Ausschnitten laufen lassen."
text_width = buffer.measure_text(text_string, scale=text_scale)


#Laufschrift 1

def scrolling_text():

    global old_ticks #müssen als global deklariert werden, weil wir sie ändern
    global scroll_speed
    global pos_x

    if ((time.ticks_ms() - old_ticks) >= scroll_speed):
        old_ticks = time.ticks_ms()
        
        buffer.set_clip(clip_pos_x, clip_pos_y, clip_width, clip_height)
        buffer.set_pen(black)
        buffer.clear()
    
        if pos_x >= -text_width:
            pos_x -= 1
        else:
            pos_x = clip_width+clip_pos_x+3
            
        buffer.set_pen(color1)
        buffer.text(text_string, pos_x, pos_y, scale=text_scale)
        buffer.remove_clip()
        


while True:
    

    scrolling_text()
    buffer.set_pen(color2)
    buffer.line(14, 20, 50, 20)
    buffer.line(14, 40, 50, 40)
    buffer.line(13, 20, 13, 41)
    buffer.line(50, 20, 50, 41)


    matrix.update(buffer)