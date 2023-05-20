pyautogui.screenshot('win10_logo.png', region=(0, 0, 50, 39))
location = pyautogui.locateOnScreen('win10_logo.png')
pyautogui.click(location)
print(location)

