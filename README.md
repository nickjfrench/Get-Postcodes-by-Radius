# Get Postcodes by Radius
Python script using the ZipCodeBase API to get postcodes within a radius.
My use case only needed up to 100km grouped into 25km, 50km, and 100km lists.
Although, this should act as a good template/demo if you wish to expand.

## API Documentation
ZipCodeBase was the API used to get postcodes within a radius.
View their documentation here: https://app.zipcodebase.com/documentation#radius 
You'll need an API Key to use this script. Within the function, update the key string with your API Key.

## To Use
To use the script, at the end of the document change the parameters for `postcodes_in_100km_radius(3000)` to your specified starting postcode, and country code (if not Australia).
Country code must be a 2 letter code from https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
** You'll need to also replace your API Key within the function. **

Then call the python file. For example, `python postcodes_by_radius.py`
