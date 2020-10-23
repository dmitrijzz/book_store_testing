from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from testing import login, logout
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
wait = WebDriverWait(driver, 10)

def product_page():
    driver.execute_script("window.open();")
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    driver.get("http://practice.automationtesting.in/")

    login(driver, "dmitrijzz@gmail.com", "AzzPractic")

    shop = driver.find_element_by_css_selector("li[id='menu-item-40'] a")
    shop.click()

    book_html_forms = driver.find_element_by_css_selector("img[alt='Mastering HTML5 Forms']")
    book_html_forms.click()

    summary_text = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.summary h1"), "HTML5 Forms"))
    if summary_text:
        print ("Заголовок корректный")
    else:
        print ("Заголовок не корректный")

    logout(driver)
    driver.close()
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)

def num_per_cat():
    driver.execute_script("window.open();")
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    driver.get("http://practice.automationtesting.in/")

    login(driver, "dmitrijzz@gmail.com", "AzzPractic")

    shop = driver.find_element_by_css_selector("li[id='menu-item-40'] a")
    shop.click()

    kat_HTML = driver.find_element_by_css_selector("li.cat-item-19 a")
    kat_HTML.click()

    products_count = driver.find_elements_by_css_selector("ul.products li")
    if len(products_count) == 3:
        print("В разделе HTML 3 товара")
    else:
        print("Ошибка. Количество товаров в разделе HTML: " + str(len(products_count)))

    logout(driver)
    driver.close()
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)

def orders():
    driver.execute_script("window.open();")
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    driver.get("http://practice.automationtesting.in/")

    login(driver, "dmitrijzz@gmail.com", "AzzPractic")

    shop = driver.find_element_by_css_selector("li[id='menu-item-40'] a")
    shop.click()

    selected = driver.find_element_by_css_selector("select[name='orderby'] option[selected]")
    selected_value = selected.get_attribute("value")
    if (selected_value=='price-desc'):
        print ('По умолчанию выбрана сортировка от большего к меньшему')
    else:
        print ('По умолчанию выбрана сортировка НЕ от большего к меньшему')
        selector = driver.find_element_by_css_selector("select[name='orderby']")
        select = Select(selector)
        select.select_by_value('price-desc')

        selected = driver.find_element_by_css_selector("select[name='orderby'] option[selected]")
        selected_value = selected.get_attribute("value")
        if (selected_value=='price-desc'):
            print ('После изменения выбрана сортировка от большего к меньшему')

    logout(driver)
    driver.close()
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)

def sales():
    driver.execute_script("window.open();")
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    driver.get("http://practice.automationtesting.in/")

    login(driver, "dmitrijzz@gmail.com", "AzzPractic")

    shop = driver.find_element_by_css_selector("li[id='menu-item-40'] a")
    shop.click()

    android_book = driver.find_element_by_css_selector("img[title='Android Quick Start Guide']")
    android_book.click()

    old_price = driver.find_element_by_css_selector("del>span").text
    if (old_price == "₹600.00"):
        print ("Цена до скидки верная")
    else:
        print ("Цена до скидки не верная и равна:", old_price)

    new_price = driver.find_element_by_css_selector("ins>span").text
    if (new_price == "₹450.00"):
        print ("Цена со скидкой верная")
    else:
        print ("Цена со скидкой не верная и равна:", new_price)

    android_book_preview = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[title='Android Quick Start Guide']")))
    android_book_preview.click()

    btn_preview_close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.pp_close")))
    btn_preview_close.click()

    logout(driver)
    driver.close()
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)

def basket():
    driver.execute_script("window.open();")
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    driver.get("http://practice.automationtesting.in/")

    shop = driver.find_element_by_css_selector("li[id='menu-item-40'] a")
    shop.click()

    basket_HTML = driver.find_element_by_css_selector("a[data-product_id='182']")
    basket_HTML.click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.added_to_cart")))
    basket_count_items = driver.find_element_by_css_selector("a.wpmenucart-contents :nth-child(2)").text
    basket_price = driver.find_element_by_css_selector("a.wpmenucart-contents :nth-child(3)").text

    assert ((basket_count_items == "1 Item") and (basket_price=="₹180.00"))
    print ("Количество товаров и сумма в корзине правильная")

    basket = driver.find_element_by_css_selector("a.wpmenucart-contents")
    basket.click()

    price_subtotal = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.cart-subtotal span.amount"), "₹180.00"))
    if (price_subtotal):
        print ("Subtotal верно отображается в корзине")
    else:
        print ("Subtotal =", driver.find_element_by_css_selector("tr.cart-subtotal span.amount").text )

    driver.close()
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)

