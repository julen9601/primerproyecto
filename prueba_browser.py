from selenium import webdriver
from selenium.webdriver.common.by import By
import config as c


def openbrowser():
    browser= webdriver.Chrome(executable_path=c.path)
    browser.get("https://www.darkorbit.es")
    
    login_form = browser.find_element_by_id('bgcdw_login_form_username')
    password_form = browser.find_element_by_id('bgcdw_login_form_password')
    boton_continuar = browser.find_element_by_xpath("//fieldset[@class='bgcdw_login_form_buttons']/input[1]")
    
    login_form.send_keys(c.usuario)
    password_form.send_keys(c.passwd)
    boton_continuar.click()







