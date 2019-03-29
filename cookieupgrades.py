from threading import Thread
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class CookieUpgrades:
	def __init__(self, driver, wait):
		self.driver = driver
		self.wait = wait
		self.running = False

	def start(self):
		if not self.running:
			self.t1 = Thread(target=self.cookie_upgrade)
			self.t1.start()

	def cookie_upgrade(self):
		self.running = True
		selector = '.crate.upgrade.enabled'
		try:
			self.driver.find_element_by_css_selector(selector).click()
		except:
			pass
			#print("boo")
		time.sleep(1)
		self.running = False