#!/usr/bin/env python

#### ZipCodeBase Radius PostCode Search ####
#### By Nick French on 2 Nov 2022 ####

import requests
import json


def postcodes_in_100km_radius(starting_postcode=3000, country="au"):
    """ Search for postcodes within 100km of given starting postcode.\n
    Country must be a 2 letter code from https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 \n
    ** Ensure API KEY is set ** """

    # API Key uses ZipCodeBase account. Replace with your key.
    headers = {
        "apikey": "REPLACE_ME"}

    # For details on required parameters. See Radius section at https://app.zipcodebase.com/documentation#radius
    # Radius defaults to using KM. See documentation above.
    params = (
        ("code", starting_postcode),
        ("radius", "100"),
        ("country", country),
    )

    response = requests.get(
        'https://app.zipcodebase.com/api/v1/radius', headers=headers, params=params)

    # Convert Output Text into a Json Object
    jsonOutput = json.loads(response.text)

    # Keep only the post codes grouped by their distance
    results25 = []
    results50 = []
    results100 = []
    for result in jsonOutput["results"]:
        if result['distance'] <= 25.00:
            results25.append(int(result["code"]))
        if result['distance'] > 25.00 and result['distance'] <= 50.00:
            results50.append(int(result["code"]))
        if result['distance'] > 50.00 and result['distance'] <= 100.00:
            results100.append(int(result["code"]))

    # Remove Duplicates. As a dict type can't have duplicate keys.
    results25 = list(dict.fromkeys(results25))
    # Sort list by ascending
    results25.sort()
    results50 = list(dict.fromkeys(results50))
    results50.sort()
    results100 = list(dict.fromkeys(results100))
    results100.sort()

    # Output
    print("Getting all postcodes within " +
          params[1][1] + " km of " + params[0][1])
    print("* Not displaying duplicates")

    print("\n--- Results Under 25km ---")
    print("Total: " + str(len(results25)))
    print(results25)

    print("\n--- Results Above 25km and Under 50km ---")
    print("Total: " + str(len(results50)))
    print(results50)

    print("\n--- Results Above 50km and Under 100km ---")
    print("Total: " + str(len(results100)))
    print(results100)


postcodes_in_100km_radius(3000)
