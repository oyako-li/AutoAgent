import pyautogui as pgi
import time

def activator(filename):
    f = open(filename, 'r')

    log = []

    for line in f:
        line = line.rstrip()
        l = line.split(",")
        print(l)
        log.append(l)

    f.close()

    for i in range(len(log)):

        time.sleep(float(log[i][0]))

        if 'Button.left.True' == log[i][1]:
            r = log[i][2].split(':')
            pgi.moveTo(int(r[0]), int(r[1]))
            pgi.click()

        if 'Button.left.False' == log[i][1]:
            pgi.mouseUp()
            
        if 'Button.right.True' == log[i][1]:
            r = log[i][2].split(':')
            pgi.moveTo(int(r[0]), int(r[1]))
            pgi.rightClick()

        if 'Button.right.True' == log[i][1]:
            pgi.mouseUp()
        
        if 'Key.True' == log[i][1]:
            pgi.keyDown(log[i][2])
        
        if 'Key.False' == log[i][1]:
            pgi.keyUp(log[i][2])
    
    return True