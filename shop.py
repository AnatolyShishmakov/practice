# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# My_Account = driver.find_element_by_link_text("My Account").click()
# username = driver.find_element_by_id("username")
# username.send_keys("qwertyu@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Qwertyuiop123456789!")
# login = driver.find_element_by_css_selector("[name='login']").click()
# shop = driver.find_element_by_id("menu-item-40").click()
# html_5 = driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']").click()
# Book = WebDriverWait(driver, 10).until(
#      EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='product_title entry-title']"), "HTML5 Forms"))



# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# My_Account = driver.find_element_by_link_text("My Account").click()
# username = driver.find_element_by_id("username")
# username.send_keys("qwertyu@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Qwertyuiop123456789!")
# login = driver.find_element_by_css_selector("[name='login']").click()
# shop = driver.find_element_by_id("menu-item-40").click()
# html_btn = driver.find_element_by_css_selector("[class='cat-item cat-item-19']>a").click()
# time.sleep(5)
# item_elements = driver.find_elements_by_css_selector("[class='woocommerce-LoopProduct-link']")
# if len("item_elements")==3:
#     print("три товара")
# else:
#     print("ошибка "+str(len("item_elements")))


# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(10)
# My_Account = driver.find_element_by_link_text("My Account").click()
# username = driver.find_element_by_id("username")
# username.send_keys("qwertyu@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Qwertyuiop123456789!")
# login = driver.find_element_by_css_selector("[name='login']").click()
# shop = driver.find_element_by_id("menu-item-40").click()
# default = driver.find_element_by_name("orderby")
# default_check = default.get_attribute("menu_order")
# if default_check == default_check:
#     print("по умолчанию")
# else:
#     print("ошибка")
# default = driver.find_element_by_name("orderby")
# select = Select(default)
# select.select_by_value("price-desc")
# default = driver.find_element_by_name("orderby")
# default_check = default.get_attribute("price-desc")
# if default_check == default_check:
#     print("Sort by price: high to low")
# else:
#     print("ошибка")



# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# My_Account = driver.find_element_by_link_text("My Account").click()
# username = driver.find_element_by_id("username")
# username.send_keys("qwertyu@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Qwertyuiop123456789!")
# login = driver.find_element_by_css_selector("[name='login']").click()
# shop = driver.find_element_by_id("menu-item-40").click()
# book = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]').click()
# old_price = driver.find_element_by_css_selector('del>[class="woocommerce-Price-amount amount"]')
# old_price_get_text = old_price.text
# old_price_get_text = "600"
# price = driver.find_element_by_css_selector('ins>[class="woocommerce-Price-amount amount"]')
# price_get_text = price.text
# price_get_text = "450"
# prettyPhoto = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='attachment-shop_single size-shop_single wp-post-image']")) )
# prettyPhoto = driver.find_element_by_css_selector('[class="attachment-shop_single size-shop_single wp-post-image"]').click()
# close = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="pp_close"]')) )
# close = driver.find_element_by_css_selector('[class="pp_close"]').click()


# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(10)
# shop = driver.find_element_by_id("menu-item-40").click()
# add = driver.find_element_by_css_selector('[data-product_id="182"]').click()
# basket = driver.find_element_by_css_selector('[class="wpmenucart-contents"]')
# basket_get_text = basket.text
# assert '1' in basket_get_text
# basket2 = driver.find_element_by_css_selector('[class="amount"]')
# basket2_get_text = basket2.text
# assert basket2_get_text=='₹180.00'
# in_basket = driver.find_element_by_css_selector('[class="wpmenucart-contents"]').click()
# subtotal = WebDriverWait(driver, 5).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="cart-subtotal"]'), "180.00"))
# total = WebDriverWait(driver, 5).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="order-total"]'), "183.60"))




# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(10)
# shop = driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 300);")
# add = driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(5)
# add2 = driver.find_element_by_css_selector('[data-product_id="180"]').click()
# in_basket = driver.find_element_by_css_selector('[class="wpmenucart-contents"]').click()
# time.sleep(5)
# delete = driver.find_element_by_css_selector('[data-product_id="180"]').click()
# undo = driver.find_element_by_link_text('Undo?').click()
# clear0 = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]').clear()
# add3 = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# add3.send_keys(3)
# update = driver.find_element_by_css_selector('[value="Update Basket"]').click()
# book = driver.find_element_by_css_selector('[value="3"]')
# book_value = book.get_attribute('value')
# assert book_value=='3'
# time.sleep(5)
# btn = driver.find_element_by_css_selector('[name="apply_coupon"]').click()
# coupon = driver.find_element_by_css_selector('[class="woocommerce-error"]')
# coupon_get_text = coupon.text
# assert coupon_get_text=='Please enter a coupon code.'




# import time
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(10)
# shop = driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 300);")
# add = driver.find_element_by_css_selector('[data-product_id="182"]').click()
# in_basket = driver.find_element_by_css_selector('[class="wpmenucart-contents"]').click()
# proseed = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="checkout-button button alt wc-forward"]')))
# proseed = driver.find_element_by_css_selector('[class="checkout-button button alt wc-forward"]').click()
# first_name = WebDriverWait(driver,10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="billing_first_name"]')))
# first_name = driver.find_element_by_css_selector('[id="billing_first_name"]')
# first_name.send_keys('qwerty')
# last_name = driver.find_element_by_css_selector('[id="billing_last_name"]')
# last_name.send_keys('asdfg')
# email = driver.find_element_by_css_selector('[id="billing_email"]')
# email.send_keys('dfghj@mail.com')
# phone = driver.find_element_by_css_selector('[id="billing_phone"]')
# phone.send_keys(1234567890)
# country = driver.find_element_by_css_selector('[class="select2-container country_to_state country_select"]').click()
# rus = driver.find_element_by_css_selector('[id="s2id_autogen1_search"]')
# rus.send_keys("Russia")
# rus2 = driver.find_element_by_css_selector('[class="select2-result-label"]').click()
# adress = driver.find_element_by_css_selector('[id="billing_address_1"]')
# adress.send_keys('fgjfjfjkgg 1')
# city = driver.find_element_by_css_selector('[id="billing_city"]')
# city.send_keys("Moscov")
# state = driver.find_element_by_css_selector('[id="billing_state"]')
# state.send_keys('jhgkjkjhlkj')
# zip = driver.find_element_by_css_selector('[id="billing_postcode"]')
# zip.send_keys(456754)
# driver.execute_script("window.scrollBy(0, 600);")
# btn = driver.find_element_by_css_selector('[id="payment_method_cheque"]')
# btn.click()
# order = driver.find_element_by_css_selector('[id="place_order"]').click()
# text = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="woocommerce-thankyou-order-received"]'),'Thank you. Your order has been received.'))
# text2 = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="method"]'), 'Check Payments'))















