from pynput.mouse import Listener
from pynput.keyboard import Key, Controller
import logging

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

keyboard = Controller()

def on_press(key):
    try:
        logging.info(f"key_pressed with ({key.char})")
    except AttributeError:
        logging.info(f"key_pressed with ({key})")

def on_release(key):
    logging.info(f"key_release with ({key})")
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll, on_press=on_press, on_release=on_release) as listener:
    listener.join()
    # keyboard.press(Key.space)
    # keyboard.release(Key.space)
    