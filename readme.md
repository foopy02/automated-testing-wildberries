# Automated Testing On Selenium
This project has 2 testcases for [Wildberries](https://www.wildberries.ru/) to check main functionality:
* **TC001** - Verify that quick view works
* **TC002** - Verify that add to cart of any elements works

Tried to use **POM** (_Page Object Model_).
# Installation
```
pip install -r requirements.txt
```
# Launch of test
To test **TC001**
```
pytest test_detail_page.py
```
***
To test **TC002**
```
pytest test_main_page.py
```