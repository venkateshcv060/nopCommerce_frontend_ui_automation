from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class CheckoutPage(BasePage):
        CHECKOUT_BUTTON=(By.ID,"checkout")
        TERMS_OF_SERVICE_BUTTON=(By.ID,"termsofservice")
        CHECKOUT_AS_GUEST_BUTTON=(By.CSS_SELECTOR,".button-1.checkout-as-guest-button")
        CHECKOUT_REGISTER_BUTTON=(By.CSS_SELECTOR,".button-1.register-button")
        CHECKOUT_USER_EMAIL=(By.ID,"Email")
        CHECKOUT_USER_PASSWORD=(By.ID,"Password")
        CHECKOUT_LOGIN_BUTTON = (By.CSS_SELECTOR, ".button-1.login-button")


        def __init__(self, driver):
            # super().__init__(driver)
          self.driver=driver

        def click_checkout(self):
            self.click(self.CHECKOUT_BUTTON)

        def click_terms_of_service(self):
            self.click(self.TERMS_OF_SERVICE_BUTTON)

        def click_checkout_as_guest(self):
            self.click(self.CHECKOUT_AS_GUEST_BUTTON)

