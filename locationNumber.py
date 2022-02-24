# pip install phonenumbers
# import parse and geocoder
from phonenumbers import parse, geocoder

number = '+962----------'  # put your number here

print(f'\nthe location of this phone number {number} is: ', end='')

# use description_for_number from geocoder after parse the number to get the location of the number

print(geocoder.description_for_number(parse(number), 'en'))  # you can put the language that you want like en, ar...

