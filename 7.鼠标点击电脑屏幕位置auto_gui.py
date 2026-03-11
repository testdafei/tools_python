import pyautogui
import time
# time.sleep(3)
i = 1
while 1:
   # if i%2==0:
   #    pyautogui.click(1500, 600, clicks=1, interval=0.0, button='left')
   # else:
   #    pyautogui.click(1600, 700, clicks=1, interval=0.0, button='left')
   wide,heigh = pyautogui.size()
   print(wide,heigh)
   # pyautogui.click(862, 47, clicks=2, interval=0.5, button='left')   #对应位置点击两次，0.5S一次
   pyautogui.click(1360, 600, clicks=1, interval=10, button='left')   #对应位置点击1次，5S一次
   # pyautogui.click(570, 888, duration=2)  # 移动到对应位置后点击
   # time.sleep(3)
   print("==================this is the : "+str(i)+" times click=================")
   i += 1
