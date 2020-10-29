# Data Pipelines with Modules

- [Overview](#overview)
- [What is a module?](#what-is-a-module)
- [Creating modules](#creating-modules)
- [Modules as scripts](#modules-as-scripts)
- [Modular data pipelines](#modular-data-pipelines)
- [Conclusion](#conclusion)

## Overview

A Python script that performs any significant number of tasks can easily grow bloated and hard to manage. This often occurs through a process of accretion:

1. Identify a challenge (e.g. scrape a web page)
1. Write some code to solve the problem (write a web scraper)
1. Rinse and repeat steps 1 and 2 for each new problem (transform json to csv, insert csv into a database, analyze data, produce a report, etc.)

Soon you're staring at hundreds or thousands of lines of code that are hard to decipher and debug.

[Functions](art_of_functions.md) are a first line of defense against such complexity. Often, a single script with clearly defined functions will suffice for taming the chaos.

But as projects increase in complexity, other tools must be used to organize code into a clean, understandable structure. Chief among these tools is the Python [module](https://docs.python.org/3.8/tutorial/modules.html).

Below, we'll learn how modules help organize code as part of a data pipeline with multiple, discrete steps. We'll also learn how to orchestrate, or drive, each step in the pipeline using a single script.

## What is a module?
 
A module is simply a text file with Python code and a `.py` extension. 

You've already used plenty of modules in the course of learning Python fundamentals:

```
# Import from built-in Python modules
import csv
from json import dump

# Import third-party libraries
import requests
from bs4 import BeautifulSoup
```

## Creating modules

Similar to built-in and third-party modules, it's possible to create your own modules containing functions, variables and other importable code.

Below is a basic `code.py` module containing a variable and function:

```
NUMBER=10

def api_call():
    print("Write some code to make an API call, why don't ya?")

```

You could then import this code from another file in the same directory, e.g. `do_stuff.py`.

```
from code import NUMBER, api_call

print(NUMBER)
api_call()
```

Modules (and the related concept of [packages](https://docs.python.org/3.8/tutorial/modules.html#packages)) are important for writing well-organized, readable code.
 
For a more thorough introduction to Python modules (and packages), check out [Real Python](https://realpython.com/python-modules-packages/).

## Modules as scripts

So we understand how to create modules and import their code.

We also know how to create [Python scripts](overview.md#python-scripts) that perform a set of actions.

Being a clever bunch, Pythonistas have a strategy for creating modules (with importable code) that can also be [executed as scripts](https://docs.python.org/3.8/tutorial/modules.html#executing-modules-as-scripts). 

Here's what it looks like if we applied the strategy to the `code.py` example from above.

```
NUMBER=10

def api_call():
    print("Write some code to make an API call, why don't ya?")

# Below is the new code
if __name__ == '__main__':
    api_call()
```

Above, the `if __name__ == '__main__'` line is the secret sauce for creating a dual-purpose module. 

The strategy relies on the built-in `__name__` variable to determine if a module has been run as a script or imported by another module.

*The value of `__name__` will vary depending on how the module is being used.* When the file is run as a script (`python code.py`), Python automatically sets the value to the string [`'__main__'`](https://docs.python.org/3/library/__main__.html). In this context, the condition is true and therefore `api_call()` will run.

However, when another module imports `code.py`, the module's own name (minus the `.py` suffix) is set as the value for `__name__`.  In this case, `__name__` will equal  `'code'`. Therefore, the condition will *not* be true and `api_call()` will not run.

Here's a concrete example using a revised version of `do_stuff.py`:

```
# code.__name__ will be the string "code",
# as opposed to "__main__", since code has
# been imported by do_stuff.py
import code
print(code.__name__)
```

## Modular data pipelines

The ability to run modules as scripts helps us [chop big problems down to size](../owl_probs_unix.md#cut-your-problems-down-to-size). It allows us to tackle one problem at a time, and then organize each solution into a single automated pipeline.

Here's a very basic example using three files: `scraper.py`, `converter.py`, and `run_pipeline.py`.

```
# scraper.py
def scrape():
     print("This function downloads pages from a website.")
     
if __name__ == '__main__':
    scrape()
```

```
# converter.py
def convert():
     print("This function extracts structured data from web pages."
     
if __name__ == '__main__':
    convert()

```

```
# run_pipeline.py
# This module imports and runs the "main"
# functions from the other modules, to create
# a single automated pipeline

from scraper import scrape
from converter import convert

def main():
    scrape()
    convert()
    
if __name__ == '__main__':
    main()   
```

With a setup such as above, we're able to individually run `scraper.py` and `converter.py` as scripts.

From a development perspective, it might make sense to first work through the scraper code. This might involve repeatedly running the module as a script as we sort through coding problems:

```
python scraper.py
```

Once the scraper is working and we've downloaded the necessary files, we can move on to `converter.py`, which presumably parses the pages downloaded by the scraper. Now we can simply run the converter without triggering all of the scraping processes:

```
python converter.py
```

By loosening the [coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming)) between these steps, we avoid wasting our own development time and making unnecessary requests to the website. 

Had we combined both of these steps in a single Python script, we would find ourselves running all of the scraper code every time we wanted to test the latest changes or additions to our conversion step.

You can imagine how tedious and costly this will become as a project grows in complexity.

Of course, it's also helpful to create an easy way to run all of the steps in the pipeline. It's quite likely, for example, that a data pipeline such as this would run on an automated schedule. Rather than scheduling numerous individual scripts, it makes sense to create a single script that orchestrates all of the steps. That is precisely the role of `run_pipeline.py`, which imports and executes the top-level functions from `scraper.py` and `converter.py`. 

Remember, due to the `if __name__ == '__main__'` conditional in each of those modules, the top-level functions will *not* be run as a side effect of importing their code. Instead, `run_pipeline.py` imports and executes their functionality.

A few final observations on the above example:

* We've been using the name "main" for our top-level functions in scripts thus far. But as you can see, there's no absolute rule requiring the use of the word "main". Here, we decided to be pragmatic in our naming conventions. We used names such as `scrape` and `convert` as the "main" functions in their respective modules, while using the more traditional `main` in the `run_pipeline.py` script. This way our pipeline script is a bit more readable.
* The above example is obviously simplified. In a real-world scenario, each of these modules would likely contain a number of other "helper" functions that are used by top-level functions such as `scrape` and `convert`.


## Conclusion

As programmer journalists, we're often faced with "expensive" tasks. Such tasks can involve actual fees, such as costs associated with using an API. Often, they involve tasks that cost us time such as a complex web scrape or training a machine learning model. 

Minimizing how often we run such tasks can help save precious time and money.

Modular data pipelines offer a sensible way to address such concerns.
They allow us the flexibility to repeat individual tasks without triggering potentially expensive operations elsewhere in the pipeline.

At the same time, they let us easily orchestrate and drive all steps in a pipeline when necessary.

Lastly, modules allow us to reason more clearly about code. They let us chop big problems down to size by grouping related code. They help us create well-organized programs that other humans can more easily understand, use and debug.
