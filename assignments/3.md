# Assignment 3 - Strings and Awesome animals

## Python strings reading and practice

Read the [W3 strings section](https://www.w3schools.com/python/python_strings.asp) and work through the [exercises](https://www.w3schools.com/python/exercise.asp?filename=exercise_strings1).

## Awesome animals exercise

> NOTE: For this assignment, you are **not** allowed to use built-in modules such as `csv` or third-party libraries such as `pandas`.

This coding assignment will require you to apply the skills we've learned in the course of our earlier Python readings and the following tutorials:

* [Counting and filtering](../docs/python/count_filter.md)
* [Reading and writing files](../docs/python/file_io.md)

It will also require you to learn on your own about a few features of working with Python strings (see below for more details).

To complete the coding exercise, read and follow the instructions below:

* On the command line, use [DataKit](../docs/datakit.md) to create a new project called `comm-177p-assignment-3`. Remember, all you should need is  `datakit project create` if your system is set up correctly. **Points will be deducted if the project is not named correctly!**
* Create a python script called `filter_awesome_animals.py` in the project's `scripts/` folder.
* Inside the script, read the data from [animal_ratings.csv](https://raw.githubusercontent.com/stanfordjournalism/stanford-progj-2020/master/data/animal_ratings.csv). You do **not** have to programmatically fetch this data in the script since we haven't covered how to do this yet. Instead, manually download a copy of the file and save it alongside the `filter_awesome_animals.py` in the `scripts/` directory.
* In the script, filter the data to create a new list of animals who have "awesomeness" ratings of 5 or above.
* Write the filtered list of animals to a new file called `awesome_animals.csv`. The new file should contain the exact same data columns and header row (`animal`, `awesomeness`) as the original file. The new file will differ only in the number of rows (it should have fewer).
* At the end of the script, have it print the following line: `There are X awesome animals.`, replacing the `X` value with the count of filtered animals. The `X` must be dynamically generated and inserted into the text using [string formatting](https://www.w3schools.com/python/python_string_formatting.asp). In other words, do not hard-code the value into the string.

Lastly, you can run this script on the command line:

```
python filter_awesome_animals.py
```

### Hints

In order to perform this work, you'll need to apply some string manipulation skills:

* [Splitting strings](https://www.w3schools.com/python/ref_string_split.asp)
* [Converting strings to integers](https://realpython.com/convert-python-string-to-int/#converting-a-python-string-to-an-int)

### Submitting

Save and push your code to GitHub and submit the URL to your project in Canvas.