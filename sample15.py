import pyautogui as pgi
import time

time.sleep(3)

pgi.keyDown('ctrl')
pgi.keyDown('w')
pgi.keyUp('w')
pgi.keyUp('ctrl')