from threading import Thread
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class GoldenCookie:
	def __init__(self, driver, wait):
		self.driver = driver
		self.wait = wait
		self.running = False

	def start(self):
		if not self.running:
			self.t1 = Thread(target=self.golden_cookie)
			self.t1.start()

	def golden_cookie(self):
		self.running = True
		try:
			element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'shimmer')))
			element.click()
			print("Golden cookie clicked")
		except Exception as e:
			self.running = False
			#print(str(e))
			return False
		finally:
			self.running = False