import os
import time
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import numpy as np
import ctypes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from level_editor_page import LevelEditorPage
from explorer_page import ExplorerPage

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

import cv2
import pyautogui


def bring_window_to_top(window_handle):
    """Brings the specified window to the top."""
    ctypes.windll.user32.BringWindowToTop(window_handle)


class WindowsAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # set up appium
        desired_caps = {}
        desired_caps["app"] = "C:\\Users\\salom\\Desktop\\salomon\\levelEditor.exe"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps)

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()

    def open_lvl_1(self):
        level_editor = LevelEditorPage(self.driver)
        explorer = ExplorerPage(self.driver)
        self.change_window_to_first_handle()
        level_editor.open_level_button.click()
        self.change_window_to_first_handle()
        wait = WebDriverWait(self.driver, 30)
        time.sleep(1)
        self.driver.w3c = False
        self.driver.switch_to.window(self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.implicitly_wait(30)
        assets_elem = wait.until(EC.element_to_be_clickable((By.NAME, "assets")))
        assets_elem.click()
        explorer.open_button.click()
        self.driver.implicitly_wait(30)
        levels_elem = wait.until(EC.element_to_be_clickable((By.NAME, "Levels")))
        levels_elem.click()
        explorer.open_button.click()
        self.driver.implicitly_wait(30)
        level_3_elem = wait.until(EC.element_to_be_clickable((By.NAME, "Level1")))
        level_3_elem.click()
        explorer.open_button.click()
        print("FINISH FILE SELECTION")

    def open_lvl_3(self):
        level_editor = LevelEditorPage(self.driver)
        explorer = ExplorerPage(self.driver)
        self.change_window_to_first_handle()
        level_editor.open_level_button.click()
        self.change_window_to_first_handle()
        wait = WebDriverWait(self.driver, 30)
        time.sleep(1)
        self.driver.w3c = False
        self.driver.switch_to.window(self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.implicitly_wait(30)
        assets_elem = wait.until(EC.element_to_be_clickable((By.NAME, "assets")))
        assets_elem.click()
        explorer.open_button.click()
        self.driver.implicitly_wait(30)
        levels_elem = wait.until(EC.element_to_be_clickable((By.NAME, "Levels")))
        levels_elem.click()
        explorer.open_button.click()
        self.driver.implicitly_wait(30)
        level_3_elem = wait.until(EC.element_to_be_clickable((By.NAME, "Level3")))
        level_3_elem.click()
        explorer.open_button.click()
        print("FINISH FILE SELECTION")

    def change_window_to_first_handle(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(1)
        self.driver.switch_to.window(self.driver.current_window_handle)

    def reset_test_3(self):
        level_editor_page = LevelEditorPage(self.driver)
        i = 0
        while i < 26:
            level_editor_page.title_field.send_keys(Keys.BACK_SPACE)
            i += 1
        level_editor_page.background_01_field.click()
        self.change_window_to_first_handle()
        level_editor_page.background_03_field.click()
        self.change_window_to_first_handle()
        background_lvl_change = level_editor_page.background_03_field.text
        self.assertEqual(background_lvl_change, "Background-03.png")
        level_editor_page.save_button.click()

    def open_lvl_folder(self):
        level_editor_page = LevelEditorPage(self.driver)
        explorer_page = ExplorerPage(self.driver)
        wait = WebDriverWait(self.driver, 30)
        self.change_window_to_first_handle()
        time.sleep(2)
        self.driver.implicitly_wait(30)
        level_editor_page.open_level_button.click()
        self.driver.w3c = False
        self.driver.switch_to.window(self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.change_window_to_first_handle()
        self.driver.implicitly_wait(30)
        element_assets = wait.until(EC.element_to_be_clickable((By.NAME, 'assets')))
        element_assets.click()
        explorer_page.open_button.click()
        self.change_window_to_first_handle()
        self.driver.implicitly_wait(30)
        elements_levels = wait.until(EC.element_to_be_clickable((By.NAME, 'Levels')))
        elements_levels.click()
        explorer_page.open_button.click()
        time.sleep(2)

    def open_lvl_folder_from_assets(self):
        explorer_page = ExplorerPage(self.driver)
        self.change_window_to_first_handle()
        self.driver.implicitly_wait(30)
        self.change_window_to_first_handle()
        explorer_page.assets_folder.click()
        explorer_page.open_button.click()
        self.change_window_to_first_handle()
        self.driver.implicitly_wait(30)
        explorer_page.levels_folder.click()
        explorer_page.open_button.click()
        time.sleep(2)

    def put_all_blocks(self):
        app_window = self.driver.get_window_size()
        print(self.driver.get_window_size())
        window_width, window_height = app_window['width'], app_window["height"]
        print(window_width)
        print(window_height)
        initial_x = 0.7
        initial_y = 1
        row_x = 0.5
        row_y = 0.5
        i = 0
        while i < 14:
            x = window_width * initial_x
            y = window_height * initial_y
            # Perform the click
            pyautogui.click(x, y)
            initial_x += 0.05
            x_row = window_width * row_x
            y_row = window_height * row_y
            pyautogui.click(x_row, y_row)
            row_x += 0.055
            i += 1

    def test_01_click_new_level(self):
        level_editor_page = LevelEditorPage(self.driver)
        explorer = ExplorerPage(self.driver)
        background_txt_before_new_lvl = level_editor_page.background_01_field.text
        self.assertEqual(background_txt_before_new_lvl, "Background-01.png")
        level_editor_page.new_level_button.click()
        time.sleep(1)
        background_txt_after_new_lvl = level_editor_page.title_field.text
        self.assertEqual(background_txt_after_new_lvl, "")
        time.sleep(2)
        self.put_all_blocks()
        level_editor_page.title_field.send_keys(" Level7Salomon")
        level_editor_page.background_selection_field.click()
        self.change_window_to_first_handle()
        level_editor_page.background_01_field.click()
        self.change_window_to_first_handle()
        level_editor_page.save_button.click()
        self.open_lvl_folder_from_assets()
        self.change_window_to_first_handle()
        explorer.file_name_box.send_keys("Level7")
        explorer.save_button.click()
        try:
            self.change_window_to_first_handle()
            explorer.confirm_button.click()
        except:
            pass

    def test_02_open_level(self):
        level_editor_page = LevelEditorPage(self.driver)
        self.driver.implicitly_wait(30)
        self.open_lvl_3()
        self.change_window_to_first_handle()
        background_lvl_3 = level_editor_page.background_03_field.text
        self.assertEqual(background_lvl_3, "Background-03.png")
        level_editor_page.title_field.send_keys(" Modified for Salomon Test")
        level_editor_page.background_03_field.click()
        print("AFTER SELECTION DROPDOWN")
        self.change_window_to_first_handle()
        level_editor_page.background_01_field.click()
        print("AFTER CLICK")
        self.change_window_to_first_handle()
        background_lvl_change = level_editor_page.background_01_field.text
        self.assertEqual(background_lvl_change, "Background-01.png")
        level_editor_page.save_button.click()
        self.open_lvl_3()
        self.change_window_to_first_handle()
        background_lvl_change_after_save = level_editor_page.background_01_field.text
        self.assertEqual(background_lvl_change_after_save, "Background-01.png")
        self.reset_test_3()

    def test_03_open_all_tests(self):
        explorer_page = ExplorerPage(self.driver)
        time.sleep(3)
        i = 2
        elem_exists = True
        while elem_exists and i < 9:
            self.open_lvl_folder()
            self.change_window_to_first_handle()
            elements = explorer_page.all_levels
            self.change_window_to_first_handle()
            wait = WebDriverWait(self.driver, 30)
            self.driver.implicitly_wait(30)
            level = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@Name='Vista Elementos']/*")))
            level[i].click()
            self.change_window_to_first_handle()
            explorer_page.open_button.click()
            self.change_window_to_first_handle()
            lvl_dict = {
                "lvl1": "Background-01.png",
                "lvl2": "Background-02.png",
                "lvl3": "Background-03.png",
                "lvl4": "Background-04.png",
                "lvl5": "Background-05.png",
                "lvl6": "Background-01.png",
                "lvl7": "Background-01.png"
            }
            search_str = "lvl" + str(i - 1)
            i += 1
            print(i)
            try:
                lvl_loaded = self.driver.find_element_by_name(lvl_dict[search_str])
            except NoSuchElementException:
                lvl_loaded = None
                elem_exists = False

            self.assertIsNotNone(lvl_loaded)

    def test_04_place_specific_tiles_in_specific_places(self):
        level_editor_page = LevelEditorPage(self.driver)
        # self.change_window_to_first_handle()
        # self.driver.find_element_by_accessibility_id("TitleBar").click()
        self.change_window_to_first_handle()
        self.open_lvl_1()
        self.change_window_to_first_handle()
        app_window = self.driver.get_window_size()
        print(self.driver.get_window_size())
        window_width, window_height = app_window['width'], app_window["height"]
        # select red block
        pyautogui.click(window_width * 0.7, window_height * 1)
        # replace gray with red one
        pyautogui.click(window_width * 0.45, window_height * 0.45)
        # select blue block
        pyautogui.click(window_width * 0.82, window_height * 1)
        # replace with yellow with blue
        pyautogui.click(window_width * 0.45, window_height * 0.55)
        # place any block on 4th column 1st row
        pyautogui.click(window_width * 0.65, window_height * 0.28)
        self.change_window_to_first_handle()
        self.change_window_to_first_handle()
        # level_editor_page.save_button.click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WindowsAppTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
