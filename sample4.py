from email.policy import default
from pynput import mouse, keyboard
import sys
import logging
from time import gmtime, strftime

filename = strftime("%a,%d,%b,%Y,%H,%M,%S", gmtime())
logging.basicConfig(filename=f"{filename}.log", level=logging.DEBUG, format='%(asctime)s,%(msecs)03d,%(message)s', datefmt='%Y,%m,%d,%H,%M,%S')

def click(x, y, button, pressed):
    logging.info(f'{button},{pressed},({x}, {y})')

    print('{2} が {0} された座標： {1}'.format(
        'Pressed' if pressed else 'Released',(x, y), button))

def press(key):
    try:
        logging.info(f"press,({key.char})")

        print('アルファベット {0} が押されました'.format(key.char))
    except AttributeError:
        logging.info(f"press,({key})")
        print('スペシャルキー {0} が押されました'.format(key))

def release(key):
    try:
        logging.info(f"release,({key.char})")
        print('{0} が離されました'.format(key))
    except AttributeError:
        logging.info(f"release,({key})")
        print('スペシャルキー {0} が押されました'.format(key))
    
# mouseのリスナー
mouse_listener = mouse.Listener(
    on_click=click,)

# keyboardのリスナー
keyboard_listener = keyboard.Listener(
    on_press=press,
    on_release=release)

mouse_listener.start()
keyboard_listener.start()
print(filename)

try:
    while True: pass
except KeyboardInterrupt:
    mouse_listener.stop()       # mouseのListenerを止める
    keyboard_listener.stop()   
    sys.exit