Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import phonenumbers
... from phonenumbers import timezone
... from phonenumbers import geocoder
... from phonenumbers import carrier
...  
... number = input("Enter the phone number with country code : ")
...  
... # Parsing String to the Phone number
... phoneNumber = phonenumbers.parse(number)
...  
... # printing the timezone using the timezone module
... timeZone = timezone.time_zones_for_number(phoneNumber)
... print("timezone : "+str(timeZone))
...  
... # printing the geolocation of the given number using the geocoder module
... geolocation = geocoder.description_for_number(phoneNumber,"en")
... print("location : "+geolocation)
...  
... # printing the service provider name using the carrier module
... service = carrier.name_for_number(phoneNumber,"en")
