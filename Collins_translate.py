import io
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
def main():

	inFile = sys.argv[1]

	print ("Important Note: Please check the usage policy of Collins ENG-HINDI translator")
	time.sleep(2)

	print ("Please wait while we open Mozilla Firefox")
	browser = webdriver.Firefox()
	browser.maximize_window()

	print ("Opening Collins ENG-HINDI translator")
	browser.get ('https://www.collinsdictionary.com/dictionary/english-hindi')

	print ("Reading input file")
	with open(inFile, 'r') as fin:
		for line in fin.readlines():
			for word in line.split():
				send_data = browser.find_element_by_name('q')
				send_data.send_keys(word)

				time.sleep(2)
				search = browser.find_element_by_xpath("//i[@class = 'icon-search icon-fw']")
				search.click()

if __name__ == '__main__':
	main()