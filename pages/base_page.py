from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import *

from utilities.waits import *

class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
        self.actions=ActionChains(driver)

    def open(self, url):
        self.driver.get(url)
        wait_for_page_load(self.driver)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url


#element actions
    def click(self, locator):
        element = wait_for_clickable(self.driver, locator)
        element.click()

    def send_keys(self, locator, text, clear=True):
        element = wait_for_visibility(self.driver, locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = wait_for_visibility(self.driver, locator)
        return element.text.strip()

    def is_visible(self, locator):
        try:
            wait_for_visibility(self.driver, locator, timeout=5)
            return True
        except Exception:
            return False


#Action chains or Mouse actions
    def hover(self, locator):
        element = wait_for_visibility(self.driver, locator)
        self.actions.move_to_element(element).perform()

#Dropdown
    def select_by_text(self, locator, text):
        element = wait_for_presence(self.driver, locator)
        Select(element).select_by_visible_text(text)

    def press_key(self, key):
        self.actions.send_keys(key).perform()


#Scrolling & JavaScript
    def scroll_to_element(self, locator):
        element = wait_for_presence(self.driver, locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", element
        )

    def scroll_to_bottom(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )


#Browser navigations
    def refresh(self):
        self.driver.refresh()
        wait_for_page_load(self.driver)

    def go_back(self):
        self.driver.back()
        wait_for_page_load(self.driver)

    def go_forward(self):
        self.driver.forward()
        wait_for_page_load(self.driver)


#Frames
    def switch_to_frame(self, locator):
        frame = wait_for_presence(self.driver, locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_window(self, index=0):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[index])


#Alerts
    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

