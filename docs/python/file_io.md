# Reading Files

Learning how to read and write files is an essential programming task.

Below are some examples intended to demonstrate some basic techniques in an interactive Python shell session.

> Examples below will use the [animals.csv](../data/animals.csv) and [animal_ratings.csv](../data/animal_ratings.csv) files in this repo.

To follow along, open an ipython terminal.

## Opening and closing files

Files are typically read from (or written to) in Python using the built-in [open](https://docs.python.org/3.5/library/functions.html#open) function.

This function allows us to open a file in various modes. 

```
# Open a file in read mode
f1 = open('data.csv', 'r')
f1.close()

# Open a file in append mode
# to add lines to pre-existing content
f2 = open('data.csv', 'a')
f2.close()

# Open a file in write mode
# Additions will overwrite pre-existing content
f3 = open('data.csv', 'w')
f3.close()
```

The `open` function has a few other modes, but the above read, append and write modes are the most useful to learn at the outset.

Note that we made a point of closing all of the files. Failing to close a file can lead to [memory leaks](https://en.wikipedia.org/wiki/Memory_leak) and other unexpected behavor -- e.g when working with files in an interactive Python interpreter, content you're expecting to appear in a file may not yet have been "flushed" to the file.

### The "with" idiom

As you get more familiar with Python, you'll notice the use of the `with` statement to open files. This is a common idiom which ensures that a file is properly closed after the `with` block of code completes execution. 

> Here's some [helpful background](https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/) on why we should always use `with` to open files. 


```
with open('data.csv', 'r') as myfile:
    text = myfile.read()
# At this point, we're outside the "with" block
# and the file has been automatically closed
print(text)
```

This idiom can feel strange at first, but using it can help avoid memory leaks or other code problems.

## Reading data

The simplest way to read data from a file is the `.read` method on an open file [handle](https://en.wikipedia.org/wiki/Handle_(computing)). 

For example, to read data from a locally downloaded version of [animals.csv](../data/animals.csv).

```
with open('data/animals.csv', 'r') as f:
    text = f.read()
print(text)
animal
cat
cougar
dog
snake
narwhal
```

## Read lines from file

When we read data from a file, often the most useful way to access that data is line by line. Unfortunately, the `.read` method mentioned above brings the data in as one large blob of text, leaving us on the hook for spliting that text into separate lines.

It's not a ton of extra work, but why go to the trouble when Python gives us several ways to more quickly process individual rows?

Below is an example using the [readlines](https://www.w3schools.com/python/ref_file_readlines.asp) method on open files.

```
with open('animals.csv', 'r') as f:
    animals = f.readlines()
print(animals)
['animal\n', 'cat\n', 'cougar\n', 'dog\n', 'snake\n', 'narwhal\n']
```

Note above that the items in the list contain a `\n` character. This is a [newline](https://en.wikipedia.org/wiki/Newline), an "invisible" character that is used to indicate the end of a line of text on Mac/Unix systems.

When processing data read from files, we typically want to remove newlines using the [strip method](https://www.w3schools.com/python/ref_string_strip.asp).

```
# Select the second item in the list
animals[1]
'cat\n'

animals[1].strip()
'cat'
```

Stripping newlines helps ensure that programming logic such as name-based matching or filters don't accidentally fail due to the presence of newlines. For example, the below illustrates how newlines might trip you up:

```
# Notice the animal rows have newlines
>>> print(animals)
['animal\n', 'cat\n', 'cougar\n', 'dog\n', 'snake\n', 'narwhal\n']

# We'll create a new list 
# and attempt to store just the cat in the list
>>> filtered_animals = []
>>> for animal in animals:
...     if animal == 'cat':
...         filtered_animals.append(animal)
...

# Note the list is empty; our 
# attempt to match "cat" failed!
>>> print(filtered_animals)
[]

# Let's try again, this time 
# also matching the newline character
>>> for animal in animals:
...     if animal == 'cat\n':
...         filtered_animals.append(animal)
...
...
>>> print(filtered_animals)
['cat\n']

```

## Read lines efficiently

The `readlines` method is handy, but Python provides an even simpler idiom for reading the lines of a file: just step through them using a [for loop](https://www.w3schools.com/python/python_for_loops.asp).

```
with open('animals.csv') as f:
    for line in f:
        print(line.strip())     
animal
cat
cougar
dog
snake
narwhal
```

The above reads each line from the file in a step-wise fashion, one by one. This "streaming" method of data ingestion is particularly handy when dealing with large files. Steppng through the file in a "for loop" avoids consuming excessive memory by reading in all the lines of a file at once, which is what happens when using the `read` or `readlines` methods.


## Writing files

Let's say that we want to create a new file containing a filtered list of animals. Specifically, we just want animals whose names do not start with the letter "c".

We'll need to filter out the `cat` and `cougar`.

```
with open('animals.csv', 'r') as infile:
    animals_filtered = []
    for line in infile:
        animal = line.strip()
        if animal not in ['cat', 'cougar']:
            animals_filtered.append(animal)

print(animals_filtered)
['animal', 'dog', 'snake', 'narwhal']

# Now we can write the filtered list to a new file
with open('animals_filtered.csv', 'w') as outfile:
    for animal in animals_filtered:
        # Note we have to add the newline that we 
        # stripped above
        outfile.write(animal + '\n')
```

It's important to note that above, we actually created an extra bit of work for ourselves by stripping the newlines when we read the source data. When we wrote the filtered data to a new file, we were forced to add the newline to each row. If we had not, the data would have been jumbled into one line: `animaldogsnakenarwhal`.