import random
import time

import pyautogui

from standard.clickActions import ClickActions
from standard.imagesearch import imagesearch

"""""
space between left to right
1202, 318 -> 1267, 314 

space between up to down
1180, 334 - >1180, 339

Inventory item
width: 38 
length: 26

item to delete info:
click : 1258 - 310

max X 
X left: 1200
X right:1301

max Y
Y up:   354 
Y down: 369
"""""


class randomPositioner:

    def __init__(self):
        self.click = ClickActions()

    @staticmethod
    def r_move_to_drop_x():
        return random.randint(-20, 20)

    @staticmethod
    def r_move_to_drop_y():
        return random.randint(45, 60)

    @staticmethod
    def r_click_inventory_item():
        return random.randint(0, 40)

    def drop_inventory(self, first_item_in_inventory):
        inventory_empty = False
        while not inventory_empty:
            first_item = imagesearch(first_item_in_inventory)
            if first_item[0] != -1:
                click_x = first_item[0] + self.r_click_inventory_item()
                click_y = first_item[1] + self.r_click_inventory_item()
                print("position : ", first_item[0], first_item[1])
                pyautogui.moveTo(click_x, click_y)
                self.click.click_right()
                self.move_to_delete(click_x, click_y)
                self.click.click_left()
                time.sleep(random.uniform(0.6, 1.2))
            else:
                inventory_empty = True

    @staticmethod
    def move_to_delete(x, y):
        inventory_x_radius = 1 + random.uniform(-58, 33)
        inventory_y_radius = 2 + random.randint(44, 59)
        pyautogui.moveTo(x + inventory_x_radius, y + inventory_y_radius)

    def click_on(self, image):
        to_click = imagesearch(image)
        if to_click[0] != -1:
            click_x = to_click[0]
            click_y = to_click[1]
            pyautogui.moveTo(click_x, click_y)
            self.click.click_right()
        else:
            print('image not found')


i = randomPositioner()
#i.drop_inventory("basic_log.png")
i.click_on("fishing_spot.png")

