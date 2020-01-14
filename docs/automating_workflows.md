# Working at the Speed of News

> "Laziness: The quality that makes you go to great effort to reduce overall energy expenditure. It makes you write labor-saving programs that other people will find useful and document what you wrote so you don't have to answer so many questions about it." ~ [Larry Wall](http://threevirtues.com/), creator of Perl 

When news breaks and you're new to a beat, it can be especially stressful to hunt down sources and pull together copy under deadline. Veteran reporters, on the other hand, often have (slightly) lower stress levels. They typically have a wealth of domain
knowledge to dip into. They're intimately familiar with the trends and key players on their beat, as well as documents that can provide background or help answer questions. They have a stable of human sources who can speak to an issue or point them toward other, more relevant sources.

In a similar vein, data journalists and newsroom developers just starting out often work in ad hoc, "messy" ways. This is natural when you join a team, learn a new technology, etc. But over time, these technical-minded journalists build up a stable of tools and resources to help themselves and [their colleagues][] work at the speed of news. 

Newsroom coders make a virtue of "laziness." Here are a few examples of their work:

* [Content publishing](https://tarbell.readthedocs.io/en/1.0.10/)
* [Data analysis](https://agate.readthedocs.io/en/1.6.1/)
* [Data-gathering web admins](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/)
* [Document handling](https://www.documentcloud.org/)
* [News tips](https://newsklaxon.org/)
* [Storybots](https://slate.com/technology/2014/03/quakebot-los-angeles-times-robot-journalist-writes-article-on-la-earthquake.html)

[their colleagues]: https://www.nytimes.com/2019/03/26/reader-center/times-documents-reporters-cohen.html

## Automating workflow with DataKit

In this course we'll dip into this culture of automation by using [DataKit][], an open-source command-line tool created by The Associated Press. DataKit was designed in a team environment to bring sanity to data projects. Among other things, it helps standardize project structures, easily share code and data with teammates, and even publish data as part of story packages.

It also makes it easy to customize workflows to suit different teams and individuals. We've customized DataKit for use in the classroom.

DataKit will help us streamline our workflow while applying best practices from the worlds of data science and software. Among other things, it will help us:

* Create standard project structures for all code work
* Use virtual environments for Python
* Save code and data in version control (git)
* Publish our work to GitHub, making it easy to open-source if we choose
* Easily share our work with instructors

See [here](https://github.com/stanfordjournalism/cookiecutter-stanford-progj) for more details on our classroom workflow and customizations.

[DataKit]: https://datakit.ap.org/

## Install

Follow the steps in [Tech Setup - DataKit](tech_setup.md). *Note, you must first work through the preceding steps in the Technical Setup.*

## Kick the tires

As a first project, let's assume you've created a [data processing script using csvkit](power_tools_for_data_wrangling.md#wrangling-with-csvkit).

Execute the command below to create your first DataKit project. 

> Before running the command, take note of the commented-out instructions (i.e. the lines prefixed with `#`).

```
# When prompted:
#  - Choose "2 - Exercise" as the "repo_type" 
#  - Type "csvkit" for the "project_number_or_shortname". 

# For other prompts, hit "return" to accept default values

datakit project create --template gh:stanfordjournalism/cookiecutter-stanford-progj
```

After running the above, pay careful attention to the shell output. It should provide the URL for the auto-generated GitHub repo.

Next, install Python dependencies for the project and test the process of saving work.

```
# Navigate to the newly created project folder
cd comm-177p-exercise-csvkit/

# Install Python dependencies
pipenv install

# Copy your csvkit code to the new project
# NOTE: Substitute the actual path to csv_wrangle.sh on your machine
cp /path/to/csvkit_wrangle.sh scripts/csvkit_wrangle.sh

# Activate a sandboxed environment for this project
pipenv shell

# Save your work locally
invoke code.save

# Push work to GitHub
invoke code.push
```

Congratulations, your work should now be saved in a private repo on GitHub!!

## Day-to-day with DataKit

In the future, you can use DataKit to create new projects by simply running `datakit project create`, followed by the other commands mentioned above.

You should get into the habit of saving and publishing your work to GitHub whenever you add, change or delete files. This applies to both code and data files.

If you're making changes to a previously created project, you won't need all of the commands mentioned above. 

Here's the short list of commands you'll need when working with an existing project:

> Note: Every project's `README.md` includes reminders on this workflow.

```
# Navigate to the project folder
cd comm-177p-exercise-csvkit/

# Activate a sandboxed environment for this project
pipenv shell

# Save your work locally
invoke code.save

# Push work to GitHub
invoke code.push
```



