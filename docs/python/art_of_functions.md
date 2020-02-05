# The Art of Writing Functions

- [Overview and advice](#overview-and-advice)
- [The `main` function](#the-main-function)
- [Exercise](#exercise)
- [Further reading](#further-reading)

## Overview and advice 

```
def do_stuff():
    print("Totally doing stuff")
```

Functions are an invaluable tool that help write readable, reliable and reusable code.

Functions help decompose a problem into more manageable chunks. They help you reason more clearly about the problem at hand.

Naming functions can be hard. Try to be descriptive but concise. The intent of the function should be clear.

And please, PLEASE use snake_case in Python :)

Here are some functions that illustrate good habits:

```
def download_json():
    # code that downloads JSON
    # and saves it to local file
    pass
    
def convert_json(json_file):
    # code that reads JSON file
    # and converts to a CSV
    pass
```

Functions should generally have clear inputs and outputs.

```
def convert_json(json_path):
    # code to read local JSON fle
    # and convert to list
    rows = [
        ['ca', 'san fran'],
        ['ca', 'los angeles']
    ]
    return rows
```

Having a hard time naming a function? It may be doing too much! Try breaking large functions into smaller functions. 

```
### BAD ###

def scrape_and_process_and_load():
    # bunch of code to scrape a website,
    # process the data, and load it
    # into a database.
    pass
	
	
### BETTER ###

def scrape():
    pass
    
def process_data():
    pass
	
def load_database():
    pass
```

This strategy of decomposing large functions mirrors the process of [chopping up a large programming problem](../owl_probs_unix.md#cut-your-problems-down-to-size) into smaller sub-problems. By creating smaller functions devoted to particular tasks, we can more easily reason through our problem in code.



## The main function

It's quite likely you'll end up with code that has a number of functions performing very specific tasks. You may even have functions calling other functions.

Although we encourage using functions, orchestrating them can become a challenge. Even reading code with lots functions can become difficult.

When writing scripts, it's wise to create a "top-level" [entry point](https://en.wikipedia.org/wiki/Entry_point) function that serves as a sort of maestro. Its job is to kick off the script and orchestrate lower-level functions devoted to specific tasks.

Traditionally, this high-level orchestrator is called `main`. It's defined in the same way as other Python functions and is really no different, except in its role.

```
# Below, the main function calls a series of functions
# defined elsewhere
def main():
    download_json()
    transform_json()
    generate_csv()
    
# We call "main" at the end of our script,
# which kicks off all the other functions
main()
```

## Exercise

The code below scrapes and counts the words on a very basic web page.

Spend a few minutes reviewing the code and getting a sense of what it does. 

Then try rewriting the code to use multiple, clearly defined functions. 

It's especially helpful to print out the code and just use pen on paper to group related code into functions and give them clear names.

Along the way, think about what if any inputs and outputs each function should have. For example, does one function return a value that must be passed to another function?

Once you've defined the functions and their interplay, create a script with a [`main`](#the-main-function) function at top that orchestrates the other functions. Remember, the job of `main` is to invoke these functions in the expected manner, handling inputs and outputs as needed. Lastly, don't forget to call `main()` at the end of your script to kick things off.

```
import bs4, requests

url = "http://example.com"
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, "html.parser")
words = []
words.extend(soup.find('h1').text.split())
for paragraph in soup.find_all('p'):
    text = paragraph.text
    para_words = text.replace('.',' ').replace('\n', ' ').split()
    words.extend(para_words)

print("There are {} words on example.com".format(len(words)))
```

## Further reading

* [W3C Python Functions](https://www.w3schools.com/python/python_functions.asp)
* [Chapter 3 - Functions](https://automatetheboringstuff.com/2e/chapter3/) of *Automate the Boring Stuff*.