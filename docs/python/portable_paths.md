
# Portable Code

- [Overview](#overview)
- [Relative Paths](#relative-paths)
- [Environment Variables and pipenv](#environment-variables-and-pipenv)
- [Path Tricks in Python](#path-tricks-in-python)
  - [Constructing file paths](#constructing-file-paths)
  
## Overview

Portable code is designed to run easily on any system. An important concern when writing code in a team environment is to ensure that file paths are not specific to one person's system.

A script that uses a [fully qualified file name](https://en.wikipedia.org/wiki/Fully_qualified_name#Filenames_and_paths), for example, would *not* run correctly on anyone else's computer:

```
path = '/Users/jsmith/Desktop/my-project/data.csv'
with open(path, 'r') as source_file:
	text = source_file.read()
```

In fact, J. Smith will be in for a rude surprise if he gets a new laptop and picks a different username.

Using a file path such as `~/Desktop/my-project/data.csv`, where the [tilde is dynamically resolved]([tilde expansion](http://www.gnu.org/software/bash/manual/html_node/Tilde-Expansion.html)) to the user's home directory (e.g. `/Users/jsmith`) is not much better. We're still specifying  the `Desktop`, which may not be where another user places the `my-project` folder.

```
path = '~/Desktop/my-project/data.csv'
with open(path, 'r') as source_file:
	text = source_file.read()
```

Ideally, we want a way to dynamically construct file paths so that they'll work on any user's machine. Below are a few strategies that help us construct paths designed to 

## Relative Paths

A [relative file path](https://en.wikipedia.org/wiki/Path_%28computing%29#Absolute_and_relative_paths) is one constructed relative to the [current working directory][]. This avoids the need to provide a fully qualified (or absolute path).

[current working directory]: http://www.linfo.org/current_directory.html

Imagine we have the following files:

```
~/project/scripts/myscript.py
~/project/data/awesome.csv
```

If you navigate to the `scripts/` directory in the shell, it's possible to read the contents of `awesome.csv` by using the [dot dot](http://www.linfo.org/dot.html) syntax (`..`), which translates to the parent directory of the [current working directory](http://www.linfo.org/current_directory.html).

```
cd ~/project/scripts/
cat ../data/awesome.csv
```

In the same way, this relative file path can also be used in `scripts/myscript.py`:

```
with open('../data/awesome.csv', 'r') as source_file:
	text = source_file.read()
```


However, this approach has a significant shortcoming: It will only work if a user navigates to the `scripts/` directory before running the script.

```
cd ~/project/scripts/
python myscript.py
```

The above works because the current working directory is set to `scripts/`. Therefore, the `..` translates to the parent directory where `data/` is indeed located.

Running the script from the root of the project (or anywhere else on the file system), would cause an error because the parent directory would not contain the `data/` directory:

```
# This would fail because "project" is the 
# current working directory
cd ~/project/
python scripts/myscript.py
```

The above code would attempt to read `~/code/data/awesome.csv`, which is clearly not correct.

## Environment Variables and pipenv

The bash shell environment includes [a variety of built-in variables](https://bash.cyberciti.biz/guide/Variables) that are available to your scripts. You can list all of these variables using the `printenv` command on the shell. The list is quite long, as you can see.

Some of these variables, such as `$HOME`, can be quite useful in both bash and Python scripts. Further, you can define your own variables and make them available to scripts. One common strategy involves setting variables for API keys in shell configuration files. For example, you might place `export TWITTER_API_KEY=your-api-key` in the `~/.bash_profile` configuration file. Every time a new shell is opened, this value will be available in the shell's environment.

We can then look up and use the value in our scripts, allowing us to avoid hard-coding such sensitive information into the script itself.

In a similar fashion, the [DataKit](../datakit.md) [project template](https://github.com/stanfordjournalism/cookiecutter-stanford-progj) we've been using automatically creates a few helpful environment variables. These variables are stored in a hidden `.env` file in each project, and are [automatically exported](https://pipenv.readthedocs.io/en/latest/advanced/#automatic-loading-of-env) (without need for using the `export` command explicitly) our project's virtual environment whe we run `pipenv shell`.

```
~> cd ~/code/comm-177p-assignment-1
~/code/comm-177p-assignment-1> cat .env
PROJECT_ROOT=${PWD}
PYTHONPATH=${PROJECT_ROOT}
DATA_DIR=${PROJECT_ROOT}/data

# Notice that .env variables get loaded below
~/code/comm-177p-assignment-1> pipenv shell
Loading .env environment variables…
Launching subshell in virtual environment…
 . /Users/tumgoren/.local/share/virtualenvs/comm-177p-assignment-1-aN5P1Pxo/bin/activate
~/code/comm-177p-assignment-1>  . /Users/tumgoren/.local/share/virtualenvs/comm-177p-assignment-1-aN5P1Pxo/bin/activate


(comm-177p-assignment-1) ~/code/comm-177p-assignment-1> printenv | grep DATA_DIR
DATA_DIR=/Users/tumgoren/code/comm-177p-assignment-1/data
```

 Above, note that:
 
 * We used [command substitution](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html) in the variable definitions to dynamically generate the values based on the current working directory.
 
 The variables can now be used by shell scripts and Python code to build portable paths to files in the project. Again, assume we have a project structure such as below:
 
 ```
 ~/project/scripts/myscript.py
~/project/data/awesome.csv
 ```
 
Then `myscript.py` could dynamically build a path to `awesome.csv` using the following strategy:

```
import os
data_dir = os.environ['DATA_DIR']
# Use the "join" function to join the path components
csv_file = os.path.join(data_dir, 'awesome.csv')
with open(csv_file, 'r') as source_file:
	text = source_file.read()

```

The one potential hiccup with this approach is that it will only work if `pipenv shell` is run from the top-most directory of the project (commonly called the project "root"). If you were to activate the enviroment from, say, the `scripts/` directory, the paths would be incorrect. So be sure to only activate the project environment from the repo's root.

There are even more robust strategies for dynamically generating file paths in Python, but for this course, we'll generally rely on the use of the shell variable strategy described here.

## Path Tricks in Python

The final strategy for creating portable code involves using Python itself to construct file paths, rather than relying on environment variables. Assuming the same file structure mentioned above, below is an example that would work in `scripts/myscript.py`:

```
import os
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
csv_file = os.path.join(project_root, 'data/awesome.csv')
with open(csv_file, 'r') as source_file:
	text = source_file.read()
```

Notice that we're using the Python [Path library](https://docs.python.org/3/library/pathlib.html) to dynamically resolve the root of our project, based on a special variable called `__file__`. This variable is automatically created by Python and contains the name of the file from which the Python code was loaded (in this case `myscript.py`). We feed this variable to `Path`, which in turn provides some helpful methods related to...you guessed...file paths. The  `.parent` method provides the parent directory of a file or directory. By calling it two times, we're able to accurately resolve the project root relative to `scripts/myscript.py`.

This is a somewhat more advanced use of Python to dynamically construct file paths. It's arguably a bit more robust than the environment variable method described above, although it requires us to write more complex code than if we were to simply rely on an automatically generated environment variable.