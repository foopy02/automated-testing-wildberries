from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import time
#Importing from parent dir
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import settings

PARENT_DIR  = Path(__file__).resolve().parent

class Page:
    CHROME_DRIVER_PATH = f"{PARENT_DIR}/chromedriver.exe"
    FIREFOX_DRIVER_PATH = f"{PARENT_DIR}/geckodriver.exe"

    def create_driver(self):
        match settings.BROWSER:
            case "chrome":
                options = webdriver.ChromeOptions()
                options.add_experimental_option("detach", False)
                self.driver = webdriver.Chrome(options=options, executable_path=self.CHROME_DRIVER_PATH)
            case "chrome_headless":
                options = webdriver.ChromeOptions()
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')  # Last I checked this was necessary.
                options.add_experimental_option("detach", False)
                self.driver = webdriver.Chrome(options=options, executable_path=self.CHROME_DRIVER_PATH)
            case "firefox":
                self.driver = webdriver.Firefox(executable_path=self.FIREFOX_DRIVER_PATH)
        self.driver.maximize_window()
    

    def wait_for_presence(self, by: By, value: str) -> None:
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((by, value)))


    def close_driver(self):
        time.sleep(settings.SLEEP_TIME_BEFORE_QUIT)
        self.driver.close()
        