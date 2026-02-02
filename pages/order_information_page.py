from selenium.webdriver.common.by import By

class OrderInfo:
    PRINT_ORDER_INFO=(By.CSS_SELECTOR,".button-2.print-order-button")
    PDF_INVOICE=(By.CSS_SELECTOR,".button-2.pdf-invoice-button")
    CANCEL_ORDER=(By.ID,"cancel_order")
    RE_ORDER=(By.CSS_SELECTOR,".button-1.re-order-button")

    def __init__(self,driver):
        self.driver=driver

