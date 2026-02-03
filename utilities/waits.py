from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utilities.logger import get_logger

logger=get_logger()
def wait_for_visibility(driver, locator, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    except TimeoutException:
        raise TimeoutException(f"Element not visible: {locator}")


def wait_for_presence(driver, locator, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    except TimeoutException:
        raise TimeoutException(f"Element not present: {locator}")


def wait_for_clickable(driver, locator, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    except TimeoutException:
        raise TimeoutException(f"Element not clickable: {locator}")


def wait_for_invisibility(driver, locator, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    except TimeoutException:
        raise TimeoutException(f"Element still visible: {locator}")


def wait_for_text(driver, locator, expected_text, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.text_to_be_present_in_element(locator, expected_text)
        )
    except TimeoutException:
        raise TimeoutException(
            f"Expected text '{expected_text}' not found in element: {locator}"
        )


def wait_for_url_contains(driver, partial_url, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.url_contains(partial_url)
        )
    except TimeoutException:
        raise TimeoutException(
            f"URL did not contain expected text: {partial_url}"
        )


def wait_for_page_load(driver, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    except TimeoutException:
        raise TimeoutException("Page did not load completely")
