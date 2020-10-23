from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("http://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 600);")

#Открываем Selenium Ruby и вкладку "REVIEWS"
selenium_book = driver.find_element_by_css_selector("div[id=text-22-sub_row_1-0-2-0-0] h3")
selenium_book.click()
review_tab = driver.find_element_by_css_selector("div.woocommerce-tabs.wc-tabs-wrapper li.reviews_tab")
review_tab.click()

# Ставим оценку 5 звезд
five_stars = driver.find_element_by_css_selector("p.stars a.star-5")
five_stars.click()

# Заполняем поля отзыва
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Dmitry")
email = driver.find_element_by_id("email")
email.send_keys("aaa@aa.a")

# Нажимаем кнопку Submit
submit = driver.find_element_by_id("submit")
submit.click()
