# I am setting try for finally.
# you can add exceptions to handle errors in the code

try:
	# import phonenumbers module for geocoder and carrier
	import phonenumbers
	# print welcome to user
	print("Welcome to phonecrash")
	# giving warning to user about the country code
	print("Enter the phonenumber with country code")

	# input of number for the output
	number=input("Enter your number: ")

	#using geocoder we will find the country
	from phonenumbers import geocoder
	ch_number = phonenumbers.parse(number, "CH")
	print(geocoder.description_for_number(ch_number, "en"))

	# using carrier we will find the service card
	from phonenumbers import carrier
	service_number = phonenumbers.parse(number, "RO")
	print(carrier.name_for_number(service_number, "en"))

# printing thanks to user for using code.
finally:
	print("Thanks for using phonecrash")