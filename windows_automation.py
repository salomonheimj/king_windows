import time
import unittest
from appium import webdriver
import ctypes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.common.touch_action import TouchAction

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys


def bring_window_to_top(window_handle):
    """Brings the specified window to the top."""
    ctypes.windll.user32.BringWindowToTop(window_handle)
class SimpleCalculatorTests(unittest.TestCase):

    @classmethod

    def setUpClass(self):
        #set up appium
        desired_caps = {}
        desired_caps["app"] = "C:\\Users\\salom\\Desktop\\salomon\\levelEditor.exe"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= desired_caps)

    def open_lvl_3(self):
        self.change_window_to_first_handle()
        self.driver.find_element_by_accessibility_id("Open Level.<empty>.LevelEditor - 1.0.0").click()
        self.change_window_to_first_handle()
        wait = WebDriverWait(self.driver, 30)
        time.sleep(1)
        print(self.driver.window_handles)
        self.driver.w3c = False
        self.driver.switch_to.window(self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[0])
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        self.driver.implicitly_wait(30)
        assets_elem = wait.until(EC.element_to_be_clickable((By.NAME, "assets")))
        assets_elem.click()
        self.driver.find_element_by_name("Abrir").click()
        self.driver.implicitly_wait(30)
        levels_elem = wait.until(EC.element_to_be_clickable((By.NAME, "Levels")))
        levels_elem.click()
        self.driver.find_element_by_name("Abrir").click()
        self.driver.implicitly_wait(2)
        level_3_elem = wait.until(EC.element_to_be_clickable((By.NAME, "Level3")))
        level_3_elem.click()
        self.driver.find_element_by_name("Abrir").click()
        print("FINISH FILE SELECTION")

    def change_window_to_first_handle(self):
        print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(1)
        print("ON MAIN")
        self.driver.switch_to.window(self.driver.current_window_handle)
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)

    def reset_test_3(self):
        i = 0
        while i < 26:
            self.driver.find_element_by_accessibility_id(".<empty>.LevelEditor - 1.0.0").send_keys(Keys.BACK_SPACE)
            i += 1
        background_field = self.driver.find_element_by_accessibility_id("Background-01.png.<empty>.LevelEditor - 1.0.0")
        background_field.click()
        print("AFTER SELECTION DROPDOWN")
        self.change_window_to_first_handle()
        self.driver.find_element_by_name("Background-03.png").click()
        print("AFTER CLICK")
        self.change_window_to_first_handle()
        background_lvl_change = self.driver.find_element_by_name("Background-03.png").text
        self.assertEqual(background_lvl_change, "Background-03.png")
        self.driver.find_element_by_accessibility_id("Save.<empty>.LevelEditor - 1.0.0").click()


    def open_lvl_folder(self):
        wait = WebDriverWait(self.driver, 30)
        self.change_window_to_first_handle()
        time.sleep(2)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_accessibility_id("Open Level.<empty>.LevelEditor - 1.0.0").click()
        print(self.driver.window_handles)
        self.driver.w3c = False
        self.driver.switch_to.window(self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[0])
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        self.change_window_to_first_handle()
        self.driver.implicitly_wait(30)
        element_assets = wait.until(EC.element_to_be_clickable((By.NAME, 'assets')))
        element_assets.click()
        self.driver.find_element_by_name("Abrir").click()
        self.change_window_to_first_handle()
        self.driver.implicitly_wait(30)
        elements_levels = wait.until(EC.element_to_be_clickable((By.NAME, 'Levels')))
        elements_levels.click()
        self.driver.find_element_by_name("Abrir").click()
        time.sleep(2)

    def open_lvl_folder_from_assets(self):
        self.change_window_to_first_handle()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name("assets").click()
        self.driver.find_element_by_name("Abrir").click()
        self.change_window_to_first_handle()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name("Levels").click()
        self.driver.find_element_by_name("Abrir").click()
        time.sleep(2)

    def test_01_click_new_level(self):
        print(self.driver.window_handles)
        background_txt_before_new_lvl = self.driver.find_element_by_accessibility_id(
            "Background-01.png.<empty>.LevelEditor - 1.0.0").text
        self.assertEqual(background_txt_before_new_lvl, "Background-01.png")
        new_lvl_btn = self.driver.find_element_by_name("New level")
        new_lvl_btn.click()
        time.sleep(1)
        background_txt_after_new_lvl = self.driver.find_element_by_accessibility_id(
            ".<empty>.LevelEditor - 1.0.0").text
        self.assertEqual(background_txt_after_new_lvl, "")
        title_field = self.driver.find_element_by_accessibility_id(".<empty>.LevelEditor - 1.0.0")
        title_field.send_keys(" Level6Salomon")
        self.change_window_to_first_handle()
        self.driver.find_element_by_accessibility_id("Save.<empty>.LevelEditor - 1.0.0").click()
        self.open_lvl_folder_from_assets()
        self.change_window_to_first_handle()
        self.driver.find_element_by_accessibility_id("FileNameControlHost").send_keys("Level7")
        self.driver.find_element_by_name("Guardar").click()
        try:
            self.change_window_to_first_handle()
            self.driver.find_element_by_name("Sí").click()
        except:
            pass


    def test_02_open_level(self):
        self.driver.implicitly_wait(30)
        self.open_lvl_3()
        self.change_window_to_first_handle()
        background_lvl_3 = self.driver.find_element_by_name("Background-03.png").text
        self.assertEqual(background_lvl_3, "Background-03.png")
        title_field = self.driver.find_element_by_accessibility_id(".<empty>.LevelEditor - 1.0.0")
        title_field.send_keys(" Modified for Salomon Test")
        background_field = self.driver.find_element_by_accessibility_id("Background-03.png.<empty>.LevelEditor - 1.0.0")
        background_field.click()
        print("AFTER SELECTION DROPDOWN")
        self.change_window_to_first_handle()
        self.driver.find_element_by_name("Background-01.png").click()
        print("AFTER CLICK")
        self.change_window_to_first_handle()
        background_lvl_change = self.driver.find_element_by_name("Background-01.png").text
        self.assertEqual(background_lvl_change, "Background-01.png")
        self.driver.find_element_by_accessibility_id("Save.<empty>.LevelEditor - 1.0.0").click()
        self.open_lvl_3()
        self.change_window_to_first_handle()
        background_lvl_change_after_save = self.driver.find_element_by_name("Background-01.png").text
        self.assertEqual(background_lvl_change_after_save, "Background-01.png")
        self.reset_test_3()

    def test_03_open_all_tests(self):
        time.sleep(3)
        i = 2
        elem_exists = True
        while elem_exists and i < 10:
            self.open_lvl_folder()
            self.change_window_to_first_handle()
            elements = self.driver.find_elements_by_xpath("//*[@Name='Vista Elementos']/*")
            self.change_window_to_first_handle()
            wait = WebDriverWait(self.driver, 30)
            self.driver.implicitly_wait(30)
            level = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@Name='Vista Elementos']/*")))
            level[i].click()
            self.change_window_to_first_handle()
            self.driver.find_element_by_name("Abrir").click()
            self.change_window_to_first_handle()
            lvl_dict = {
                "lvl1": "Background-01.png",
                "lvl2": "Background-02.png",
                "lvl3": "Background-03.png",
                "lvl4": "Background-04.png",
                "lvl5": "Background-05.png",
                "lvl6": "Background-01.png",
                "lvl7": "Background-05.png"
            }
            search_str = "lvl" + str(i - 1)
            i += 1
            print(i)
            try:
                lvl_loaded = self.driver.find_element_by_name(lvl_dict[search_str])
                self.assertIsNotNone(lvl_loaded)
            except NoSuchElementException:
                elem_exists = False

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
