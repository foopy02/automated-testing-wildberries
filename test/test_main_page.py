import os
import sys
#Importing from parent dir
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from pages.main_page import MainPage

def test_open_quick():
    main_page = MainPage()
    main_page.open_quick_view()
    main_page.click_to_title()
    main_page.close_driver()
