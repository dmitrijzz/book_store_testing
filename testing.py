from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# Функция регистрации на сайте (принимат ссылку на окно, логин и пароль)
def registration(drv, l, p):
    # Нажимаем меню My Account
    btn_my_account = drv.find_element_by_id("menu-item-50")
    btn_my_account.click()

    # Вводим логин и пароль
    email = drv.find_element_by_id("reg_email")
    email.send_keys(l)
    password = drv.find_element_by_id("reg_password")
    password.send_keys(p)

    # Нажимаем кнопку Submit
    btn_submit = drv.find_element_by_css_selector("p.woocomerce-FormRow.form-row input[type='submit']")
    btn_submit.click()

# Функция авторизации на сайте (принимат ссылку на окно, логин и пароль)
def login(drv, l, p):
    # Нажимаем меню My Account
    btn_my_account = drv.find_element_by_id("menu-item-50")
    btn_my_account.click()

    # Вводим логин и пароль
    email = drv.find_element_by_id("username")
    email.send_keys(l)
    password = drv.find_element_by_id("password")
    password.send_keys(p)

    # Нажимаем кнопку Login
    btn_submit = drv.find_element_by_css_selector("input[name='login']")
    btn_submit.click()

    # Проверка что удачно залогинились
    logout_present = WebDriverWait(drv, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li.woocommerce-MyAccount-navigation-link--customer-logout a"), "Logout"))
    if logout_present:
        print ("Залогинились успешно")
    else:
        print ("Процедура регистрации не удалась")

# Функция де-авторизации на сайте (принимат ссылку на окно)
def logout (drv):
    # Нажимаем меню My Account
    btn_my_account = drv.find_element_by_id("menu-item-50")
    btn_my_account.click()

    # Нажимаем кнопку Logout
    logout = drv.find_element_by_css_selector("li.woocommerce-MyAccount-navigation-link--customer-logout a")
    logout.click()

    print ("Разлогинились успешно")
