'''
2. Write a program to determine which country a city belongs to. Given list of
cities per country:
Australia = ["Sydney"
,
"Melbourne"
,
"Brisbane"
,
"Perth"]

UAE = ["Dubai"
,
"Abu Dhabi"
,
"Sharjah"
,
"Ajman"]

India = ["Mumbai"
,
"Bangalore"
,
"Chennai"
,
"Delhi"]

Ask the user to enter a city name and print the corresponding country. Example:
Enter a city name: "Abu Dhabi"
Output: "Abu Dhabi is in UAE"
'''
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ")

if city in Australia:
    print(city, "is in Australia")
elif city in UAE:
    print(city, "is in UAE")
elif city in India:
    print(city, "is in India")
else:
    print("City not found")