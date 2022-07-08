from selene import command, have
from selene.core.entity import Element


class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def select_from_list(self, /, *, option: str):
        self.browser.all('option').element_by(have.exact_text(option)).click()

    def input(self, /, *, option: str):
        self.element.perform(command.js.set_value(option)).click()
