from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import *
from utilities.waits import *

class ProductPage(BasePage):
    PRODUCT_ADD_TO_CART=(By.ID,"add-to-cart-button-4")
    SHOPPING_CART_BUTTON=(By.ID,"topcartlink")
    CART_ADDED_CLOSE=(By.XPATH,"//span[@class='close']")

    def __init__(self, driver):
        # super().__init__(driver)
          self.driver=driver

    def click_product_add_to_cart(self):
        self.click(self.PRODUCT_ADD_TO_CART)

    def click_product_added_successfully_close(self):
        wait_for_clickable(self.driver,self.CART_ADDED_CLOSE,25)
        self.click(self.CART_ADDED_CLOSE)
