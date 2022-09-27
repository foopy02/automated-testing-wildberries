from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from pathlib import Path
import time
from .parent_page import Page

PARENT_DIR  = Path(__file__).resolve().parent

class DetailPage(Page):
    # cart_classname = "goods__item goods-card j-product-item"
    HTTP_URL = "https://www.wildberries.ru/catalog/17575454/detail.aspx?targetUrl=EX"

    btn_block_classname = "product-page__aside"
    main_btn_classname = "btn-main"
    after_clicked_a_classname = "btn-base j-go-to-basket"

    modal_window_classname = "action-notification show"
    amount_of_items_cart_classname = "navbar-pc__notify"
    
    def __init__(self) -> None:
        self.create_driver()
        self.driver.get(self.HTTP_URL)

    def add_to_cart(self):
        self.wait_for_presence(By.CLASS_NAME, self.btn_block_classname)
        btn_block = self.driver.find_element(By.CLASS_NAME, self.btn_block_classname)
        to_cart_btn = btn_block.find_element(By.CLASS_NAME, "btn-main")
        to_cart_btn.click()
        time.sleep(0.5)
        
        after_added_btn = btn_block.find_element(By.TAG_NAME, "a").get_attribute("class")

        self.wait_for_presence(By.CLASS_NAME, self.amount_of_items_cart_classname)
        cart_amount_of_items = self.driver.find_element(By.CLASS_NAME, self.amount_of_items_cart_classname )
        
        #Check if there amount of items in cart incremented
        assert cart_amount_of_items.text == "1", "Amount of items in cart didn't increment"

        #Check if after clicking button changed the text of it
        assert after_added_btn == self.after_clicked_a_classname, "Button didn't change the text"

