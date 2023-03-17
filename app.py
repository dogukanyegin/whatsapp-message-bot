import pyautogui
import time
import codecs
time.sleep(3)

f=open('message.txt', "r",encoding="utf-8")

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")