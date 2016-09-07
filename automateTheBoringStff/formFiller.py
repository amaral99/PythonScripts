#! /usr/bin/python3
# formFiller.py - auto fills forms

import pyautogui, time

# set from computers' coordinates.

nameField = (388, 391)
submitButton = (449, 901)
submitButtonColor = (75, 141, 249)
submitAnotherLink = (566, 299)

formData = [{'name': 'Alice', 'fear': 'eavesDroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'}, {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'}, {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'}, {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphod the law.'},]

pyautogui.PAUSE = 0.5

for person in formData:
	# TODO: give the user a chance to kill the script.
	print('>>> 5 SECOND PAUSE TO LET USER PRES CTRL-C <<<')
	time.sleep(5)

# TODO: Wait until the form page has loaded.
	while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
		time.sleep(0.5)

	print('Entering %s info...' % (person['name']))
	pyautogui.click(nameField[0], nameField[1])

# TODO: fill out the Name Field.
	pyautogui.typewrite(person['name'] + '\t')

# TODO: Fill out the Greatest Fear(s)field.
	pyautogui.typewrite(person['fear'] + '\t')

# TODO: Fill out the Source of Wizard Powers field.
	if person['source'] == 'wand':
		pyautogui.typewrite(['down', '\t'])
	elif person['source'] == 'amulet':
		pyautogui.typewrite(['down', 'down', '\t'])
	elif person['source'] == 'crystal ball':
		pyautogui.typewrite(['down', 'down', 'down', '\t'])
	elif person['source'] == 'money':
		pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])

# TODO: fill out the RoboCop field.
	if person['robocop'] == 1:
		pyautogui.typewrite([' ', '\t'])
	elif person['robocop'] == 2:
		pyautogui.typewrite(['right', '\t'])
	elif person['robocop'] == 3:
		pyautogui.typewrite(['right', 'right', '\t'])
	elif person['robocop'] == 4:
		pyautogui.typewrite(['right', 'right', 'right', '\t'])
	elif person['robocop'] == 5:
		pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])


# TODO: Fill out the Additional Comments field.
	pyautogui.typewrite(person['comments'] + '\t')

# TODO: Click Submit.
	pyautogui.press('enter')

# TODO: wait until form page has loaded.
	print('Clicked Submit.')
	time.sleep(5)

# TODO: Click the Submit another response link.
	pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
