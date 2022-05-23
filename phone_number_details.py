import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Ingresa número telefónico con el código de país: ")
mobileNo = phonenumbers.parse(mobileNo)

# Get timezone a phone number
print(timezone.time_zones_for_number(mobileNo))

# Get carrier of a phone number
print(carrier.name_for_number(mobileNo, "en"))

# Get region information
print(geocoder.description_for_number(mobileNo, "en"))

# Validating phone number
print("Número válido: ", phonenumbers.is_valid_number(mobileNo))

# Check posibility of number
print("Check posibility of number:", phonenumbers.is_possible_number(mobileNo))
