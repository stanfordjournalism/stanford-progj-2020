# Working with APIs

- [Overview](#overview)
- [Leveling up on an API](#leveling-up-on-an-api)
- [Trump Organization example](#trump-organization-example)
- [Trump Entities exercise](#trump-entities-exercise)

## Overview

Working with [APIs](../apis_and_the_news.md) can be tricky. They typically require some form of authentication (e.g. an API key) and provide numerous URL-based resources -- commonly called [endpoints][] -- for different types of data.

[endpoints]:https://en.wikipedia.org/wiki/Web_API#Endpoints

The [OpenCorporates API](https://api.opencorporates.com/), which provides data on companies registered all over the world, is a good example. 

Its [company search endpoint](https://api.opencorporates.com/documentation/API-Reference#get-companies/search) returns a list of companies:

> https://api.opencorporates.com/v0.4/companies/search?q=trump+organization

Whereas the [company detail endpoint](https://api.opencorporates.com/documentation/API-Reference#get-companies/:jurisdiction_code/:company_number) provides a bit more information on each entity such as officers and number of employees:

> https://api.opencorporates.com/companies/us_ny/694908

Below, we'll work through an example using OpenCorporates data to get familiar with the process of using APIs. OpenCorporates is a great service and provides data free for public journalism projects. If you plan to use their data for a private or commercial project, please make sure you obey the terms of their [license](https://opencorporates.com/legal/licence).


## Leveling up on an API

Before we can start using an API, we typically have to spend some time getting acquainted with its offerings and requirements. 

Below are some strategies for leveling up on an API:

* Read the docs thoroughly.
* Identify API [endpoints][] of interest (i.e. ones that address the story or topic you're exploring).
* API providers sometimes offer example API calls that you can try in a browser. Other providers even offer an interactive console in the browser for experimenting. Try kicking the tires by customizing example API calls.
* JSON and XML data can be brutal to read. Use a Web browser (or [browser plugin](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en)) that formats the data for readability and lets you expand/collapse nested data.
* Experiment in the interactive Python shell. Make an API call to fetch some data. Then [introspect](https://en.wikipedia.org/wiki/Type_introspection) the data using the [type function][] and [list](https://docs.python.org/3.8/tutorial/datastructures.html#more-on-lists) and [dictionary](https://docs.python.org/3.8/tutorial/datastructures.html#dictionaries) methods such as `.keys()`.
* Look for Python “[client](https://github.com/datamade/census)” libraries that ease use of the API.

[type function]: https://www.w3schools.com/python/ref_func_type.asp

## Trump Organization example

Let's try out some of the techniques mentioned above using OpenCorporates data on [The Trump Organization, Inc.](https://opencorporates.com/companies/us_ny/694908).

> Note, you must install `requests` before running the below code.

First let's grab the data. Note that below, we use the `response.json()` method to automatically transform the JSON string to a Python data structure. The `requests` library provides this as a handy feature because it's so often used to request JSON. Farther down, we'll also see how to use Python's built-in [json library][] to write data to a file. 

[json library]: https://docs.python.org/3/library/json.html

```
>>> import requests
>>> url = "https://api.opencorporates.com/companies/us_ny/694908"
>>> response = requests.get(url)
>>> data = response.json()
```

Now let's poke around the data to get a sense of its structure. We'll use the [type function][] to determine if a given layer of this nested data structure is a list or dictionary (these are the typical data structures used in JSON to organize data).

That information will give us a sense of what types of Python functionality are available to us. For example, a list will require grabbing items by index; a dictionary will require looking up items using keys.

```
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['api_version', 'results'])

# Let's poke around the 'results'
>>> type(data['results'])
<class 'dict'>

# Yet another dictionary, but with only 
# a single key so our path forward is clear.
>>> data['results'].keys()
dict_keys(['company'])

# Now we're in business
>>> type(data['results']['company'])
<class 'dict'>
>>> data['results']['company'].keys()
```

So we clearly have to dig down a ways through some nested dictionaries before arriving at our target data. Here's a sample of what that data looks like. Note we've cleaned up the output using the `pprint` function.

```
>>> from pprint import pprint
>>> pprint(data['results']['company'])
{'agent_address': None,
 'agent_name': None,
 'alternate_registration_entities': [],
 'alternative_names': [],
 'branch': None,
 'branch_status': None,
 'company_number': '694908',
 'company_type': 'DOMESTIC BUSINESS CORPORATION',
 'controlling_entity': None,
 'corporate_groupings': [{'corporate_grouping': {'name': 'Donald Trump',
                                                 'opencorporates_url': 'https://opencorporates.com/corporate_groupings/Donald+Trump',
                                                 'updated_at': '2020-02-03T12:46:41+00:00',
                                                 'wikipedia_id': 'Donald_Trump'}},
```

Note that above, the `corporate_groupings` key is a list of dictionaries. We'd access these using list index lookups (or simply by looping through them).

```
>>> pprint(data['results']['company']['corporate_groupings'][0])
{'corporate_grouping': {'name': 'Donald Trump',
                        'opencorporates_url': 'https://opencorporates.com/corporate_groupings/Donald+Trump',
                        'updated_at': '2020-02-03T12:46:41+00:00',
                        'wikipedia_id': 'Donald_Trump'}}
```

Finally, let's say we wanted to save all this data to a local file. We can easily do this using the [json library][].

```
# Import json library and use "indent=4" to 
# nicely format the output
>>> import json
>>> with open('trump_org_inc.json', 'w') as outfile:
...     json.dump(data, outfile, indent=4)
...    
```

## Trump entities exercise

Now it's your turn to give it a try. Let's say we want to generate a CSV containing a list of all the corporate entities associated with Donald Trump. OpenCorporates provides a [CorporateGroupings endpoint](https://api.opencorporates.com/documentation/API-Reference#get-corporate_groupings/:name) that lets us do just that.

Here is the endpoint you'll need.

> https://api.opencorporates.com/v0.4/corporate_groupings/Donald+Trump

Try writing the code to:

* Request the data
* Transform the returned JSON from a string to native Python data structures
* Save the JSON to a local file called `trump_entities.json`. Make sure the data is nicely formatted using `indent=4`
* Generate a CSV called `trump_entities.csv` that contains the below fields. You'll need to dig these out of the `membership` dictionary inside of each item inside of `memberships`):
  * `name`
  * `jurisdiction_code`
  * `company_number`
  * `opencorporates_url`