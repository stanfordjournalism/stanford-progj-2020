# Counting and filtering

- [Overview](#overview)
- [Counting](#counting)
- [Filtering](#filtering)
- [Count if](#count-if)

## Overview

In the course of our Python study, we've learned about some of the basic features of the Python programming language. That includes:

  * Basic data types (integers, strings, lists, dicts)
  * Expressions and assignment statements
  * Variables as storage containers
  * Flow control ("for" loops and if/elif/else)
  * Built-in functions such as `len` and `print`

Let's start tying together this knowledge and applying it in practical contexts.

> For these examples, you should fire up an interactive Python interpeter on the command line by typing `python` or `ipython` (if you've installed it).

## Counting

Counting is one of the most basic and important operations we need to perform.

One of the simplest and most common ways to count items involves using the built-in [len](https://docs.python.org/3.5/library/functions.html#len) function to measure the length of an array:

```
animals = ['cat', 'dog', 'bird']
len(animals)
3
```

Another common approach -- one often used when processing data from an external source such as a CSV -- is to use a counter variable. 

```
count = 0
for animal in animals:
	count +=1 # same as writing count = count + 1
print(count)
3
```

Above, we "initialized" a variable called `count`, and then used the [augmentation operator](https://docs.python.org/3.8/reference/simple_stmts.html#augmented-assignment-statements) to increment the count as we loop through the list of animals.

## Filtering

Filtering data based on some aspect of the information is another common data wrangling task.

```
for animal in animals:
    if animal != 'dog':
        print(animal)
cat
bird      
```

## Count if

We can now combine the above techniques to count a filtered list of items. Here are a few different approaches.

```
# Use a simple counter
count = 0
for animal in animals:
    if animal != 'dog':
        count += 1
print(count)
2
```

What if we need to keep the results that we filtered for some reason? For example, say we need both the count *and* the actual data for some additional downstream purpose such as saving it to a new file. In this case, we can adapt our strategy with the help of a list and `len`.


```
# Store the filtered items in a new list
noncanines = []
for animal in animals:
    if animal != 'dog':
        noncanines.append(animal)
        
# Now "count" the filtered list
print(len(noncanines))
2
```

Both of these approaches work, and which one you use will vary based on the end goal.
