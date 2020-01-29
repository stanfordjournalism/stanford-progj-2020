# Downloading remote files

- [Overview](#overview)
- [Install](#install)
- [Usage](#usage)
- [Further reading](#further-reading)

## Overview

Acquiring files from government agencies and other data sources on the Web is crucial to data journalism. 

The Python language and ecosystem offer numerous libraries for working with remote resources. In this course, we'll focus on [requests][], a third-party library that is a go-to resource because of its ease of use and flexibility. [requests][] can handle a variety of scenarios, from simple downloads of data files to working with authentication-based APIs such as Twitter.

[requests]: https://2.python-requests.org/en/master/

## Install

`requests` can be installed using standard package managers such as [pip](https://pip.pypa.io/en/stable/) and [pipenv](https://pipenv.readthedocs.io/en/latest/). In this course, we generally use `pipenv` to install libraries into "virtual environments" that allow us to isolate software dependencies for each project.

```
# system install
pip install requests

# Or install in a project environment using pipenv
cd ~/Desktop/code/awesome-project
pipenv install requests
```


## Usage

In the below example, we use `requests` to download the [animals.csv][] sample data to a local file.

[animals.csv]: https://raw.githubusercontent.com/stanfordjournalism/stanford-progj-2020/master/data/animals.csv

To follow along, fire up an interactive Python interpeter on the command line by typing `python` or `ipython` (if you've installed it).

```
>>> import requests
>>> url = "https://raw.githubusercontent.com/stanfordjournalism/stanford-progj-2020/master/data/animals.csv"
>>> response = requests.get(url)
>>> response.text
>>> print(response.text)
animal
cat
cougar
dog
snake
narwhal
```

Above, we use `requests.get` to [make a request](https://2.python-requests.org/en/master/user/quickstart/#make-a-request) for the remote file at a GitHub URL. The [contents](https://2.python-requests.org/en/master/user/quickstart/#response-content) of the file are available in the `.text` attribute of the response (from GitHub) to our web request.

From here, you can use standard methods for writing [files](file_io.md#writing-files) or [CSVs](csv.md#writing-csvs) to save the content in a local file.

```
>>> with open('animals.csv', 'w') as local_file:
...     local_file.write(response.text)
...
```

## Further reading

The above is a very basic use case. Check out the [requests][] documentation for details on how to handle a variety of other scenarios.