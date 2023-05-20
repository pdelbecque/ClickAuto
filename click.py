import pyautogui
import time

location = pyautogui.locateOnScreen('accepter.png')
pyautogui.click(location)
print(location)
location = pyautogui.locateOnScreen('croix3.png')
pyautogui.click(location)
print(location)
location = pyautogui.locateOnScreen('croix1.png')
pyautogui.click(location)
print(location)
location = pyautogui.locateOnScreen('croix2.png')
pyautogui.click(location)

print("ok")
print("ok2")