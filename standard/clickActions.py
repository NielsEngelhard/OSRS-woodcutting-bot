import pyautogui
import time
from standard.imagesearch import r


class ClickActions:

    @staticmethod
    def click_right():
        pyautogui.click(button="right")
        time.sleep(r(0.4, 0.2))  # the r function simply returns 0.4 + 0.2 * random.random()

    @staticmethod
    def click_left():
        pyautogui.click(button="left")
        time.sleep(r(0.4, 0.2))  # the r function simply returns 0.4 + 0.2 * random.random()
