import pyautogui as pgi
import time

def activator(_filename):
    f = open(f"./log/{_filename}.log", 'r')

    log = []

    for line in f:
        line = line.rstrip()
        l = line.split(",")
        log.append(l)

    f.close()

    for i in range(len(log)):
        if "Key." in log[i][2]:
            log[i][2] = log[i][2][4:]

        if "_" in log[i][2]:
            log[i][2] = log[i][2].strip("_")

        if "shift" == log[i][2]:
            log[i][2] = "shiftleft"

        if "shiftr" == log[i][2]:
            log[i][2] = "shiftright"

        if "ctrlr" == log[i][2]:
            log[i][2] = "ctrlright"

        if "ctrll" == log[i][2]:
            log[i][2] = "ctrlleft"

        if "altgr" == log[i][2]:
            log[i][2] ="optionright"

        if "altl" == log[i][2]:
            log[i][2] ="optionleft"

        if "cmd" == log[i][2]:
            log[i][2] = "command"

        if "<28>" == log[i][2]:
            log[i][2] = "nonconvert"

        if "<29>" == log[i][2]:
            log[i][2] = "convert"

    print(log)
    
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

    
if __name__ == "__main__":
    activator("Sat,23,Apr,2022,07,22,52")