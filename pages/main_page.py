from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .parent_page import Page

PARENT_DIR  = Path(__file__).resolve().parent

class MainPage(Page):
    HTTP_URL = "https://www.wildberries.ru/catalog/zhenshchinam/odezhda/bluzki-i-rubashki"

    product_classname = "product-card__img"
    title_a_classname = "product__header-wrap"

    def __init__(self) -> None:
        self.create_driver()
        self.driver.get(self.HTTP_URL)


    def open_quick_view(self):
        self.wait_for_presence(By.CLASS_NAME, self.product_classname)
        product = self.driver.find_elements(By.CLASS_NAME, self.product_classname)[0]
        product.click()
    
    def click_to_title(self):
        self.wait_for_presence(By.CLASS_NAME, self.title_a_classname)
        title_href = self.driver.find_element(By.CLASS_NAME, self.title_a_classname).find_element(By.TAG_NAME, "a").get_attribute("href")
        self.driver.get(title_href)
        assert title_href == self.driver.current_url, "URL link from title and redirected url doesn't match"
    
        


