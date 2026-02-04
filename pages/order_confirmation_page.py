from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderConfirmation(BasePage):
    THANK_YOU_MSG=(By.XPATH,"//h1[normalize-space()='Thank you']")
    ORDER_SUCCESS_MSG=(By.XPATH,"//h2[normalize-space()='Your order has been successfully processed!']")
    ORDER_DETAILS_LINK=(By.XPATH,"//a[normalize-space()='Click here for order details.'])")
    ORDER_CONFIRMATION_CONTINUE=(By.CSS_SELECTOR,".button-1.order-completed-continue-button")
    # ORDER_SUCCESS_MSG=(By.CSS_SELECTOR,".section.order-completed")

    def __init__(self,driver):
        self.driver=driver

    def get_order_success_msg(self):
        self.scroll_to_element(self.THANK_YOU_MSG)
        return self.get_text(self.THANK_YOU_MSG)



