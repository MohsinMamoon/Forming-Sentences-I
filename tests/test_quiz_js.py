import pytest
import time
from selenium.webdriver.support.ui import Select


class TestQuizJavascript(object):

    def test_lang_sel(self, browser):
        browser.get('localhost:5000/quiz')
        browser.execute_script('lang_sel("English")')
        time.sleep(1)
        questions = browser.execute_script('return Questions')
        assert len(questions) != 0
        q_panels = browser.find_elements_by_class_name('panel-heading')
        assert len(q_panels) == len(questions)

    def test_Sub(self, browser):
        questions = browser.execute_script('return Questions')
        for i in questions:
            options = browser.find_elements_by_class_name('q'+str(i['ID']))
            for j in options:
                if j.get_attribute('title') == str(i['answer']):
                    j.click()
                    break
        browser.execute_script('Sub()')
        assert browser.execute_script('return correct') == len(questions)

    def test_reset(self, browser):
        time.sleep(1)
        buttons = browser.find_elements_by_class_name('btn-default')
        for i in buttons:
            if i.text == 'No':
                i.click()
                time.sleep(1)
        browser.find_element_by_class_name('btn-danger').click()
        assert browser.execute_script('return correct') == 0