#Peter Bates
#CIS 245 Project
#openweathermap api

import requests, json

#openweathermap info:
baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
apiKey = "fa93214eb4f60ad4decef8dc78b38ebf"

def main():
	#This is the main function, takes input and gets weather
	print("Welcome, let's check the weather")
	menuSelection = ''
	menuSelection = mainMenu(menuSelection)
	while menuSelection != 'exit':
		menuSelection = inputCheck(menuSelection)
		while menuSelection == '':
			menuSelection = mainMenu(menuSelection)
			menuSelection = inputCheck(menuSelection)
		if menuSelection != '' and menuSelection != 'exit':
			weather = getWeather(menuSelection)
			displayWeather(weather)
		
		menuSelection = mainMenu(menuSelection)
		
def mainMenu(menuSelect):
	#Initial selection to see if things want to exit
	if menuSelect != 'exit':
		menuSelect = input('\nPlease enter a zip code or city. To exit, type "exit": ')
	return menuSelect

def inputCheck(menuChoice):
	#we want to see if their input is blank, and continue reprompt until filled
	while menuChoice == '':
		menuChoice = input('\nEnter a zip code, city, or "exit": ')

	#first check for call to exit before anything else
	if(menuChoice.lower() == 'exit'):
		menuChoice = 'exit'
		return menuChoice
	elif(menuChoice != ''):
		try:
			int(menuChoice)
		except ValueError:
			url = baseUrl + "appid=" + apiKey + "&q=" + menuChoice
			return url
		else:
			if len(menuChoice) != 5:
				print("Please enter a 5-digit zipcode.")
				url = ''
			else:
				url = baseUrl + "appid=" + apiKey + "&zip=" + menuChoice
			return url

def getWeather(url):
	response = requests.get(url)
	return response.json()

def displayWeather(weather):
	if(weather["cod"] == '404'):
		print ("Sorry, " + weather["message"] + ".")
	else:
		location = weather["name"]
		describeWeather = weather["weather"]
		description = describeWeather[0]["description"]
		temperatures = weather["main"]
	
		temp = temperatures["temp"]
		feelTemp = temperatures["feels_like"]
		#Temp conversion (K − 273.15) × 9/5 + 32 = °F.
		temp = round((((temp - 273.15) * 9) / 5) + 32)
		feelTemp = round((((feelTemp - 273.15) * 9) / 5) + 32)

		currentWeather = "Currently " + location + " has " + description + ". "
		currentWeather += "\nThe temperature is " + str(temp) + "°F, and it feels like " + str(feelTemp) + "°F."

		print(currentWeather)

main()
#just call the main

#Credit:
#https://openweathermap.org/current#list
#https://nineplanets.org/kids/temperature-conversion/