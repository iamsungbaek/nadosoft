import pyautogui

#pyautogui.useImageNotFoundException()


#file_menu = pyautogui.locateOnScreen("file_menu.png")
#file_menu = pyautogui.locateOnScreen("file_menu.png", grayscale=True)
#file_menu = pyautogui.locateOnScreen("file_menu.png", region(1488,633,1881,137)) #region(x,y,width,height)
#print(file_menu)
#pyautogui.click(file_menu)
#pyautogui.moveTo(file_menu)

#screen = pyautogui.locateOnScreen("screenshot.png")
#print(screen)

# for i in pyautogui.locateAllOnScreen("check.box.png")
#   print(i)
#   pyautogui.click(i, duration=0.5)


#계속 기다리기
#자동화 대상이 바로 보여지지 않는 경우

file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# # if file_menu_notepad:
# #   pyautogui.click(file_menu_notepad)
# # else:
# #   print("발견실패")
# while file_menu_notepad is None:
#   file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#   print("발견실패")

# pyautogui.click(file_menu_notepad)


#일정 시간동안 기다리기
import time
import sys

timeout = 10 #지정식산
start = time.time() #시작시간
file_menu_notepad = None
while file_menu_notepad is None:
  file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
  end = time.time() #종료시간
  if end - start > timeout: # 지정한 10초를 초과하면
      print("시간 종료")
      sys.exit()

pyautogui.click(file_menu_notepad)