# Libraries

- [The Python Standard Library Library](#python-standard-library)
- [Importing modules](#importing-modules)
- [3rd-party libraries](#third-party-libraries)
- [Installing and using 3rd-party libraries](#installing-and-using-libraries)
- [Further reading](#further-reading)

## Overview

> "Laziness: The quality that makes you go to great effort to reduce overall energy expenditure. It makes you write labor-saving programs that other people will find useful and document what you wrote so you don't have to answer so many questions about it." ~ [Larry Wall](http://threevirtues.com/), creator of Perl

Programmers make a virtue of laziness. They routinely go out of their way to simplify complex tasks and automate mundane, repetitive work. They avoid [reinventing wheels](https://en.wikipedia.org/wiki/Reinventing_the_wheel).

One way programmers accomplish the above is by writing reusable libraries, or packages, of code. Below we'll explore two avenues for making use of libraries.

## Python Standard Library

Python itself ships with a large [standard library](https://docs.python.org/3/library/index.html) that helps with myriad programming tasks. These include:

* [Downloading remote files](https://docs.python.org/3/library/urllib.request.html)
* Working with [local files and directories](https://docs.python.org/3/library/os.html)
* Reading and writing a range of data formats such as [CSV](https://docs.python.org/3/library/csv.html), [JSON](https://docs.python.org/3/library/json.html) and [XML](https://docs.python.org/3/library/xml.etree.elementtree.html)
* Working with [dates and times](https://docs.python.org/3/library/datetime.html)
* [Pattern matching](https://docs.python.org/3/library/re.html) in text

The list goes on and on...Pythonistas like to say that the language comes with "batteries included."

### Importing modules

Making use of the standard library simply requires you to import a given library or [module](https://www.w3schools.com/python/python_modules.asp) (the latter is the technical way to refer to a library in Python).

You can import and use modules inside a python script or the interactive interpreter.

Let's give it a try. Open a Python interactive interpreter to follow along (type `python` or `ipython` if the latter is installed).

Below we show how to import the [json module](https://docs.python.org/3/library/json.html) to convert a Python dictionary to [JSON](https://www.w3schools.com/js/js_json_intro.asp), a common data format used in web programming.

```
>>> place = {'state': 'CA', 'city': 'Palo Alto'}
>>> import json
>>> json.dumps(place)
'{"state": "CA", "city": "Palo Alto"}'
```

Alternatively, you could directly import the [dumps function](https://docs.python.org/3/library/json.html#json.dumps) using the `from [module] import [name]` syntax.

```
>>> from json import dumps
>>> place = {'state': 'CA', 'city': 'Palo Alto'}
>>> dumps(place)
'{"state": "CA", "city": "Palo Alto"}'
```

For more details on importing modules, check out:

* [W3C Python Modules](https://www.w3schools.com/python/python_modules.asp)
* *Importing Modules* section of [Chapter 2](https://automatetheboringstuff.com/2e/chapter2/) in *Automate the Boring Stuff*

## Third-party libraries

As a Python programmer, you also have access to more than 200,000 libraries built by third-party developers through the [Python Package Index](https://pypi.org/). Many of these libraries supplement the standard library, while some improve upon libraries already built into the langauge. The quality and usefulness varies, but in a number of areas, "best of breed" libraries have emerged that are frequently used by journalists. They include libraries for:

* [Downloading files](https://2.python-requests.org/en/master/) from the web and working with APIs
* [Scraping web sites](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Analyzing](https://pandas.pydata.org/) and [visualizing data](https://matplotlib.org/)
* Using [computer vision](https://opencv.org/)
* Working with [geospatial data](http://geopandas.org/)
* [Machine learning](https://scikit-learn.org/stable/index.html)

If you can think of a task, Python most likely has a library for it. 

### Installing and using libraries

Unlike the standard library, you must first install a third-party library before you can import and use it in your code.

Standard package management tools such as [pip](https://pip.pypa.io/en/stable/) and [pipenv](https://pipenv.readthedocs.io/en/latest/) can be used to install third-party libraries. In this course, we generally use `pipenv` to install libraries into "virtual environments" that allow us to isolate software dependencies for each project.

For example, to install the [requests][] library into `awesome-project`: 

[requests]: https://2.python-requests.org/en/master/

```
cd /path/to/awesome-project
pipenv install requests
```

Once installed in the virtual environment, you can import and use modules in the same way as described [above](#importing-modules). 
**Just don't forget to activate the virtual environment before running a script or the interactive interpreter!!**

```
cd /path/to/awesome-project
# Activate the virtual environment
pipenv shell

# Open an interactive Python interpeter
python
```

Now you should be inside the interactive Python interpreter, where you can import and use the requests module.

```
>>> import requests
>>> response = requests.get('http://example.com/')
```

See [here](remote_files.md) for more details on using [requests][].

## Further reading

**Importing and using modules**

* *Importing Modules* section of [Chapter 2](https://automatetheboringstuff.com/2e/chapter2/) in *Automate the Boring Stuff*
* [Hitchhiker's Guide to Python - Modules](https://docs.python-guide.org/writing/structure/#modules) - a bit technical, but solid overview of modules and good habits when importing code
* [The import system](https://docs.python.org/3/reference/import.html) contains the gory details on importing modules

**Python Standard Library**

* [A Brief Tour of the Python Standard Library](https://docs.python.org/3.8/tutorial/stdlib.html) - a gentler introduction to a wide range of useful tools in the standard library
* [The Python Standard Library](https://docs.python.org/3/library/index.html) - full index of everything in the standard library





