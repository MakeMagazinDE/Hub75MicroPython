<b>Timing und Clipping</b>
<br><br>
Möchte man mehr als eine Laufschrift darstellen, kann man die <b>if</b>-Bedingung aus <i>laufschrift_mit_timing.py</i> in der Dauerschleife <b>while True:</b> samt ihrer Variablen vervielfachen. Das Beispielprogramm <i>zwei_laufschriften_regenbogen.py</i> zeigt, wie es geht und löst zudem noch folgendes Problem: ein Flimmern, das entsteht, wenn beide Laufschriften sich mit unterschiedlicher Geschwindigkeit bewegen. Dieses tritt auf, weil die beiden Schriften den Bildschirm zu unterschiedlichen Zeitpunkten mit <b>buffer.clear()</b> löschen.
<br><br>
Man kann dieses Problem mit der Clipping-Funktion lösen, die Pimoroni in seiner Interstate75/PicoGraphics-Bibliothek anbietet. Mit ihr lassen sich die Laufschriften und ihre <b>clear()</b>-Befehle voneinander trennen. 
<br><br>
Clippings verhalten sich dabei wie Schablonen oder Ebenen, die über der Matrix liegen und Inhalte nur innerhalb festgelegter, rechteckiger Ausschnitte anzeigen. Das Koordinatensystem bleibt von ihnen unbeeinflusst. Wie man es etwa von Ebenen in Grafikprogrammen kennt, kommen sich Clippings gegenseitig nicht in die Quere (außer, man überlagert sie): Wenn man also in Clipping 1 den Befehl <b>buffer.clear()</b> ausführt, hat das keine Auswirkung auf andere Clippings. So lassen sich dann auch zwei Laufschriften unabhängig voneinander, flimmerfrei aktualisieren.
<br><br>
Ein Clipping kann man mit
<br><br>
<b>buffer.set_clip(x, y, b, h)</b>
<br><br>
erzeugen, wobei <b>b</b> die Breite und <b>h</b> die Höhe bestimmt. Mit
<br><br>
<b>buffer.remove_clip()</b>
<br><br>
löscht man das Clipping am Ende der if-Bedingung dann wieder, damit sich die Clippings nicht stapeln.
<br><br>
<i>Auch laufschrift_im_rahmen.py zeigt, wie man Clippings auf einer LED-Matrix einsetzen kann.
