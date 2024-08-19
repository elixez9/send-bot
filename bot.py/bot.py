import pyautogui
import time


while True:
    w=input("w:")
    if w == "end":
        break
    time.sleep(5)
    for i in range(10):
        pyautogui.press("enter")