from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

def registration(drv, l, p):

    btn_my_account = drv.find_element_by_id("menu-item-50")
    btn_my_account.click()

    email = drv.find_element_by_id("reg_email")
    email.send_keys(l)

    password = drv.find_element_by_id("reg_password")
    password.send_keys(p)

    btn_submit = drv.find_element_by_css_selector("p.woocomerce-FormRow.form-row input[type='submit']")
    btn_submit.click()

def login(drv, l, p):
    btn_my_account = drv.find_element_by_id("menu-item-50")
    btn_my_account.click()

    email = drv.find_element_by_id("username")
    email.send_keys(l)

    password = drv.find_element_by_id("password")
    password.send_keys(p)

    btn_submit = drv.find_element_by_css_selector("input[name='login']")
    btn_submit.click()

    logout_present = WebDriverWait(drv, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li.woocommerce-MyAccount-navigation-link--customer-logout a"), "Logout"))
    if logout_present:
        print ("Залогинились успешно")
    else:
        print ("Процедура регистрации не удалась")

def logout (drv):
    btn_my_account = drv.find_element_by_id("menu-item-50")
    btn_my_account.click()

    logout = drv.find_element_by_css_selector("li.woocommerce-MyAccount-navigation-link--customer-logout a")
    logout.click()

    print ("Разлогинились успешно")
