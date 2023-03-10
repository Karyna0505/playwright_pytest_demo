
from playwright.sync_api import Page, expect


class TextBox:

    def __init__(self, page: Page):

        self.page = page

        self.__full_name = self.page.locator('[id="userName"]')
        self.__email = self.page.locator('[id="userEmail"]')
        self.__current_address = self.page.locator('textarea[id="currentAddress"]')
        self.__permanent_address = self.page.locator('textarea[id="permanentAddress"]')
        self.__submit_btn = self.page.locator('button[id="submit"]')

        self.__output_form = self.page.locator('div[id="output"]')
        self.__output_name = self.page.locator('p[id="name"]')
        self.__output_email = self.page.locator('p[id="email"]')
        self.__output_current_address = self.page.locator('p[id="currentAddress"]')
        self.__output_permanent_address = self.page.locator('p[id="permanentAddress"]')

    def set_username(self, user_name) -> None:

        self.__full_name.fill(user_name)

    def set_email(self, email) -> None:

        self.__email.fill(email)

    def set_current_address(self, address) -> None:

        self.__current_address.type(address)

    def set_permanent_address(self, address) -> None:

        self.__permanent_address.type(address)

    def click_submit_btn(self) -> None:

        self.__submit_btn.click()
        self.__output_form.wait_for(state='visible')

    def check_output_form(self, username, email,current_address, permanent_address) -> None:

        assert self.__output_name.text_content() == f'Name:{username}', \
            f'Expected {username}. got {self.__output_name.text_content()}'

        assert  self.__output_email.text_content() == f'Email:{email}', \
            f'Expected {email}, got {self.__output_email.text_content()}'

        expect(self.__output_current_address).to_have_text(f'Current Address :{current_address}')

        expect(self.__output_permanent_address).to_have_text(f'Permananet Address :{permanent_address}')



