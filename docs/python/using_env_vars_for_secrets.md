# Using Environment Variables to Stash Secrets

It's generally a bad idea to hard-code passwords, API keys and other sensitive information directly in a script.

When writing scripts, one strategy to protect such information is to stash it away in a [shell configuration file](https://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html) such as `~/.bashrc` or `~/.bash_profile`.

This involves exporting an [environment variable](https://www.computerhope.com/unix/uenv.htm) in the configuration file, so that it becomes available in the shell's environment when you open a terminal.

For example, let's say we put the following into our `~/.bash_profile` file:

```
export SUPER_SECRET_API_KEY="FASDASDF"
```

When you open up a new shell, you should be able to see the variable using the `printenv` command:

```
~/Desktop> printenv | grep SUPER_SECRET_API_KEY
SUPER_SECRET_API_KEY=FASDASDF
```

Similarly, this variable can be accessed from a Python script or application using the [os.environ](https://docs.python.org/3/library/os.html#os.environ) function:

```
# example in the Python interpreter
>>> import os
>>> os.environ['SUPER_SECRET_API_KEY']
'FASDASDF'

```

A more fully fleshed-out example in the context of a Python script:

```
# my_awesome_scraper.py
import os
import requests

API_KEY = os.environ['SUPER_SECRET_API_KEY']
headers = {"X-API-Key": API_KEY}

requests.get(
	"http://awesomedata.json",
	headers=headers
)

```

Finally, it's worth noting that there are [other tools and strategies](https://stackoverflow.com/questions/7014953/i-need-to-securely-store-a-username-and-password-in-python-what-are-my-options) that provide higher degrees of security, and these should be considered depending on the use case and sensitivity of the data handled by the application.