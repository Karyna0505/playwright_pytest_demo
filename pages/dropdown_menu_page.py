import random

from playwright.sync_api import Page


class DropDownMenu:

    def __init__(self, page: Page):

        self.page = page

        self.__select_value_dropdown = self.page.locator('[id="withOptGroup"]')
        self.__group_1_option_1 = self.page.locator('//div[text()="Group 1, option 1"]')
        self.__select_one_dropdown = self.page.locator('[id="selectOne"]')
        self.__prof = self.page.locator('//div[text()="Prof."]')
        self.__old_style_select_menu_dropdown = self.page.locator('select[id="oldSelectMenu"]')
        self.__multiselect_dropdown = self.page.locator('(//div[contains(@class,"control")])[3]')
        self.__volvo = self.page.locator('option[value="volvo"]')
        self.__audi = self.page.locator('option[value="audi"]')

    def select_group1_option1(self) -> None:
        self.__select_value_dropdown.click()
        self.__group_1_option_1.click()

    def select_professor(self) -> None:
        self.__select_one_dropdown.click()
        self.__prof.click()

    def select_old_color(self) -> None:
        option = str(random.randint(1, 10))
        self.__old_style_select_menu_dropdown.select_option(option)

    def select_multiple_colors(self, colors) -> None:
        self.__multiselect_dropdown.click()
        for color in colors:
            option = self.page.locator(f'//div[text()="{color}"]')
            option.click()

    def select_cars(self) -> None:
        self.__volvo.drag_to(self.__audi)
