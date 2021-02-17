
import pyautogui
import keyboard
import win32api, win32con
import time

keyboard.wait('esc')

black = (0,0,0)

road1 = (481, 553)
road2 = (510, 553)
road3 = (714, 553)
road4 = (848, 553)

def click(pos):
    print('dected--------')
    win32api.SetCursorPos(pos)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while True:
    print(pyautogui.pixel(road1[0] , road1[1]))
    if pyautogui.pixel(road1[0] , road1[1]) == black:
        click(road1)

    if pyautogui.pixel(road2[0] , road2[1]) == black:
        click(road2)

    if pyautogui.pixel(road3[0] , road3[1]) == black:
        click(road3)

    if pyautogui.pixel(road4[0] , road4[1]) == black:
        click(road4)
