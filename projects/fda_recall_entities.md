# FDA Recall Entities

- [Overview](#overview)
- [Setup](#setup)
- [Code details](#code-details)
- [Submitting](#submitting)

## Overview

This project ties together [web scraping](../docs/web_scraping/README.md), an [API service](../docs/api_services.md), and basic data wrangling skills.

It requires creating a multi-step [data pipeline](../docs/python/data_pipelines_with_modules.md) that performs the below steps:

* Scrapes FDA recall announcements
* Performs entity extraction on specific text from each recall announcement using the [OpenCalais/Refinitiv Intelligent Tagging API](https://developers.refinitiv.com/open-permid/intelligent-tagging-restful-api)
* Generates a CSV listing extracted entities

Each of these steps must be encapsulated in [a module that can be executed individually as a script](../docs/python/data_pipelines_with_modules.md#modules-as-scripts).

You must also create a single script that orchestrates all of the steps of the pipeline at once. See below for more details on each script.

## Setup

Create a new [DataKit](../docs/datakit.md) project, choosing `project` when prompted (rather than assignment) and give it a short name of `FDA Recalls`. 

```
cd ~/Desktop/code
datakit project create
```

For this project, you'll need the requests and bs4 libraries.

```
cd comm-177p-project-fda-recalls
pipenv install requests bs4
```

Next, create the following Python modules in your `scripts/` directory.

```
fda.py
opencalais.py
report.py
run_pipeline.py
```

## Code Details

Each of the modules below should be created in a way that allows them to be optionally run as scripts. When they are run as a script, it should trigger the top-level "main" function. You do not need to call the top-level function "main" in each file, and in fact, it can be helpful to give them more meaningful names such as "scrape".

> If you find any of the above confusing, please give the [data pipelines with modules][] tutorial a careful read before proceeding.

### fda.py

`fda.py` should scrape the links to [2020 medical device recall announcements](https://www.fda.gov/medical-devices/medical-device-recalls/2020-medical-device-recalls) and then request and save the raw HTML for each of those "detail" pages to the `data/raw/` directory inside of your project.

The files must be named using the last portion of their URL + the `.html` suffix. For example, this url:

	https://www.fda.gov/medical-devices/medical-device-recalls/ge-healthcare-recalls-carescape-respiratory-modules-due-incorrect-oxygen-values

...should be save here:

	data/raw/ge-healthcare-recalls-carescape-respiratory-modules-due-incorrect-oxygen-values.html

You must use the `DATA_DIR` environment variable to construct the path to the saved files, as detailed in the [portable paths tutorial][].

Lastly, you must include the `if __name__ == '__main__':` strategy in the module to make it executable as a stand-alone script. Again, see [data pipelines with modules][] for details.



### opencalais.py

`opencalais.py` should use [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse and extract the first paragraph in the *"Reason for Recall"* section of each recall page (the HTML downloaded by `fda.py`). 

Once the text is extracted, it should send the paragraph to the OpenCalais API for entity extraction.

For this step, you *must* [obtain an API key](../code/calais_example/README.md#obtain-an-api-key) and then create an environment variable called `OPENCALAIS_API_KEY`. This allows you to avoid hard-coding your key in the script.

> **Here is [example code](../code/calais_example/README.md) demonstrating the above techniques.** Additionally, see [Using Environment Variables to Stash Secrets](../docs/python/using_env_vars_for_secrets.md).

The JSON returned by OpenCalais should be saved in local files alongside the original HTML files. The JSON files should be named identically, except that their file extensions should be changed from `.html` to `.json`. Here is an example:

```
data/raw/distributor-teleflex-recalls-galemed-babiplus-pressure-relief-manifolds-due-dislodged-valve.json
```

You must use the `DATA_DIR` environment variable to construct the path to the saved files, as detailed in the [portable paths tutorial][].


Lastly, you must include the `if __name__ == '__main__':` strategy in the module to make it executable as a stand-alone script. Again, see [data pipelines with modules][] for details.

### report.py

`report.py` should read the JSON files downloaded by `opencalais.py` and generate a CSV called `fda_tags.csv`. This CSV must be saved at the following location in your project:

```
data/processed/fda_tags.csv
```

This CSV should list the "name" of every `socialTag` found in the JSON file, alongside the name of the JSON file where it originated (just the base name of the file, not a partial or full directory path).

Here is the expected header and an example row:

```
entity,source_file
Physical sciences, distributor-teleflex-recalls-galemed-babiplus-pressure-relief-manifolds-due-dislodged-valve.json
```

* `Physical sciences` is extracted from the `name` field of the OpenCalais JSON data
* The file name is simply the name of the local JSON file where the OpenCalais data is stored. 

Here's a snippet showing the relevant portion of the JSON file for a "socialTag" item:

```
    "http://d.opencalais.com/dochash-1/f8724654-39f5-386c-a864-4c449d6e3563/SocialTag/1": {
        "_typeGroup": "socialTag",
        "id": "http://d.opencalais.com/dochash-1/f8724654-39f5-386c-a864-4c449d6e3563/SocialTag/1",
        "socialTag": "http://d.opencalais.com/genericHasher-1/1563dc67-5148-3911-a81d-05553fa900cc",
        "forenduserdisplay": "true",
        "name": "Physical sciences",
        "importance": "1",
        "originalValue": "Physical sciences"
    },
```

Once again, you must use the `DATA_DIR` environment variable to construct the path to the saved file, as detailed in the [portable paths tutorial][].


Lastly, you must include the `if __name__ == '__main__':` strategy in the module to make it executable as a stand-alone script. Again, see [data pipelines with modules][] for details.


### run_pipeline.py

`run_pipeline.py` must import the top-level functions from each of the prior modules and run them inside a `main` function. It must also include the  `if __name__ == '__main__':` strategy.

For example:

```
from fda import download_recall_pages

def main():
    download_recall_pages()
    
if __name__ == '__main__':
    main()
```

This script is intended to trigger, or invoke, all of the functions from the preceding steps. It is the maestro that allows us to easily run a fully automated, multi-step data pipeline.

## Submitting

As always, to complete the assignment, you must:

* Push your code to GitHub
* Submit a link to the GitHub project via Canvas

[portable paths tutorial]: ../docs/python/portable_paths.md#environment-variables-and-pipenv
[data pipelines with modules]: ../docs/python/data_pipelines_with_modules.md