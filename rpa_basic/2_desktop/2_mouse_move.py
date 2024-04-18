import pyautogui

#절대좌표
#pyautogui.moveTo(100,110) # 지정한 위치로 마우스 이동
pyautogui.moveTo(100,210, duration=2) # 2초 동한 지정한 위치로 마우스 이동
print(pyautogui.position()) #point x,y


#상대좌표
pyautogui.move(100,210, duration=2) # 2초 동한 지정한 위치로 마우스 이동
print(pyautogui.position()) #point x,y

pyautogui.move(20,110, duration=3) # 2초 동한 지정한 위치로 마우스 이동
print(pyautogui.position()) #point x,y


p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)