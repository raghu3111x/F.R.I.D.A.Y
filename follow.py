import pyautogui as pt
import time

time.sleep(2)
while True:
    follow_list = list(pt.locateAllOnScreen('follow_button.PNG'))
    print(follow_list)
    for i in follow_list:
        #pt.center(tuple(i))
        pt.moveTo(pt.center(tuple(i)))
        pt.click()
        #time.sleep(10)
    pt.moveTo(912,586)
    pt.scroll(-380)

    time.sleep(2)