import pytest
from VolvoProject.Pages.LoginPage import LoginPage
from VolvoProject.Tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_verify_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login("anushabalan16@gmail.com","India@2024")

