import time
import unittest
from appium import webdriver
import ctypes
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

    def test_click_new_level(self):
        print(self.driver.window_handles)
        background_txt_before_new_lvl = self.driver.find_element_by_accessibility_id(
            "Background-01.png.<empty>.LevelEditor - 1.0.0").text
        self.assertEqual(background_txt_before_new_lvl, "Background-01.png")
        new_lvl_btn = self.driver.find_element_by_name("New level")
        new_lvl_btn.click()
        time.sleep(1)
        background_txt_after_new_lvl = self.driver.find_element_by_accessibility_id(
            ".<empty>.LevelEditor - 1.0.0").text
        self.assertEqual(background_txt_after_new_lvl,"")

    def test_open_level(self):
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
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(1)
        print("ON MAIN")
        self.driver.switch_to.window(self.driver.current_window_handle)
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        background_lvl_3 = self.driver.find_element_by_name("Background-03.png").text
        self.assertEqual(background_lvl_3, "Background-03.png")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
