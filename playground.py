
class Page:
    def click(self):
        print("Clicking...")

    def find_element(self):
        print("Searching...")

    def verify_text(self):
        print("Testing for text...")


class LoginPage(Page):
    def login(self):
        print('login')

class SignUpPage(Page):
    def signup(self):
        print('registering...')
