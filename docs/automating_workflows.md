# Automating workflows with DataKit

In this course, we'll use [DataKit][], an open-source command-line tool, to automate various aspects of our classroom workflow. DataKit will help us:

* Create a standard project structure for all code work
* Use virtual environments for Python
* Save work locally using version control (git)
* Submit work on GitHub

DataKit is designed to help simplify all of the above and more. 

The Associated Press created this tool to streamline routine tasks, facilitate collaboration, and more easily publish data projects. We've customized the tool to optimize it for use in class.

See [here](https://github.com/stanfordjournalism/cookiecutter-stanford-progj) for more details on how it will be used in class.

[DataKit]: https://datakit.ap.org/

## Install

Follow the steps in [Tech Setup - DataKit](tech_setup.md). *Note, you must first work through the preceding steps in the Technical Setup.*

## Kick the tires

Execute the below command to create your first DataKit project.

> When prompted, choose `2 - Exercise` as the "repo\_type" and type `csvkit` for the "project\_number\_or\_shortname". 

> For everything else, you can accept the default values by hitting `return`.

```
datakit project create --template gh:stanfordjournalism/cookiecutter-stanford-progj
```

After running the above, pay careful attention to the shell output. It should provide the URL for the auto-generated GitHub repo.

Next, install Python dependencies for the project and test the process of saving work.

```
# Navigate to the newly created project folder
cd comm-177p-exercise-csvkit/

# Install Python dependencies
pipenv install

# Move your csvkit code to the new project
cp /path/to/csvkit_wrangle.sh scripts/csvkit_wrangle.sh

# Activate a sandboxed environment for this project
pipenv shell

# Save your work locally
invoke code.save

# Push work to GitHub
invoke code.push
```

Congratulations, your work should now be saved in a private repo on GitHub!!

In the future, you can use DataKit to create new code repos for assignments by simply running `datakit project create`.

