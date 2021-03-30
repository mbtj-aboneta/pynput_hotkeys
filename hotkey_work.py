#note: Clean this up
from pynput.keyboard import Key
from pynput.keyboard import Controller as kController 
from pynput.mouse import Controller as mController
from pynput.mouse import Button
from pynput import keyboard


#note: this too
mcont = mController()
kcont = kController()

def mclick(x,y):
    mcont.position = (x,y)
    mcont.press(Button.left)
    mcont.release(Button.left)
    return
def kpress(k):
    kcont.press(k)
    kcont.release(k)
    return

def on_press(key):
    if key == keyboard.KeyCode(char="0"):
        mclick(369, 309)
        kpress(Key.page_down)
        kpress(Key.page_down)
    if key == keyboard.KeyCode(char="8"):
        mclick(50, 402)
    if key == keyboard.KeyCode(char="7"):
        mcont.position = (461, 482)
    return

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()



