
from selene import have
from selene.support.shared import browser

from tests.controls.datepicker import DatePicker
from tests.controls.dropdown import Dropdown
from tests.controls.resourse import resource

from tests.controls.table import Table
from tests.controls.tags_input import TagsInput


def test_submit_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Dan')

    browser.element('#lastName').type('Vu')

    browser.element('#userEmail').type('danvu@ya.ru')

    gender_male = '[for=gender-radio-1]'
    browser.element(gender_male).click()

    browser.element('#userNumber').type('89124356789')

    date_of_birth = DatePicker(browser.element('#dateOfBirthInput'))
    date_of_birth.input(option='30 Jul 1989')

    subjects = TagsInput(browser.element('#subjectsInput'))
    subjects.add('Eng', autocomplete='English')
    subjects.add('Maths')

    hobbies_sports = '[for="hobbies-checkbox-1"]'
    browser.element(hobbies_sports).click()

    browser.element('#uploadPicture').send_keys(resource('w9.jpg'))

    browser.element('#currentAddress').type('DC')

    states = Dropdown(browser.element('#state'))
    states.select(option='Haryana')

    city = Dropdown(browser.element('#city'))
    city.select(option='Karnal')

    browser.element('#submit').click()

    result = Table(browser.element('.modal-content .table'))
    result.cells_of_row(0).should(have.exact_texts('Student Name', 'Dan Vu'))
    result.cells_of_row(1).should(have.exact_texts('Student Email', 'danvu@ya.ru'))
    result.cells_of_row(2).should(have.exact_texts('Gender', 'Male'))
    result.cells_of_row(3).should(have.exact_texts('Mobile', '8912435678'))
    result.cells_of_row(4).should(have.exact_texts('Date of Birth', '30 Jul 1989'))
    result.cells_of_row(5).should(have.exact_texts('Subjects', 'English, Maths'))
    result.cells_of_row(6).should(have.exact_texts('Hobbies', 'Sports'))
    result.cells_of_row(7).should(have.exact_texts('Picture', 'w9.jpg'))
    result.cells_of_row(8).should(have.exact_texts('Address', 'DC'))
    result.cells_of_row(9).should(have.exact_texts('State and City', 'Haryana Karnal'))
