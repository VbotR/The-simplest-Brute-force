import os 
import random 
import time 
import pyautogui

print ('Cntrl+C')

pyautogui.PAUSE = 0.2

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        
   
except:
    os.system('clear')
    print('exit')
