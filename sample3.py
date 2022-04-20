from pynput import keyboard
from pynput.mouse import Listener
# from pynput.keyboard import Key, Controller
import logging
import sys




logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

# keyboard = Controller()

# def on_press(key):
#     try:
#         logging.info(f"key_pressed with ({key.char})")
#         if key.char == keyboard.esc:
#             sys.exit()
            
#     except AttributeError:
#         logging.info(f"key_pressed with ({key})")

# def on_release(key):
#     logging.info(f"key_release with ({key})")
#     # if key == keyboard.esc:
#     #     # Stop listener
#     #     return False

# def on_move(x, y):
#     logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
    print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

# The event listener will be running in this block
with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.esc: break

        print('Received event {}'.format(event))

with Listener(on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()