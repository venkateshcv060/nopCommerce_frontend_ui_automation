from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_LINK=(By.CSS_SELECTOR,".ico-login")
    REGISTER_BUTTON=(By.CSS_SELECTOR,".button-1.register-button")
    EMAIL_FIELD=(By.ID,"Email")
    PASSWORD_FIELD=(By.ID,"Password")
    LOGIN_BUTTON=(By.CSS_SELECTOR,".button-1.login-button")


    def click_login(self):
        self.click(self.LOGIN_LINK)

    def enter_login_email(self, email):
        self.send_keys(self.EMAIL_FIELD, email)

    def enter_login_password(self,password):
        self.send_keys(self.PASSWORD_FIELD,password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def user_login(self,login_email,login_password):
        self.click_login()
        self.enter_login_email(login_email)
        self.enter_login_password(login_password)
        self.click_login_button()


