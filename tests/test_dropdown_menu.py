import pytest

from pages.dropdown_menu_page import DropDownMenu
from utils.test_data import Data


class TestDropdownMenu:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.dropdown = DropDownMenu(self.page)

        self.page.goto('https://demoqa.com/select-menu')

    def test_select_menu(self, test_setup):
        """
        Test to verify all dropdown menus on the page
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.dropdown.select_group1_option1()

        self.dropdown.select_professor()

        self.dropdown.select_old_color()

        self.dropdown.select_multiple_colors(Data.colors)

        self.dropdown.select_cars()