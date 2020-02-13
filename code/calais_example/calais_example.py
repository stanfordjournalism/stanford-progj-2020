"""
Example Python script showing how to call the
OpenCalais Intelligent Tagging API.

See readme.md alongside this script for more details.
"""
import os
import json
import requests


CALAIS_URL = 'https://api-eit.refinitiv.com/permid/calais'
# BELOW VARIABLE MUST BE SET IN ~/.bash_profile
API_KEY = os.environ['OPENCALAIS_API_KEY']

EXAMPLE_TEXT= """
    Smiths Medical is recalling the sterile saline and sterile water products for inhalation due to the potential exposure to infectious agents (bacillus infantis and staphylococcus epidermidis) because of damage to the containers used to package the finished products. Use of these products in patients could result in infection and may require treatment with antibiotics. Serious or untreated infections could result in patient death.

The company initiated a voluntary recall on September 5, 2017. That recall covered several products, including some that are outside the scope of this notice. The FDA is auditing the recall to ensure the company has notified all affected customers and that affected product has been returned. Based on the available information, the FDA is now classifying the action regarding the affected products (listed below) as a Class I recall.
"""

def main():
    headers = {
        'X-AG-Access-Token' : API_KEY,
        'Content-Type' : 'text/raw',
        'outputformat' : 'application/json',
        'x-calais-selectiveTags': 'company,industry,socialtags'
    }
    # Construst a POST request, as required by the OpenCalais API
    response = requests.post(
        CALAIS_URL,
        data=EXAMPLE_TEXT,
        headers=headers,
        timeout=80
    )
    outfile = '/tmp/recall_example.json'
    with open(outfile,'w') as out:
        if response.status_code == 200:
            print("Writing response to {}".format(outfile))
            json.dump(response.json(), out, indent=4)

if __name__ == '__main__':
    main()
