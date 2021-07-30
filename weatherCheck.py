#Peter Bates
#CIS 245 Assignment 7.1 - Virtual Garage

def main():
	#This is the main function, takes input and gets weather
	menuSelection = ''
	print("Welcome, let's check the weather")
	menuSelection = mainMenu(menuSelection)
	while menuSelection != 'exit':
		menuSelection = inputCheck(menuSelection)
		getWeather(menuSelection)

		menuSelection = mainMenu(menuSelection)
		
def mainMenu(menuSelect):
	#Initial selection to see if things want to exit
	if menuSelect != 'exit':
		menuSelect = input('Please enter a zip code or city. To exit, type "exit": ')
	return menuSelect

def inputCheck(menuChoice):
	#we want to see if their input is blank, and continue reprompt until filled
	while menuChoice == '':
		menuChoice = input('\nPlease enter a zip code, city, or type "exit": ')

	#first check for call to exit before anything else
	if(menuChoice.lower() == 'exit'):
		menuChoice = 'exit'
	elif(menuChoice != ''):
		try:
			int(menuChoice)
			print("Number")
		except ValueError:
			print("Noooope")
		print("good pass")
		print(menuChoice)

	return menuChoice

def getWeather(location):
	#This will call using location to get weather information to pass back
	pass

main()
#just call the main