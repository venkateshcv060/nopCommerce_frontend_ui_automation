from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import *
from utilities.waits import *

class HomePage(BasePage):
    REGISTER_BUTTON=(By.XPATH,"//a[normalize-space()='Register']")
    ADD_TO_CART_BUTTON=(By.XPATH,"(//button[@class='button-2 product-box-add-to-cart-button'])[2]")
    SHOPPING_CART_BUTTON = (By.ID, "topcartlink")
    LOGOUT_BUTTON=(By.CSS_SELECTOR,".ico-logout")
    SEARCH_FIELD=(By.ID,"small-searchterms")
    SEARCH_BUTTON=(By.CSS_SELECTOR,".button-1.search-box-button")

    def __init__(self,driver):
        # super().__init__(driver)
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def get_title(self):
        self.wait.until(EC.title_contains("Home"))
        return self.driver.title

    def click_register(self):
        # self.hover(self.REGISTER_BTN)
        self.click(self.REGISTER_BUTTON)

    def click_add_to_cart(self):
        # self.hover(self.ADD_TO_CART_BUTTON)
        self.click(self.ADD_TO_CART_BUTTON)

    def click_shopping_cart(self):
        # wait_for_clickable(self.driver,self.SHOPPING_CART_BUTTON,30)
        self.click(self.SHOPPING_CART_BUTTON)

    def click_logout(self):
        self.click(self.LOGOUT_BUTTON)

    def type_search_field(self, search_word):
        self.send_keys(self.SEARCH_FIELD,search_word)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    def search_product(self,product):
        self.type_search_field(product)
        self.click_search_button()







