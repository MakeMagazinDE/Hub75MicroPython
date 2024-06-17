<b>Ergänzung zum Heft-Artikel: Timing und Clipping</b>
<br><br>
Möchte man mehr als eine Laufschrift darstellen, kann man die <b>if</b>-Bedingung aus <i>laufschrift_mit_timing.py</i> in der Dauerschleife <b>while True:</b> samt ihrer Variablen vervielfachen. Das Beispielprogramm <i>zwei_laufschriften_regenbogen.py</i> zeigt, wie es geht und löst zudem noch folgendes Problem: ein Flimmern, das entsteht, wenn beide Laufschriften sich mit unterschiedlicher Geschwindigkeit bewegen. Dieses tritt auf, weil die beiden Schriften den Bildschirm zu unterschiedlichen Zeitpunkten mit <b>buffer.clear()</b> löschen.
<br><br>
Dieses Problem lässt sich mit der Clipping-Funktion beheben, die sich wie eine rechteckige Schablone (z. B. für Airbrush) verhält. Mit ihr kann man die Laufschriften und ihre <b>clear()</b>-Befehle nämlich voneinander trennen. Dazu erstellt man zunächst das Clipping im Bereich der ersten Laufschrift mit:
<br><br>
<b>buffer.set_clip(x, y, b, h)</b>
<br><br>
Die Breite wird mit <b>b</b> und die Höhe mit <b>h</b> bestimmt. Danach gibt man die erste Laufschrift aus und entfernt anschließend das Clipping mit:
<br><br>
<b>buffer.remove_clip()</b>
<br><br>
Anschließend erstellt man das Clipping im Bereich der zweiten Laufschrift, gibt dort die andere Laufschrift aus und entfernt das Clipping wieder. Das passiert jetzt im Wechsel so schnell, dass man lediglich die zwei Laufschriften sieht, die ohne zu Flimmern über den Bildschirm scrollen, weil ihre Darstellung sich nicht mehr in die Quere kommt.
<br><br>
<i>Eine Variation dieser Clipping-Lösung zeigt das Programm laufschrift_im_rahmen.py, in dem der Text innerhalb eines Rahmens scrollt. Man kann dieses Werkzeug also kreativ nutzen, um Layouts für seine LED-Matrix zu erstellen.
