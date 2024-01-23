import time

# from selenium import webdriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import undetected_chromedriver as uc
class InitSpider:

    def __init__(self, url):

        #self.browser = uc.Firefox()
        self.browser = uc.Chrome(headless=True, use_subprocess=False)
        self.wait = WebDriverWait(self.browser, 20)
        self.url = url

    def initSpider(self):

       self.browser.get(self.url)
       username = self.wait.until(
           Ec.element_to_be_clickable((By.ID, 'username'))
       )
       username.send_keys('18962977190')
       password = self.wait.until(
           Ec.element_to_be_clickable((By.ID, 'password'))
       )
       password.send_keys('happiness123')
       submit = self.wait.until(
           Ec.element_to_be_clickable((By.ID, 'btn_login'))
       )
       #time.sleep(1)
       submit.click()
       key = self.wait.until(
           Ec.element_to_be_clickable((By.ID, 'key'))
       )
       key.send_keys('STM32F103C8T6')
       search = self.wait.until(
           Ec.element_to_be_clickable((By.ID, 'btn_topSearch'))
       )
       time.sleep(1)
       search.click()
       time.sleep(3)




if __name__ == "__main__":
    init = InitSpider('https://www.ic.net.cn/search/MC74HC1G14DFT2G.html?page=1')
    init.initSpider()
