# CSVs in Python

- [Overview](#overview)
- [Reading CSVs](#reading-csvs)
  - [csv.reader](#reader)
  - [csv.DictReader](#dictreader)
- [Writing CSVs](#writing-csvs)
  - [csv.writer](#writer)
  - [csv.DictWriter](#dictwriter)

## Overview

Files containing comma-separated values, more commonly known as CSVs, are among the most common and easy-to-work with data formats. Government agencies and other data sources often publish data in the CSV format, so it's important to learn how to work with such files.

Fortunately, the [Python Standard Library](https://docs.python.org/3/library/index.html) provides a built-in [csv module][] that makes it much easier to work with CSV files. The CSV module frees coders from having to perform low-level, tedious chores such as handling newline characters and splitting files on commas and other delimiter types. It also helps in more tricky scenarios, such as CSVs in which columns are separated by commas *and* field values also contain commas.

[csv module]: https://docs.python.org/3.8/library/csv.html

The [csv module][] works in tandem with the built-in `open` function that is typically used when [reading and writing files](file_io.md). It can simply be [imported and used](libraries.md) in Python scripts and the interactive interpreter without any extra installation steps.

Below, we demo the `csv` module in the Python interactive interpreter. To follow along:

* Open an interactive shell using `python` or `ipython` (if the latter is installed)
* Download the [animal_ratings.csv][], which contains the data below:

```
animal,awesomeness
cat,5
cougar,10
dog,8
snake,2
narwhal,11
```

[animal_ratings.csv]: https://raw.githubusercontent.com/stanfordjournalism/stanford-progj-2020/master/data/animal_ratings.csv

## Reading CSVs

### Reader

The CSV module provides two primary modes for working with a CSV. The first, [csv.reader][], simply reads data from a CSV and returns the values for each row in a list.

[csv.reader]: https://docs.python.org/3.7/library/csv.html#csv.reader

```
>>> import csv
>>> with open('animal_ratings.csv', 'r') as source_file:
...     reader = csv.reader(source_file)
...     for row in reader:
...         print(row)
...
['animal', 'awesomeness']
['cat', '5']
['cougar', '10']
['dog', '8']
['snake', '2']
['narwhal', '11']
```

A few important notes on the above code:

* [csv.reader][] is passed an open file "handle", as opposed to a file path
* Rows are automatically split on the delimiter (a comma in this case)
* Newline characteres are automatically stripped

Because [csv.reader][] returns rows as lists of values, we must access individual values in each row based on their index position (e.g. `row[0]`). This can be less readable and more brittle from a code perspective. For example, if a government agency changes the structure of a CSV by re-ordering or adding new columns, code that relies on index position will need to be updated.

### DictReader

When working with CSVs, it's often more useful, readable and future-proof to look up field values by column name. The `csv` module provides the [DictReader][] for just this scenario.

[DictReader]: https://docs.python.org/3.7/library/csv.html#csv.DictReader

```
>>> with open('animal_ratings.csv', 'r') as source_file:
...     dict_reader = csv.DictReader(source_file)
...     for row in dict_reader:
...         print(row)
...
OrderedDict([('animal', 'cat'), ('awesomeness', '5')])
OrderedDict([('animal', 'cougar'), ('awesomeness', '10')])
OrderedDict([('animal', 'dog'), ('awesomeness', '8')])
OrderedDict([('animal', 'snake'), ('awesomeness', '2')])
OrderedDict([('animal', 'narwhal'), ('awesomeness', '11')])
```

Some important notes on the above:

* [DictReader][] accepts an open file handle
* It returns an [OrderedDict](https://docs.python.org/3.7/library/collections.html#collections.OrderedDict) for each row. In practice, OrderedDicts work the same as normal dictionaries <sup>[1](#myfootnote1)</sup>.  They support name-based lookups (e.g. `row['animal']`) as well as standard methods such as `keys`, `values` and `items`.

Using [DictReader][] frees us from having to more carefully handle the header row in a file, for example, when counting rows in a file. It also makes our code more readable. It also helps make our code more future-proof in the event that a government agency restructures the CSV.

## Writing CSVs

The `csv` module also provides the ability to easily generate CSV files. Mirroring its read functionality, the module lets you write data rows structured as lists as well as dictionaries.

### Writer

Below is an example showing how to write a truncated version of our data to a new file.

```
>>> animals = [['animal', 'awesomeness'], ['cat', '5'], ['dog', '10']]
>>> with open('animal_shorlist.csv', 'w') as new_file:
...     writer = csv.writer(new_file)
...     for row in animals:
...         writer.writerow(row)
```

A few notes on the above:

* We included the header row as the first item in the `animals` list.
* [csv.writer][] requires an open file rather than a file path
* We used the [writerow](https://docs.python.org/3.7/library/csv.html#csv.csvwriter.writerow) method in a "for" loop, although it's possible to skip the loop entirely and write all rows at once with the [writerows](https://docs.python.org/3.7/library/csv.html#csv.csvwriter.writerows) method.

[csv.writer]: https://docs.python.org/3.7/library/csv.html#writer-objects

The above generates `animals_shortlist.csv` with the below content:

```
animal,awesomeness
cat,5
dog,10
```

### DictWriter

Similar to its counterpart on the reading side, [csv.DictWriter][] can make your code more readable and future-proof by allow you to write rows structured as dictionaries.

[csv.DictWriter]: https://docs.python.org/3.7/library/csv.html#csv.DictWriter

Here's an example:

```
>>> animals = [
... {'animal': 'cat', 'awesomeness': '5'},
... {'animal': 'dog', 'awesomeness': '10'}
... ]
>>> with open('animals_shortlist.csv', 'w') as newfile:
...     col_headers = ['animal', 'awesomeness']
...     dict_writer = csv.DictWriter(newfile, fieldnames=col_headers)
...     dict_writer.writeheader()
...     dict_writer.writerows(animals)

```

[csv.DictWriter][] is largely identical in usage to [csv.writer][], except that we must pass the column headers to the `fieldnames` argument. We also have to call `writerheader` to ensure that the header row is written to the file.


<a name="myfootnote1">1</a>: *The main advantage of OrderedDicts is that they retain the order in which items are inserted (traditional dictionaries prior to Python 3.6 did not guarantee sort order). In Python 3.8, the CSV module switches back to standard dictionaries.*
