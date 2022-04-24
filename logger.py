from pynput import mouse, keyboard
import sys
import logging
# from time import gmtime, strftime
import time

pre_time = 0
command = True
logging.basicConfig(level=logging.INFO, format='%(message)s')
_log = logging.getLogger('log_phase')


def logger(_filename):
    global pre_time
    global command
    global _log

    file_handler = logging.FileHandler(f"./log/{_filename}.log")
    file_handler.setLevel(logging.INFO)
    _log.addHandler(file_handler)
    

    pre_time = time.time()
    command = True

        
    # mouseのリスナー
    mouse_listener = mouse.Listener(
        on_click=click,)

    # keyboardのリスナー
    keyboard_listener = keyboard.Listener(
        on_press=press,
        on_release=release)

    mouse_listener.start()
    keyboard_listener.start()

    while command: pass

    mouse_listener.stop()       # mouseのListenerを止める
    keyboard_listener.stop()
    _log.handlers.clear()
    return True

def click(x, y, button, pressed):
    global pre_time
    global _log

    now = time.time()
    time_span = now - pre_time

    action = str(button)+'.'+str(pressed)
    _log.info(f'{time_span},{action},{x}:{y}')
    pre_time = now

def press(key):

    global pre_time
    global command
    global _log

    now = time.time()
    time_span = now - pre_time
    action = 'Key.True'
    try:
        if key.char == None:
            _log.info(f"{time_span},{action},{key}")
            pre_time = now
            return

        _log.info(f"{time_span},{action},{key.char}")
        pre_time = now

    except AttributeError:
        if str(key) == 'Key.esc': 
            command = False
            return

        _log.info(f"{time_span},{action},{key}")
        pre_time = now

def release(key):
    global pre_time
    global _log

    now = time.time()
    time_span = now - pre_time
    action = 'Key.False'
    try:
        if key.char == None:
            _log.info(f"{time_span},{action},{key}")
            pre_time = now
            return
        
        _log.info(f"{time_span},{action},{key.char}")
        pre_time = now

    except AttributeError:
        _log.info(f"{time_span},{action},{key}")
        pre_time = now
    
if __name__ == '__main__':
    filename = time.strftime("%a,%d,%b,%Y,%H,%M,%S", time.gmtime())
    logger(filename)
    print(filename)