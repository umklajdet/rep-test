import pyautogui as pg
import time
import os

pg.hotkey('winleft')
time.sleep(2)
pg.typewrite('notepad\n', 0.1)
#pg.hotkey('down')
#pg.typewrite('\n', 0.1)
time.sleep(3)

expect = 'Good job'

pg.hotkey('ctrl', 'n')
pg.typewrite(expect, 0.2)
pg.hotkey('ctrl', 's')
time.sleep(2)
name = 'GoodFile.txt'
path = 'C:\\Python\\' + name

if os.path.exists(name):
    os.remove(name)    

pg.typewrite(path + '\n', 0.1)
actual = ''
with open(path) as inf:
    actual = inf.readline()

if expect == actual:
    print('Passed!')
else:
    print('Failed(')
    
pg.hotkey('alt', 'F4')