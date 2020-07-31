import pytest
import time
from selenium.webdriver.support.ui import Select


class TestExperimentJavascript(object):

    def test_lang_sel(self, browser):
        browser.get('localhost:5000/experiment')
        browser.execute_script('lang_sel("English")')
        time.sleep(1)
        sentence = browser.execute_script('return Inst.sent')
        assert sentence['Language'] == 'English'
        buttons = browser.find_elements_by_class_name('btn-word')
        assert len(buttons) == len(sentence['Words'])
        assert browser.find_element_by_class_name('experiment_content').value_of_css_property('display') == 'grid'
    
    def test_casefold(self, browser):
        assert browser.execute_script('return casefold("hello")') == 'Hello'

    def test_add_sent(self, browser):
        buttons = browser.find_elements_by_class_name('btn-word')
        sentence = browser.find_element_by_id('sentence').text
        for i in range(len(buttons)):
            buttons[i].click()
            present_word = buttons[i].text
            if(i!=0): 
                present_word = ' ' + present_word.lower()
            assert browser.find_element_by_id('sentence').text  == sentence + present_word
            sentence = browser.find_element_by_id('sentence').text

    def test_undo(self, browser):
        sentence = browser.find_element_by_id('sentence').text
        browser.find_element_by_id('undo_btn').click()
        assert browser.find_element_by_id('sentence').text == sentence[:sentence.rfind(" ")]        

    def test_show_all_sent(self, browser):
        browser.execute_script('show_all_sent()')
        assert browser.find_element_by_id('all_sents')

    def test_reset_all(self, browser):
        browser.execute_script('reset_all()')
        try:
            browser.find_element_by_id('all_sents')
        except:
            assert True
        sentence = browser.execute_script('return Inst.sent')        
        assert int(browser.find_element_by_id('var_count').find_element_by_tag_name('dt').text) == len(sentence['Variations'])
    
    def test_check_sent(self, browser):
        browser.get('localhost:5000/experiment')
        browser.execute_script('lang_sel("English")')
        time.sleep(1)
        sentence = browser.execute_script('return Inst.sent')
        var_type = Select(browser.find_element_by_id('sentence_type'))
        for i in sentence['Variations']:
            browser.execute_script('Inst.p_sent = "' + i +'"')
            var_type.select_by_visible_text(sentence['Variations'][i])
            browser.execute_script('check_sent()')
            break
        assert browser.find_element_by_id('sentence_div').value_of_css_property('background-color') == 'rgba(0, 128, 0, 1)'
        assert browser.find_element_by_id('sentence_type').value_of_css_property('background-color') == 'rgba(0, 128, 0, 1)'
        time.sleep(1)
        assert int(browser.find_element_by_id('var_count').find_element_by_tag_name('dt').text) == len(sentence['Variations']) - 1
