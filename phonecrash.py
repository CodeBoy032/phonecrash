try:
	import phonenumbers
	import webbrowser
	print("Welcome to phonecrash")
	print("Enter the phonenumber with country code")
	number=input("Enter your number: ")

	if number==ValueError:
		print("Error")

	from phonenumbers import geocoder
	ch_number = phonenumbers.parse(number, "CH")
	print(geocoder.description_for_number(ch_number, "en"))

	from phonenumbers import carrier
	service_number = phonenumbers.parse(number, "RO")
	print(carrier.name_for_number(service_number, "en"))

except ValueError as e:
	print("enter a valid number!..")

except SyntaxError as e:
	print("Error")

finally:
	print("Thanks for using phonecrash")