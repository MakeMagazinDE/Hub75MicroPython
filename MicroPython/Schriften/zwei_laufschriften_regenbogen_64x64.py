import time
import random
from interstate75 import Interstate75, DISPLAY_INTERSTATE75_64X64

#Displayobjekt und Buffer
matrix = Interstate75(display=DISPLAY_INTERSTATE75_64X64)
buffer = matrix.display

#Displaygröße
width = matrix.width
height = matrix.height

#Einstellungen Laufschrift 1
old_ticks = time.ticks_ms()
waiting_time = 10 #kleiner ist schneller
text_scale = 5
pos_x = width+3
pos_y = 0
text_string = "Diese kleine Laufschrift wechselt die Farbe mit Zufallswerten."
text_width = buffer.measure_text(text_string, scale=text_scale)

#Einstellungen Laufschrift 2
old_ticks2 = time.ticks_ms()
waiting_time2 = 30 #kleiner ist schneller
text_scale2 = 2
pos_x2 = width+3
pos_y2 = 32
text_string2 = "Hier unten scrollt ein kleinerer Text in etwas langsamerer Geschwindigkeit."
text_width2 = buffer.measure_text(text_string2, scale=text_scale2)

#Farben
black = buffer.create_pen(0, 0, 0)

#Zufällige Farbwerte für den Regenbogen-Farbwechsel
value_red = random.randint(0,255)
value_green = random.randint(0,255)
value_blue = random.randint(0,255)
aim_red = random.randint(0,255)
aim_green = random.randint(0,255)
aim_blue = random.randint(0,255)

#Farbwechsel-Funktion
def rainbow_colors():
    
    global value_red
    global aim_red
    global value_green
    global aim_green
    global value_blue
    global aim_blue
    
    #Wenn der aktuelle Farbwert (0-255) nicht dem zufälligen Zielwert(0-255)
    #entspricht, addiert oder subtrahiert das Programm 1, und zwar abhängig
    #davon, ob der Zielwert höher oder niedriger als der aktuelle Farbwert ist.
    #Diese Berechnung erfolgt für alle drei Farbkanäle. Je nach Mix kann es
    #sein, dass die Schrift mal heller oder dunkler erscheint.
    #Ist das Ziel erreicht, erzeugt random.randint(0,255) einen neuen
    #zufälligen Zielwert.
    
    if value_red != aim_red:
        if value_red <= aim_red:
            value_red += 1
        else:
            value_red -= 1
    else:
        aim_red = random.randint(0,255)
        
    if value_green != aim_green:
        if value_green <= aim_green:
            value_green += 1
        else:
            value_green -= 1
    else:
        aim_green = random.randint(0,255)
        
    if value_blue != aim_blue:
        if value_blue <= aim_blue:
            value_blue += 1
        else:
            value_blue -= 1
    else:
        aim_blue = random.randint(0,255)
    

#Ich habe die Laufschriften in einzelne Funktionen ausgelagert, damit
#die Dauerschleife while True: etwas ordentlicher aussieht.

#Laufschrift 1
def scrolling_text():

    global old_ticks #müssen als global deklariert werden, weil wir sie ändern
    global waiting_time
    global pos_x

    if ((time.ticks_ms() - old_ticks) >= waiting_time):
        old_ticks = time.ticks_ms()
        
        buffer.set_clip(0, 0, 64, 32)
        buffer.set_pen(black)
        buffer.clear()
    
        if pos_x >= -text_width:
            pos_x -= 1
        else:
            pos_x = width+3
            
        rainbow_colors()
            
        buffer.set_pen(buffer.create_pen(value_red, value_green, value_blue))
        buffer.text(text_string, pos_x, pos_y, scale=text_scale)
        buffer.remove_clip()
        
        
#Laufschrift 2
def scrolling_text2():
    
    global old_ticks2
    global waiting_time2
    global pos_x2

    if ((time.ticks_ms() - old_ticks2) >= waiting_time2):
        old_ticks2 = time.ticks_ms()
        
        buffer.set_clip(0, 32, 64, 32)
        buffer.set_pen(black)
        buffer.clear()

        if pos_x2 >= -text_width2:
            pos_x2 -= 1
        else:
            pos_x2 = width+3

            
        buffer.set_pen(buffer.create_pen(230, 0, 0))    
        buffer.text(text_string2, int(pos_x2), pos_y2, scale=text_scale2)
        buffer.remove_clip()

while True:
    
    scrolling_text()
    scrolling_text2()
    
    matrix.update(buffer)
        
        
    
