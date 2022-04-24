import pyautogui as pgi
import time

def a(a,b):
    pgi.moveTo(int(a), int(b))
    pgi.click()

def b(a,b):
    pgi.moveTo(int(a),int(b))
    pgi.mouseUp()

def c(a,b):
    pgi.moveTo(int(a), int(b))
    pgi.rightClick()

def d(a):
    if a == "ctrl":
        pass
    elif a in ":":
        a = a.split(':')
        pgi.hotkey(a[0],a[1])
    else:
        pgi.keyDown(a)

def e(a):
    pgi.keyUp(a)


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
            log[i][2] = "ctrl"
        
        if "ctrll" == log[i][2]:
            log[i][2] = "ctrl"

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

        if "\x01" ==  log[i][2]:
            log[i][2] = "ctrl:a"
        if "\x02" ==  log[i][2]:
            log[i][2] = "ctrl:b"
        if "\x03" ==  log[i][2]:
            log[i][2] = "ctrl:c"
        if "\x04" ==  log[i][2]:
            log[i][2] = "ctrl:d"
        if "\x05" ==  log[i][2]:
            log[i][2] = "ctrl:e"
        if "\x06" ==  log[i][2]:
            log[i][2] = "ctrl:f"
        if "\x07" ==  log[i][2]:
            log[i][2] = "ctrl:g"
        if "\x08" ==  log[i][2]:
            log[i][2] = "ctrl:h"
        if "\x09" ==  log[i][2]:
            log[i][2] = "ctrl:i"
        if "\x0A" ==  log[i][2]:
            log[i][2] = "ctrl:j"
        if "\x0B" ==  log[i][2]:
            log[i][2] = "ctrl:k"
        if "\x0C" ==  log[i][2]:
            log[i][2] = "ctrl:l"
        if "\x0D" ==  log[i][2]:
            log[i][2] = "ctrl:m"
        if "\x0E" ==  log[i][2]:
            log[i][2] = "ctrl:n"
        if "\x0F" ==  log[i][2]:
            log[i][2] = "ctrl:o"
        if "\x10" ==  log[i][2]:
            log[i][2] = "ctrl:p"
        if "\x11" ==  log[i][2]:
            log[i][2] = "ctrl:q"
        if "\x12" ==  log[i][2]:
            log[i][2] = "ctrl:r"
        if "\x13" ==  log[i][2]:
            log[i][2] = "ctrl:s"
        if "\x14" ==  log[i][2]:
            log[i][2] = "ctrl:t"
        if "\x15" ==  log[i][2]:
            log[i][2] = "ctrl:u"
        if "\x16" ==  log[i][2]:
            log[i][2] = "ctrl:v"
        if "\x17" ==  log[i][2]:
            log[i][2] = "ctrl:w"
        if "\x18" ==  log[i][2]:
            log[i][2] = "ctrl:x"
        if "\x19" ==  log[i][2]:
            log[i][2] = "ctrl:y"
        if "\x1A" ==  log[i][2]:
            log[i][2] = "ctrl:z"
        

    print(log)

    for i in log:
        if 'Button.left.True' == i[1]:
            i[2] = i[2].split(':')
            i.append(1)

        if 'Button.left.False' == i[1]:
            i.append(2)
            
        if 'Button.right.True' == i[1]:
            i[2] = i[2].split(':')
            i.append(3)

        if 'Button.right.True' == i[1]:
            i.append(2)
        
        if 'Key.True' == i[1]:
            i.append(4)
        
        if 'Key.False' == i[1]:
            i.append(5)
    
    elapsed_time = 0

    for i in log:
        print(float(i[0])-elapsed_time)
        if float(i[0])-elapsed_time >=0:
            time.sleep(float(i[0])-elapsed_time)

        start_time = time.perf_counter()
        if i[3] >= 3:
            if i[3] >=4:
                if i[3] == 4:
                    d(i[2])
                else:
                    e(i[2])
            else:
                c(i[2][0],i[2][1])
        else:
            if i[3] == 1:
                a(i[2][0],i[2][1])
            else:
                b(i[2][0],i[2][1])
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        

    return True

if __name__ == "__main__":
    activator("Sun,24,Apr,2022,03,18,01")

    """ctrlr" == log[i][2]:
            log[i][2] = "ctrlright"

        if "ctrll"""