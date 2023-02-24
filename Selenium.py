import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

kadinproductslocator = "*[href='https://www.lcwaikiki.com/tr-TR/TR/lp/32-33-kadin']"
brownsweatshirtloctaor = "*[href='https://www.lcwaikiki.com/tr-TR/TR/etiket/tunikler-maksimum-199-99-tl-kadin']"
greenshirtlocator = "*[href='/tr-TR/TR/urun/LC-WAIKIKI/kadin/Tunik/5848669/2390611']"
sizelocator = "//*[@id='option-size']//a[text()='XS']"
addtocartloactor = "pd_add_to_cart"
gotocartlocator = "*[href='https://www.lcwaikiki.com/tr-TR/TR/sepetim']"
URL = "https://www.lcwaikiki.com/tr-TR/TR"
headerlocator = "product-list-heading__heading"
urunkodulocator = "//*[text()='Ürün Kodu: ']"
headercartpagelocator = "[class='col-md-12 cart-header mb-20']"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(URL)
assert driver.current_url.__eq__(URL)
time.sleep(2)
Kadinproducts = driver.find_element(By.CSS_SELECTOR, kadinproductslocator)
Kadinproducts.click()
assert driver.current_url.__contains__("kadin")
time.sleep(2)
Brownsweatshirt = driver.find_element(By.CSS_SELECTOR, brownsweatshirtloctaor)
Brownsweatshirt.click()
header = driver.find_element(By.CLASS_NAME, headerlocator)
print(header.text)
assert header.text.__contains__("Tunikler")
time.sleep(2)
greenshirt = driver.find_element(By.CSS_SELECTOR, greenshirtlocator)
greenshirt.click()
urunkodu = driver.find_element(By.XPATH, urunkodulocator)
assert urunkodu.text.__contains__("Ürün")
print(urunkodu.text)
time.sleep(4)
size = driver.find_element(By.XPATH, sizelocator)
size.click()
addtocart = driver.find_element(By.ID, addtocartloactor)
addtocart.click()
gotocart = driver.find_element(By.CSS_SELECTOR, gotocartlocator)
gotocart.click()
time.sleep(2)
headercartpage = driver.find_element(By.CSS_SELECTOR, headercartpagelocator)
print(headercartpage.text)
assert headercartpage.text.__contains__("Sepet")
driver.get(URL)
time.sleep(2)
driver.close()
