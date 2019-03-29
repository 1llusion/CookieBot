from threading import Thread
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import re
import time
import random

class CookieMaker:
	def __init__(self, driver, wait):
		self.driver = driver
		self.wait = wait
		self.running = False
		self.optimal_running = False
		#First is name of the maker, second is how efficient he is
		self.optimal_maker = {
							'product': 'product0',
							'ratio': 60 #The cps, don't set too low
							  }
		#self.title_number = 0 #How many cookies we have

		self.cps = {
		'product0': 1,
		'product1': 100,
		'product2': 138,
		'product3': 255,
		'product4': 500,
		'product5': 1000,
		'product6': 2564,
		'product7': 7500,
		'product8': 19615,
		'product9': 46875,
		'product10': 100000,
		'product11': 215385,
		'product12': 395348,
		'product13': 724137,
		'product14': 1238095,
		'product15': 2066666,
		}

		self.names = {
		'product0': 'Cursor',
		'product1': 'Grandma',
		'product2': 'Farm',
		'product3': 'Mine',
		'product4': 'Factory',
		'product5': 'Bank',
		'product6': 'Temple',
		'product7': 'Wizard Tower',
		'product8': 'Shipment',
		'product9': 'Alchemy Lab',
		'product10': 'Portal',
		'product11': 'Time Machine',
		'product12': 'Antimatter Condenser',
		'product13': 'Prism',
		'product14': 'Chancemaker',
		'product15': 'Fractal Engine',
		}

	def start(self):
		if not self.running:
			self.t1 = Thread(target=self.cookie_maker)
			self.t1.start()

	def cookie_maker(self):
		self.running = True
		#self.cookie_upgrade()
		optimal = self.find_optimal()
		selector = '.product.unlocked.enabled#' + optimal
		try:
			#self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector))).click()
			self.driver.find_element_by_css_selector(selector).click()
			print("Cookie maker hired!")
			self.print_cps()
		except Exception as e:
			self.running = False
			#print(str(e))
			return False
		finally:
			self.running = False

	def find_optimal(self):
		self.optimal_running = True
		title = self.driver.title.split(" ")
		#self.title_number = float(title[0].replace(',', ''))
		elements = self.driver.find_elements_by_css_selector('.product.unlocked.enabled')

		for x in range(0,len(elements)):
			if elements[x].is_displayed():

				price = elements[x].find_element_by_class_name('price').text
				price_number = self.get_number(price.replace(',', ''))
				price_number = float(price_number)

				#Extracting the integer and word value
				price_text = self.get_text(price)
				#Changing text to numbers
				if price_text:
					price_number *= price_text

				product = elements[x].get_attribute("id")
				try:
					hover = ActionChains(self.driver).move_to_element(elements[x])
					hover.perform()
					tooltip = self.driver.find_element_by_id('tooltip')
					element = tooltip.find_element_by_class_name('data')
					cps = self.get_number(element.text.replace(',', ''))
					self.cps[product] = price_number / cps
				except Exception as e:
					last_element = elements[len(elements) - 1].get_attribute("id")
					self.cps[last_element] += 0.0001
					rng = random.randint(1,101)
					if rng == 42:
						self.print_cps(True)
					if rng == 10 or rng == 90:
						self.print_cps()
					#print(str(e))

		time.sleep(0.1)
		self.optimal_running = False
		return self.get_cps()

	def get_number(self, text):
		regex = r'(\d+.\d+|\d+)'
		number = re.search(regex, text).group()
		if number:
			return float(number)
		else:
			#Just so that we never divide by 0
			print("Error in getting a number")
			return False

	def get_text(self, text):
		text = re.search(r'[^(\d+.\d+|\d+,) ]+', text)
		if text:
			return_val = text.group()
			return_val = self.word_to_number(return_val)
		else:
			return_val = 1
		return return_val

	def get_cps(self):
		return min(self.cps, key=self.cps.get)

	def print_cps(self, full = False):
		low_cps_product = min(self.cps, key=self.cps.get)
		print("Waiting for: " + self.names[low_cps_product])
		print("With its lowest cps value: " + str(self.cps[low_cps_product]))

		if full:
			print("All CPS:")
			print("---")
			for key, value in self.cps.items():
				print(self.names[key] + " -> " + str(value))
			print("---")

	def word_to_number(self, word):
		index = [
		'million','billion','trillion','quadrillion','quintillion','sextillion','septillion','octillion','nonillion','decillion','undecillion','duodecillion','tredecillion','quardecillion',
		'quindecillion','sexdecillion','septdecillion','octdecillion','nondecillion','vigintillion','unvigintillion','duovigintillion','trevintigillion','quarvintigillion','quinvintigillion',
		'sexvintigillion','septvintigillion','octvintigillion','nonvintigillion','undecivintigillion','duodecivintigillion','tredecivintigillion','quardecivintigillion','quindecivintigillion',
		'sexdecivigintillion','septdecivigintillion','octdecivigintillion','nondecivigintillion','trigintillion','untrigintillion','duotrigintillion','tretrigintillion','quartrigintillion',
		'quintrigintillion','sextrigintillion','septrigintillion','octrigintillion','nontrigintillion','decitrigintillion','undecitrigintillion','duodecitrigintillion','tredecitrigintillion',
		'quardecitrigintillion','quindecitrigintillion','sexdecitrigintillion','septdecitrigintillion','octdecitrigintillion','nondecitrigintillion','vigintitrigintillion','unvigintitrigintillion',
		'duovigintitrigintillion','trevigintitrigintillion','quarvigintitrigintillion','quinvigintitrigintillion','sexvigintitrigintillion','septvigintitrigintillion','octvigintitrigintillion',
		'nonviginitrigintillion','decivigintitrigintillion','undecivigintitrigintillion','duodecivigintitrigintillion',
		].index(word)

		if word == 'million':
			return 1000000
		return 1000 * ((index+1)**1000)

		#Taken from - https://pastebin.com/zBwkvY1j