from selenium.webdriver.common.by import By
from appium import webdriver


class ExplorerPage(object):

    def __init__(self, driver):
        self.driver = driver

    @property
    def assets_folder(self):
        return self.driver.find_element_by_name("assets")

    @property
    def levels_folder(self):
        return self.driver.find_element_by_name("Levels")

    @property
    def all_levels(self):
        return self.driver.find_elements_by_xpath("//*[@Name='Vista Elementos']/*")

    @property
    def open_button(self):
        return self.driver.find_element_by_name("Abrir")

    @property
    def save_button(self):
        return self.driver.find_element_by_name("Guardar")

    @property
    def confirm_button(self):
        return self.driver.find_element_by_name("Sí")

    @property
    def file_name_box(self):
        return self.driver.find_element_by_accessibility_id("FileNameControlHost")
