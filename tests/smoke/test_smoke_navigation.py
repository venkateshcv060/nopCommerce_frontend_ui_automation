import time

import pytest
from pages.base_page import BasePage
from utilities.logger import get_logger
from utilities.read_config import Read_Config


@pytest.mark.usefixtures("setup")
class Test_Navigation:
    logger=get_logger()

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_computers_category_opens(self,):
        self.logger.info(f"started test_computers_category_opens ")
        url=Read_Config.get_base_url()+"computers"
        base=BasePage(self.driver)
        base.open(url)
        assert "computers" in base.get_current_url()
        self.logger.info(f"Computers category is successfully opened")

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_electronics_category_opens(self,):
        self.logger.info(f"started test_electronics_category_opens ")
        url = Read_Config.get_base_url() + "electronics"
        base = BasePage(self.driver)
        base.open(url)
        assert "electronics" in base.get_current_url()
        self.logger.info(f"Electronics category is successfully opened")

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_apparels_category_opens(self):
        self.logger.info(f"started test_apparels_category_opens ")
        url = Read_Config.get_base_url() + "apparel"
        base = BasePage(self.driver)
        base.open(url)
        assert "apparel" in base.get_current_url()
        self.logger.info(f"Apparels category is successfully opened")













