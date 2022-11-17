import pyautogui
from datetime import datetime

dataNow = datetime.now().strftime('%H-%M')

im1 = pyautogui.screenshot()
im2 = pyautogui.screenshot('Y:\.NET Framework\python\screen_' + dataNow + '.png')


print('OK')