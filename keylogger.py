from pynput import mouse
from pynput.mouse import Button, Controller
from pynput import keyboard

w = open("Kellog.txt",'w')
loglist = []

def logger(log):
    print(log)
    loglist.append(str(log))
    return

#Press escape to finish recording
def on_press(key):
    try:
        logger('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        logger('special key {0} pressed'.format(
            key))
        if key == keyboard.Key.esc:
            print("logtime")
            w.writelines("%s\n" % l for l in loglist)
            w.close()
            print("Log recorded")

def on_click(x, y, button, pressed):
    logger('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))

with keyboard.Listener(on_press=on_press) as k_listener, mouse.Listener(on_click=on_click) as m_listener:
    k_listener.join()
    m_listener.join()    
