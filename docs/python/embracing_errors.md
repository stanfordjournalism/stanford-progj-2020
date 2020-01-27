# Embracing errors

> *Failure is the best teacher in life.* ~ Everybody who has learned anything.

Mistakes and code go hand in hand. It's just a fact of life. Embracing errors and learning *how to learn* from them is an important ingredient to success as a coder.

Programming languages such as Python provide tools for understanding errors, or exceptions, as they're commonly known in Python. 

Exceptions can and do occur for any number of reasons, and Python has a [long list of exception types](https://docs.python.org/3/library/exceptions.html) that it will raise depending on the situation.

You don't have to memorize that list, but it's important to understand that these error types will appear in "tracebacks" -- also known as a [stack trace](https://en.wikipedia.org/wiki/Stack_trace) -- when an error occurs. 

In Python, tracebacks display the location and type of an error, as well as the steps that led up to the exception. Note that unlike some other languages, stack traces in Python are read from top to bottom; the bottom line displays the last step of the program that led to the error.

> Here's another brief tutorial on [how to read tracebacks](http://cs.franklin.edu/~ansaria/traceback.html).

Here's an example from Wikipedia:

```
def a():
    i = 0
    j = b(i)
    return j

def b(z):
    k = 5
    if z == 0:
        c()
    return k/z

def c():
    error()

a()
```

The above program would produce the following error:

```
Traceback (most recent call last):
  File "tb.py", line 15, in <module>
    a()
  File "tb.py", line 3, in a
    j=b(i)
  File "tb.py", line 9, in b
    c()
  File "tb.py", line 13, in c
    error()
NameError: global name 'error' is not defined
```

From the traceback we can see that the error occurs in the `c` function. It appears that we tried to call a function that is not defined. 

We also can see the "call chain" that led up to the error: `a` called `b`, which in turn called `c`.

When interpreting tracebacks, you'll generally want to start at the bottom of the list at the line that caused the error. That should point you to the most likely source of the error. If nothing obvious jumps out at the location, you can work your way up the call chain, or stack, until you pinpoint the issue.