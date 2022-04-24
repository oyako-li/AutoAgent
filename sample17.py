import pyautogui as pgi
import time

time.sleep(3)

a="ctrl:w"
a = a.split(':')
print(a)
pgi.hotkey(a[0],a[1])