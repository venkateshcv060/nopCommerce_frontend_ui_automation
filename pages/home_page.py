from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import *

class HomePage(BasePage):
    REGISTER_BTN=(By.XPATH,"//a[normalize-space()='Register']")


    def __init__(self,driver):
        super().__init__(driver)
        # self.driver=driver
        # self.wait=WebDriverWait(driver,10)

    def get_title(self):
        self.wait.until(EC.title_contains("Home"))
        return self.driver.title

    def click_register(self):
        self.hover(self.REGISTER_BTN)
        self.click(self.REGISTER_BTN)


