import pyglet
import time
from pyglet.window import key


window = pyglet.window.Window(width=640, height=480,caption="Tamagotchi")

jidlo = 100
def potrava(t):
    global jidlo
    jidlo = int(jidlo)
    jidlo = jidlo - 1
    jidlo = str(jidlo)

    label = pyglet.text.Label("Tamagotchi",font_size=30,x=window.width//2, y=430,anchor_x='center', anchor_y='center')
    label3 = pyglet.text.Label("",font_size=30,x=window.width//2, y=240,anchor_x='center', anchor_y='center')
    label1 = pyglet.text.Label("Hlad: " + jidlo,font_size=20,x=320, y=380,anchor_x='center', anchor_y='center')
    jidlo = int(jidlo)
    
    global obrazek1
    if jidlo > 75:
        obrazek1 = pyglet.image.load('grafika/stastny.png')
    if jidlo < 75:
        obrazek1 = pyglet.image.load('grafika/normal.png')
    if jidlo < 25:
        obrazek1 = pyglet.image.load('grafika/smutny.png')
    if jidlo <= 0:
        label3 = pyglet.text.Label("Prohrál jsi",font_size=60,x=window.width//2, y=240,anchor_x='center', anchor_y='center')
        jidlo = 1
        
    obrazek2 = pyglet.image.load("grafika/tlacitko.png")
    obrazek2.anchor_x = obrazek2.width // 2 ##this line is new
    obrazek2.anchor_y = obrazek2.height // 2
    tlacitko = pyglet.sprite.Sprite(obrazek2, x=320, y=50)

    obrazek1.anchor_x = obrazek1.width // 2 ##this line is new
    obrazek1.anchor_y = obrazek1.height // 2 ## and this li
    smajlik1 = pyglet.sprite.Sprite(obrazek1, x=320, y=220)

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        x = 320
        y = 50
        global jidlo
        jidlo = 101


    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.SPACE:
            global jidlo
            jidlo = 101

    @window.event
    def on_draw():
        window.clear()
        label.draw()
        label1.draw()
        smajlik1.draw()
        label3.draw()
        tlacitko.draw()

pyglet.clock.schedule_interval(potrava, 1/10)

pyglet.app.run()