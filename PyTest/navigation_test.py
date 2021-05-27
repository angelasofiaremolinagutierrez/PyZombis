from selenium import webdriver
import pytest

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield #wait until all test are done
    driver.close()
    driver.quit()
    print("Test completed")

def test_navigate_menu(test_setup):
    driver.get('http://localhost:8000/')

    #menu saves each option on the index menu
    menu = driver.find_elements_by_class_name('toctree-l1')

    for option in menu:
        option.click()
        
       
