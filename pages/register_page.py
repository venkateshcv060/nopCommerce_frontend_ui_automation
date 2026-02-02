from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import *

from utilities.waits import wait_for_presence


class RegisterPage(BasePage):
    REGISTER_BTN=(By.XPATH,"//a[normalize-space()='Register']")
    GENDER_MALE=(By.ID,"gender-male")
    GENDER_FEMALE=(By.ID,"gender-female")
    FIRST_NAME=(By.ID,"FirstName")
    LAST_NAME=(By.ID,"LastName")
    EMAIL=(By.ID,"Email")
    COMPANY_NAME=(By.ID,"Company")
    NEWSLETTER_CHECKBOX=(By.ID,"NewsLetterSubscriptions_0__IsActive")
    PASSWORD=(By.ID,"Password")
    CONFIRM_PASSWORD=(By.ID,"ConfirmPassword")
    REGISTER_BUTTON=(By.ID,"register-button")
    SUCCESS_MESSAGE=(By.XPATH,"//div[@class='result']")
    ERROR_MESSAGES = (By.XPATH, "//span[contains(@class,'field-validation-error')]")
    CONTINUE_BUTTON=(By.CSS_SELECTOR,"a.register-continue-button")
    EMAIL_ERROR_TEXT=(By.ID,"Email-error") #Wrong email or Please enter a valid email address.
    CONFIRM_PASSWORD_ERROR=(By.ID,"ConfirmPassword-error")#The password and confirmation password do not match. or Password is required.

    def __init__(self,driver):
        # super().__init__(driver)
        self.driver=driver
        # self.wait=WebDriverWait(driver,10)

    def get_title(self):
        self.wait.until(EC.title_contains("Home"))
        return self.driver.title

    def select_gender(self, gender="male"):
        if gender.lower() == "male":
            self.click(self.GENDER_MALE)
        else:
            self.click(self.GENDER_FEMALE)

    def enter_first_name(self, first_name):
        self.send_keys(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.send_keys(self.LAST_NAME, last_name)

    def enter_email(self, email):
        self.send_keys(self.EMAIL, email)

    def enter_company_name(self, company):
        self.send_keys(self.COMPANY_NAME, company)

    def newsletter_checkbox(self, subscribe=True):
        checkbox = wait_for_presence(self.driver, self.NEWSLETTER_CHECKBOX)
        if checkbox.is_selected() != subscribe:
            checkbox.click()

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    def enter_confirm_password(self, password):
        self.send_keys(self.CONFIRM_PASSWORD, password)

    def click_register(self):
        self.click(self.REGISTER_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_error_messages(self):
        elements = self.driver.find_elements(*self.ERROR_MESSAGES)
        return [e.text for e in elements]

    def get_email_error_text(self):
        return self.get_text(self.EMAIL_ERROR_TEXT)

    def get_confirm_password_error_text(self):
        return self.get_text(self.CONFIRM_PASSWORD_ERROR)


    def register_user(self, user_input):
        self.select_gender(user_input["gender"])
        self.enter_first_name(user_input["first_name"])
        self.enter_last_name(user_input["last_name"])
        self.enter_email(user_input["email"])
        self.enter_company_name(user_input["company"])
        self.newsletter_checkbox(user_input["newsletter"])
        self.enter_password(user_input["password"])
        self.enter_confirm_password(user_input["password"])
        self.click_register()




