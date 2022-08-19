import pyautogui as pg, time
# passwords.txt - your password file  
time.sleep(5);SPAM = open("passwords.txt", "r")
for line in SPAM:
    pg.typewrite(line)
    pg.press("enter")
    pg.click(***, ***)
