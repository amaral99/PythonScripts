#import requests, os, bs4

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('html')

i = 1
while i < 100:
	up = htmlElem.send_keys(Keys.UP)
	down = htmlElem.send_keys(Keys.DOWN)
	left = htmlElem.send_keys(Keys.LEFT)
	right = htmlElem.send_keys(Keys.RIGHT)



#soup = bs4.BeautifulSoup([], 'html5lib')

# click on new game
#newGame = soup.select('.restart-button')
#if newGame == []:
#	print('Could not find new game')

