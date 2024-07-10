# importing modules

from geopy.geocoders import Nominatim

# calling the nominatim tool

geoLoc = Nominatim(user_agent="GetLoc")

# passing the coordinates

locname = geoLoc.reverse("26.7674446, 81.109758")

# printing the address/location name

print(locname)