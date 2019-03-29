import contextlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from cookiemaker import CookieMaker
from cookieupgrades import CookieUpgrades
from goldencookie import GoldenCookie



options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('log-level=3')
driver = webdriver.Chrome(chrome_options=options)
wait = ui.WebDriverWait(driver,30)

driver.get("http://orteil.dashnet.org/cookieclicker/")

wait.until(EC.invisibility_of_element_located((By.ID, 'loader')))
element = driver.find_element_by_id('bigCookie')

make_cookies = CookieMaker(driver, wait)
make_upgrades = CookieUpgrades(driver, wait)
click_golden = GoldenCookie(driver, wait)

time.sleep(10)
while 1:
	try:
		click_golden.start()
		make_upgrades.start()
		make_cookies.start()
		element.click()
	except:
		pass

	time.sleep(0.01)

print(driver.title)
driver.close()