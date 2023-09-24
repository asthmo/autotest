from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By

class TensorElementsLocators:
    LOCATOR_STRENGTH_IN_PEOPLE_BLOCK = (By.XPATH, '//*[.="Сила в людях"]')
    LOCATOR_ABOUT_LINK = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    LOCATOR_IMG_COLLECTIONS = (By.CLASS_NAME, 'tensor_ru-About__block3-image')

class ActionHelper(BasePage):

    def switch_window(self):
        my_windows = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(my_windows[-1])

    def check_block(self):
        return self.find_element(TensorElementsLocators.LOCATOR_STRENGTH_IN_PEOPLE_BLOCK, time=3)

    def check_size_imgs(self):
        img_collections = self.find_elements(TensorElementsLocators.LOCATOR_IMG_COLLECTIONS, time=2)
        width = img_collections[0].get_attribute('width')
        height = img_collections[0].get_attribute('height')

        counter = [True if img.get_attribute('width') == width and img.get_attribute('height') == height else False for img in img_collections]

        return counter.count(True) == len(img_collections)
    