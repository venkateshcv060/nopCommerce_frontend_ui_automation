from datetime import datetime

# import allure
import pytest
import pytest_html
import os
# from allure_commons.types import AttachmentType

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.read_config import Read_Config

def pytest_addoption(parser):
    parser.addoption("--browser",default='chrome')

@pytest.fixture(autouse=True,scope='class')
def browser(request):
    return request.config.getoption("--browser").lower()

@pytest.fixture(autouse=True,scope='class')
def setup(browser,request):
    global driver
    if browser=='chrome' or browser==None:
        ops=ChromeOptions()
        ops.add_argument("--disable-notifications")
        # ops.add_argument("--headless=new")
        # ops.add_argument("--incognito")
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=ops)
    elif browser=='firefox':
        ops=FirefoxOptions()
        ops.add_argument("--disable-notifications")
        # ops.add_argument("--headless=new")
        driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=ops)
    elif browser=='edge':
        driver=webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else :
        print("enter valid browser name")

    driver.maximize_window()
    driver.get(Read_Config.get_base_url())
    request.cls.driver=driver

    yield
    driver.quit()








# @pytest.hookimpl(hookwrapper=True,tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     setattr(item,"rep_"+report.when,report)
#
#     if report.when == "call" and report.failed:
#         # Try to get driver from class
#         driver = getattr(item._request.node.cls, "driver", None)
#
#         if driver:
#             screenshots_dir = os.path.join(os.getcwd(), "screenshots")
#             os.makedirs(screenshots_dir, exist_ok=True)
#
#             test_name = report.nodeid.replace("::", "_").replace("/", "_")
#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#             file_name = f"{test_name}_{timestamp}.png"
#             filepath = os.path.join(screenshots_dir, file_name)
#
#             driver.save_screenshot(filepath)
#             print(f"\nScreenshot saved at: {filepath}")
#
#             return report
#
#
#
#
# @pytest.fixture(autouse=True)
# def log_on_failure(request):
#     yield
#     driver = getattr(request.cls, "driver", None)
#     if driver:
#         # Attach on failure
#         if request.node.rep_call.failed:
#             allure.attach(driver.get_screenshot_as_png(),
#                           name=f"Failed Test Screenshot - {request.node.name}",
#                           attachment_type=AttachmentType.PNG)