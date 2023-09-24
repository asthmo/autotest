from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By

import time
import os
import requests

class SbisElementsLocators:
    LOCATOR_CONTACTS_LINK = (By.LINK_TEXT, 'Контакты')
    LOCATOR_TENSOR_BANNER = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/div/div/div[2]/div/a')
    LOCATOR_REGION = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
    LOCATOR_PARTNERS = (By.CLASS_NAME, 'controls-ListViewV__itemsContainer')
    LOCATOR_CHOICE_REGION = (By.CLASS_NAME, 'sbis_ru-Region-Panel__list')
    LOCATOR_KAMCHATKA = (By.XPATH, '//*[.="41 Камчатский край"]')
    LOCATOR_DOWNLOAD_SBIS_PAGE = (By.XPATH, '//a[.="Скачать СБИС"]')
    LOCATOR_TAB_SBIS_PLUGIN = (By.CLASS_NAME, 'controls-tabButton__overlay')
    LOCATOR_DOWNLOAD_LINK = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')

class SbisActionHelper(BasePage):

    def check_region(self):
        return True if SbisElementsLocators.LOCATOR_REGION else False
           
    def check_partners(self):
        return True if SbisElementsLocators.LOCATOR_PARTNERS else False    
    
    
    def swap_region(self):
        self.find_element(SbisElementsLocators.LOCATOR_KAMCHATKA).click()

    def check_swap_region(self):
        counter = [True if 'Камчат' in self.driver.title else False, 
                   True if '41-kamchatskij-kraj' in self.driver.current_url else False,
                   True if 'Камчат' in self.find_element(SbisElementsLocators.LOCATOR_REGION).text else False,
                   True if 'Камчат' in self.find_element(SbisElementsLocators.LOCATOR_PARTNERS).text else False
                   ]
        
        return True if counter.count(True) == len(counter) else False
    
    def download_plugin(self):
        
        save_path = f"web_installer.exe"
        converter = 1024

        download_tab = self.find_elements(SbisElementsLocators.LOCATOR_TAB_SBIS_PLUGIN)[1]
        download_tab.click()
        download_link_element = self.find_element(SbisElementsLocators.LOCATOR_DOWNLOAD_LINK)
        info_file_size = download_link_element.text
        file_size = float(info_file_size.split('(')[1].split(' ')[1])
        download_link = download_link_element.get_attribute('href')

        download_file = requests.get(download_link)
        with open(save_path, 'wb') as f:
            f.write(download_file.content)

        return int(os.stat(save_path)[6] / converter) == int(file_size * converter)