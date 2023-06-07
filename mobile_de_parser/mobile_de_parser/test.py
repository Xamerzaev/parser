from selectorlib import Extractor
import requests

url = 'https://suchen.mobile.de/fahrzeuge/search.html?damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&makeModelVariant1.makeId=25200&makeModelVariant1.modelId=19&maxFirstRegistrationDate=2022-12-31&maxMileage=150000&minFirstRegistrationDate=2000-01-01&minMileage=50000&ref=srpHead&scopeId=C&sortOption.sortBy=searchNetGrossPrice&sortOption.sortOrder=ASCENDING&refId=dc84461f-f220-8c1c-ef1d-6858662f830b'

response = requests.get(url)
html_content = response.text

extractor = Extractor.from_html(html_content)

# Define your CSS selectors here to extract the desired data
# For example:
make = extractor.css('span[title="Make"]').text

print(make)
