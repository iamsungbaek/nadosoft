import pyperclip, pyautogui
# pyperclip.copy("나도코딩")
# pyautogui.hotkey("ctrl", "v")

def my_write(text):
  pyperclip.copy(text)
  pyautogui.hotkey("ctrl", "v")

my_write("자고싶다")
