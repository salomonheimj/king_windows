from selenium.webdriver.common.by import By
from appium import webdriver


class LevelEditorPage(object):

    def __init__(self, driver):
        self.driver = driver

    @property
    def new_level_button(self):
        return self.driver.find_element_by_name("New level")

    @property
    def open_level_button(self):
        return self.driver.find_element_by_accessibility_id("Open Level.<empty>.LevelEditor - 1.0.0")

    @property
    def title_field(self):
        return self.driver.find_element_by_accessibility_id(".<empty>.LevelEditor - 1.0.0")

    @property
    def background_selection_field(self):
        return self.driver.find_element_by_xpath("//*[@LocalizedControlType='cuadro combinado']")

    @property
    def background_01_field(self):
        return self.driver.find_element_by_name("Background-01.png")

    @property
    def background_03_field(self):
        return self.driver.find_element_by_name("Background-03.png")

    @property
    def save_button(self):
        return self.driver.find_element_by_accessibility_id("Save.<empty>.LevelEditor - 1.0.0")

