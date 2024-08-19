import pyautogui
import time


while True:
    w=input("enter your messege:")
    if w == "end":
        break
    ##makskone
    time.sleep(5)
    for i in range(10):
        pyautogui.press("enter")
        