def basket_work():
    driver.execute_script("window.open();")
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    driver.get("http://practice.automationtesting.in/")

    shop = driver.find_element_by_css_selector("li[id='menu-item-40'] a")
    shop.click()

    driver.execute_script("window.scrollBy(0, 300);")

    basket_HTML = driver.find_element_by_css_selector("a[data-product_id='182']")
    basket_HTML.click()

    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "a.wpmenucart-contents>span"), "1 Item"))

    JS_HTML = driver.find_element_by_css_selector("a[data-product_id='180']")
    JS_HTML.click()

    basket = driver.find_element_by_css_selector("a.wpmenucart-contents")
    basket.click()

    remove_HTML = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.remove[data-product_id='182']")))
    remove_HTML.click()

    undo = driver.find_element_by_css_selector("div.woocommerce-message>a")
    undo.click()

    quantity = driver.find_element_by_xpath("//tr[.//a[text()='JS Data Structures and Algorithm']]/td/div/input")
    quantity.clear()
    quantity.send_keys(3)

    update = driver.find_element_by_css_selector("td.actions>input.button")
    update.click()

    btn_coupon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='apply_coupon']")))
    print(btn_coupon)

    quantity = driver.find_element_by_xpath("//tr[.//a[text()='JS Data Structures and Algorithm']]/td/div/input")
    selected_quantity =  quantity.get_attribute("value")
    assert selected_quantity == '3'
    print ("Количество товаров в корзине обновилось")

    time.sleep(3)
    btn_coupon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.coupon>input[name='apply_coupon']")))
    btn_coupon.click()

    error_coupon_text = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "ul.woocommerce-error>li"), "Please enter a coupon code."))
    if (error_coupon_text):
        print("Сообщение об отсутсвии купона выводится")
    else:
        print("Сообщение об отсутсвии купона не выводится")

    driver.close()
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)

def bying():
    driver.execute_script("window.open();")
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    driver.get("http://practice.automationtesting.in/")

    shop = driver.find_element_by_css_selector("li[id='menu-item-40'] a")
    shop.click()

    driver.execute_script("window.scrollBy(0, 300);")

    basket_HTML = driver.find_element_by_css_selector("a[data-product_id='182']")
    basket_HTML.click()

    time.sleep(1)
    basket = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a.wpmenucart-contents>i")))
    basket.click()

    processed = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.wc-proceed-to-checkout>a")))
    processed.click()

    name = wait.until(EC.element_to_be_clickable((By.ID,"billing_first_name")))
    name.send_keys("Add")

    last_name = driver.find_element_by_id("billing_last_name")
    last_name.send_keys("Swansen")

    email = driver.find_element_by_id("billing_email")
    email.send_keys("www@ww.w")

    phone = driver.find_element_by_id("billing_phone")
    phone.send_keys("2345674")

    country = driver.find_element_by_id("s2id_billing_country")
    country.click()

    input_country = driver.find_element_by_id("s2id_autogen1_search")
    input_country.send_keys("Ukraine")

    enter_country = driver.find_element_by_id("select2-results-1")
    enter_country.click()

    address = driver.find_element_by_id("billing_address_1")
    address.send_keys("Lenina")

    city = driver.find_element_by_id("billing_city")
    city.send_keys("TownCity")

    state = driver.find_element_by_id("billing_state")
    state.send_keys("state")

    zip = driver.find_element_by_id("billing_postcode")
    zip.send_keys("192345")

    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(3)

    radio_btn = driver.find_element_by_id("payment_method_cheque")
    radio_btn.click()

    place = driver.find_element_by_id("place_order")
    place.click()

    thank_you_text = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
    if thank_you_text:
        print ("Заказ принят. Текст 'Thank you' присутствует ")
    else:
        print("Заказ не принят.")

    payment_method = wait.until(EC.text_to_be_present_in_element((By.XPATH, "//tr[.//th[text()='Payment Method:']]/td"), "Check Payments"))
    if payment_method:
        print ("Метод оплаты 'Check Payments'")
    else:
        print("Метод оплаты не 'Check Payments'")

    driver.close()
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)


product_page()
num_per_cat()
orders()
sales()
basket()
basket_work()
bying()

driver.quit()
