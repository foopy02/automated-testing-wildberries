import os
import sys
#Importing from parent dir
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from pages.detail_page import DetailPage

def test_add_to_cart():
    detail_page = DetailPage()
    detail_page.add_to_cart()
    detail_page.close_driver()
