from pages.TensorPages import ActionHelper, TensorElementsLocators
from pages.SbisPages import SbisActionHelper, SbisElementsLocators

import time

import allure
@allure.suite('First Test-Case')
def test_first_case(browser):
    sbis_main_page = ActionHelper(browser)
    sbis_main_page.go_to_site()
    time.sleep(3)
    sbis_main_page.find_element(SbisElementsLocators.LOCATOR_CONTACTS_LINK).click()
    time.sleep(3)
    sbis_main_page.find_element(SbisElementsLocators.LOCATOR_TENSOR_BANNER).click()
    sbis_main_page.switch_window()

    with allure.step('Check exist block'):
        assert sbis_main_page.check_block() != None

    time.sleep(3)
    sbis_main_page.find_element(TensorElementsLocators.LOCATOR_ABOUT_LINK).location_once_scrolled_into_view
    sbis_main_page.find_element(TensorElementsLocators.LOCATOR_ABOUT_LINK).click()
    time.sleep(3)

    with allure.step('Check size image collection'):
        assert sbis_main_page.check_size_imgs() == True


@allure.suite('Second Test-Case')
def test_second_case(browser):
    sbis_main_page = SbisActionHelper(browser)
    sbis_main_page.go_to_site()
    time.sleep(3)
    sbis_main_page.find_element(SbisElementsLocators.LOCATOR_CONTACTS_LINK).click()
    time.sleep(3)
    
    with allure.step('Check region and partners'):
        assert sbis_main_page.check_region() == True
        assert sbis_main_page.check_partners() == True

    sbis_main_page.find_element(SbisElementsLocators.LOCATOR_REGION).click()
    time.sleep(3)
    sbis_main_page.swap_region()
    time.sleep(3)

    with allure.step('Check swap region'):
        assert sbis_main_page.check_swap_region() == True


@allure.suite('Third Test-Case')
def test_third_case(browser):
    sbis_main_page = SbisActionHelper(browser)
    sbis_main_page.go_to_site()
    time.sleep(3)
    sbis_main_page.find_element(SbisElementsLocators.LOCATOR_DOWNLOAD_SBIS_PAGE).location_once_scrolled_into_view
    sbis_main_page.find_element(SbisElementsLocators.LOCATOR_DOWNLOAD_SBIS_PAGE).click()
    time.sleep(3)
    with allure.step('Check file size'):
        assert sbis_main_page.download_plugin() == True