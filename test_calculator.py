import time
import unittest
from appium import webdriver
import ctypes

from selenium.common.exceptions import StaleElementReferenceException
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
        self.driver.find_element_by_accessibility_id("Open Level.<empty>.LevelEditor - 1.0.0").click()
        time.sleep(1)
        print(self.driver.window_handles)
        self.driver.w3c = False
        self.driver.switch_to.window(self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[0])
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_name("assets").click()
        self.driver.find_element_by_name("Abrir").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_name("Levels").click()
        self.driver.find_element_by_name("Abrir").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_name("Level3").click()
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
        self.change_window_to_first_handle()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("Open Level.<empty>.LevelEditor - 1.0.0").click()
        print(self.driver.window_handles)
        self.driver.w3c = False
        self.driver.switch_to.window(self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[0])
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        time.sleep(2)
        self.change_window_to_first_handle()
        self.driver.find_element_by_name("assets").click()
        self.driver.find_element_by_name("Abrir").click()
        time.sleep(2)
        self.change_window_to_first_handle()
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
        self.open_lvl_folder()
        self.change_window_to_first_handle()
        self.driver.find_element_by_name("Guadar").click()


    def test_02_open_level(self):
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
        i = 2
        elem_exists = True
        while elem_exists and i < 10:
            try:
                self.open_lvl_folder()
                self.change_window_to_first_handle()
                elements = self.driver.find_elements_by_xpath("//*[@Name='Vista Elementos']/*")
                time.sleep(2)
                self.change_window_to_first_handle()
                elements[i].click()
                self.change_window_to_first_handle()
                self.driver.find_element_by_name("Abrir").click()
                self.change_window_to_first_handle()
                lvl_dict = {
                    "lvl1": "Background-01.png",
                    "lvl2": "Background-02.png",
                    "lvl3": "Background-03.png",
                    "lvl4": "Background-04.png",
                    "lvl5": "Background-05.png",
                    "lvl6": "Background-05.png",
                }
                search_str = "lvl" + str(i - 1)
                lvl_loaded = self.driver.find_element_by_name(lvl_dict[search_str])
                self.assertIsNotNone(lvl_loaded)
                i += 1
            except StaleElementReferenceException:
                self.driver.find_element_by_name("Cancelar").click()
                elem_exists = False
                break

    def test(self):
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
        # USE VISUAL REGRESSION





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
