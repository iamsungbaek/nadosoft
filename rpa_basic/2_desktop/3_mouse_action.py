import pyautogui
pyautogui.mouseInfo()

pyautogui.sleep(3) #3초 대기
#print(pyautogui.position())




#pyautogui.click(2606, 51, duration=1)

#pyautogui.mouseDown() #드래그 드랍할때 사용
#pyautogui.mouseUp()   #드래그 드랍할때 사용

#pyautogui.doubleClick()
#pyautogui.Click(clicks=500) #500 번 클릭 지정

#pyautogui.moveTo(200,200) # 마우스 이동
#pyautogui.moveDown() # 마우스 버튼 누른 상태
#pyautogui.moveTo(300,300) # 마우스 이동
#pyautogui.moveUp() # 마우스 버튼 뗀 상태

pyautogui.rightClick()
pyautogui.middlClick()
pyautogui.drag()
pyautogui.drag(100,0)
pyautogui.dragTo(222,445)


pyautogui.scroll(222,445)

