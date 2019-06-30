import io
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def main():

	inFile_hin = sys.argv[1]
	out_file = sys.argv[2]

	print("Opening browser...")
	browser = webdriver.Firefox()
	browser.minimize_window()
	print("Opening link...")
	browser.get('http://preon.iiit.ac.in/babel/multi-gui')
	
	print("Reading input file...")
	with open(inFile_hin,'r') as i:
 		lines = i.readlines()
		data = " ".join(str(x) for x in lines)
		hindi_input=unicode(data,"utf-8")

	print("Sending data to browser...")
	send_hin_inp = browser.find_element_by_name('src')
	send_hin_inp.send_keys(hindi_input)

	select = Select(browser.find_element_by_name('source_lang'))
	select.select_by_visible_text('Hindi')
	
	print("Translating...")
	submitButton = browser.find_element_by_class_name('btn.btn-success.form-submit.btn-block')
	submitButton.click()

	print("Fetching translated data...")
	eng_out = browser.find_element_by_name('tgt').text

	with io.open(out_file, "a", encoding="utf-8") as fout:
		fout.write(eng_out)

	print("Translated data stored in " + out_file)
	fout.close()
	browser.close()


if __name__ == '__main__':
	main()
