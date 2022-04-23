import pyautogui as pgi
import time

def a(a,b):
    pgi.moveTo(int(a), int(b))
    pgi.click()

def b():
    pgi.mouseUp()

def c(a,b):
    pgi.moveTo(int(a), int(b))
    pgi.rightClick()

def d(a):
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
                b()
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        

    return True

if __name__ == "__main__":
    activator("Sat,23,Apr,2022,07,22,52")