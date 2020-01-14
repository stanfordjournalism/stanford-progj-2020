# CLI Power Tools for Data Wrangling

Unix provides many tools for data acquisition and wrangling. These include built-in tools for working with files -- e.g. grep, cut, and sort -- as well as an expanding universe of third-party tools.

Today we'll focus on a few tools that are especially useful to journalists. We'll begin with utilities for acquiring data, and then move on to a suite of tools for data wrangling provided by [csvkit][].

We'll also mention a few other data wrangling power tools that can help streamline the process of acquiring and even publishing data.

[csvkit]: https://csvkit.readthedocs.io/en/latest/

## Downloading data

Acquiring data is typically the first step in a project. 

The Unix [curl][] and [wget][] commands provide a variety of features for obtaining remote files. They're handy for one-off experimentation or as part of a re-usable shell script that can be run at pre-scheduled times.

Let's start getting a feel for these commands. Open a shell and run the below:

[curl]: https://curl.haxx.se/docs/manpage.html
[wget]: https://en.wikipedia.org/wiki/Wget

```
# Download Stanford Journalism home page and print to the shell
curl journalism.stanford.edu

# Download the home page and redirect the content to a local file
curl journalism.stanford.edu > sj_home.html

# Use wget to download the file
wget journalism.stanford.edu
```

Based on the above, spend a few minutes answering these questions:

* How do `curl` and `wget` differ based on these initial examples?
* Does `wget` print the file contents to the shell? 
* Where does it save the file contents? 
* What happens if you run `wget` again? On your shell, type `man wget` and scroll through it's options to see if there's a way to force the command to overwrite pre-existing files.
* Is there an option for `curl` that downloads a file directly to an identically named file locally (rather than printing the contents to the shell)? Explore `man curl` to see if you can find it. What is the name of the file `curl` downloads when using the aforementioned option?

At first blush, `curl` and `wget` appear to do the same job. But they also have unique strengths. In addition to fetching individual files, `curl` is especially useful for interacting with APIs. This can be helpful when first experimenting with the features of a new API as part of a larger project (where the ultimate goal may be to encode the data acquisition in a programming language such as Python).

`wget` lets you easily mirror a part or all of an entire website. It's especially useful if you're worried about keeping a local copy of a site that may disappear from the web (for example, [Wikileaks](https://wikileaks.org/)).

Check out the Unix Shell tutorial for a more [thorough comparison](https://carpentries-incubator.github.io/shell-extras/03-file-transfer/index.html) of `curl` and `wget`.

## Data wrangling

Data wrangling encompasses a variety of tasks common to news projects (and data work in general). A few of the common tasks are:

* **Converting** data from one format to another.
* **Leveling up** on the characteristics of a data set. Are the fields quantitative or qualitative? What is the distribution of the data in the fields? Min/max values? Are there missing values?
* **Stacking data** spread across different files. This typically involves a "vertical" merge of CSVs that are identical in structure, for example a data set that is split into yearly files. Merging the yearly files into a single larger file can make it easier to process and analyze using a database or programming language. This is similar in concept to a [SQL UNION][] query.
* **Joining data** for analytical purposes. This typically involves a "horizontal" merge of secondary data sources that share common identifiers. For example, to determine the per capita budget expenditures for a list of cities, you could merge Census population estimates with a list of spending figures for cities using a FIPS code or the combination of city and state. This is similar in concept to a [SQL JOIN][].
* **Subsetting columns** to reduce complexity and/or file size. Government data often has dozens of data columns. It can be much easier to work with the data by targeting only the fields important to your analysis. This is similar in concept to a [SQL SELECT][] query.
* **Filtering rows** is among the most common activities for a data project. This is similar in concept to a [SQL WHERE][] clause.
* **Sorting data** is another common task. csvkit provides a command-line utility to easily sort data by column values for simple cases, and also allows you to write raw SQL against data for more complex scenarios. This is similar in concept to a [SQL ORDER BY][].

[SQL UNION]: https://www.w3schools.com/SQL/sql_union.asp
[SQL JOIN]: https://www.w3schools.com/SQL/sql_join.asp
[SQL SELECT]: https://www.w3schools.com/SQL/sql_select.asp
[SQL WHERE]: https://www.w3schools.com/SQL/sql_where.asp
[SQL ORDER BY]: https://www.w3schools.com/SQL/sql_orderby.asp

## Wrangling with csvkit

[csvkit][] provides a suite of command-line tools that help with the data wrangling tasks mentioned above, and much more. 

It's a well-documented and rich suite of tools that exemplifies the Unix philosophies of "small parts, loosely joined" and "do one thing and do it well." csvkit is handy for quickly exploring and wrangling data, and for creating automated/reproducible data pipelines. It can even let you do a bit of data analysis before diving into higher-level tools such as DB Browser, RStudio or Jupyter Notebook.

### Group exercise

Take a few minutes to review the feature's mentioned on [Why csvkit?][]. 

Next, install csvkit and try using its tools to explore and wrangle the data: `pip install csvkit`

> Note, our end goal is to automate all these steps in a single shell script, so keep notes on the commands you run.

Now we're ready to use csvkit. Your task will be to hunt down the commands appropriate to each step in the process below. 

As you identify the appropriate commands and begin experimenting on the command line, be sure to consult the more [detailed documentation][] for each command to get a sense of its features and options. Certain commands will require the use of options described in those detailed docs.

Ok, on to some wrangling!

* Download the following files using `curl` or `wget`:
  * [city\_budgets\_2019.xlsx][]
  * [city\_budgets\_2020.xlsx][]
  * [city\_pops.xlsx][]
* Convert all three Excel files into CSVs. All three CSVs should have the same names as their source Excel files, except they should have a `.csv` extension (e.g. `city_budgets_2020.csv`).
* Explore the data using csvkit's tools for data introspection. Take note of which tools you tried and what kind of information they gave you (better yet, save the output!).
* Combine the two city budget files and save them in a single file called `city_budgets.csv`
* Join the city population data to the merged budgets file and save it in a new file called `city_budget_pop.csv`
* Filter the data to only keep cities in California. Save it in a new file called `city_budget_pop_ca.csv`
* Create a new file by cutting out the state fields from `city_budget_pop_ca.csv`. There should be two state fields in the source file: one from the budgets data along with the state field merged in from the city populations. Save the subsetted data into a new file called `city_budget_pop_ca_subset.csv`.
* Sort `city_budget_pop_ca_subset.csv` by year and amount in descending order using csvkit's pre-built utility for sorting. 
* Sort `city_budget_pop_ca_subset.csv` by year (lowest to highest) and by amount (highest to lowest) using csvkit's tool for writing SQL against a CSV. Which city had the highest overall budget in 2019 and 2020?
* Flesh out this [shell script][] to automate all of the above steps. You can download a local copy with the below command:

```
curl -O https://raw.githubusercontent.com/stanfordjournalism/stanford-progj-2020/master/code/csvkit_wrangle.sh
```

* And run the script with this command:

```
sh csvkit_wrangle.sh
```


[Why csvkit?]: https://csvkit.readthedocs.io/en/latest/#why-csvkit
[detailed documentation]: https://csvkit.readthedocs.io/en/latest/cli.html

[city\_budgets\_2019.xlsx]: https://raw.githubusercontent.com/stanfordjournalism/stanford-progj-2020/master/data/city_budgets_2019.xlsx
[city\_budgets\_2020.xlsx]: https://raw.githubusercontent.com/stanfordjournalism/stanford-progj-2020/master/data/city_budgets_2020.xlsx
[city\_pops.xlsx]: https://raw.githubusercontent.com/stanfordjournalism/stanford-progj-2020/master/data/city_pops.xlsx
[shell script]: https://github.com/stanfordjournalism/stanford-progj-2020/blob/master/code/csvkit_wrangle.sh

## Even more power tools

[Datasette][] is a project created by Django co-founder Simon Willison that helps journalists explore and publish data.

Per the official docs:

> It helps people take data of any shape or size and publish that as an interactive, explorable website and accompanying API.

What's more, its [growing ecosystem][] of tools streamlines the process of converting and importing data from sundry formats into SQLite databases.

[socrata2sql][] is among the tools in the datasette universe. It's incredibly useful for quickly obtaining data from government agencies that use the Socrata data publishing platform (e.g. [San Francisco][] and [California state][]).

Here's an example of how to download [eviction data for San Francisco][]:

[eviction data for San Francisco]: https://data.sfgov.org/Housing-and-Buildings/Eviction-Notices/5cei-gny5

> Note, you must first `pip install socrata2sql`

```
socrata2sql insert data.sfgov.org 5cei-gny5 
```

There are many other shell tools out there for data acquisition and wrangling. Here are a few others worth exploring:

* [census-data-downloader][] helps download Census data in a human-friendly format
* [nws-wwa][] helps with National Weather Service data
* [twitter-to-sqlite][] lets you easily save Twitter data to SQLite
* [python-us][] has a command-line tool that lets you easily query for US and states metadata (e.g. state abbreviations, FIPS codes, etc.)

News organizations with a culture of sharing code are a good place to troll for other tools. Here are a few news org GitHub accounts that contain hidden gems:

* [Associated Press](https://github.com/associatedpress)
* [Buzzfeed News](https://github.com/buzzfeednews)
* [LAT](https://github.com/datadesk)
* [NYT](https://github.com/newsdev)
* [ProPublica](https://github.com/propublica)

[Datasette]: https://datasette.readthedocs.io/en/stable/index.html
[growing ecosystem]: https://datasette.readthedocs.io/en/stable/ecosystem.html
[socrata2sql]: https://datasette.readthedocs.io/en/stable/ecosystem.html#socrata2sql
[San Francisco]: https://data.sfgov.org
[California state]: https://data.ca.gov

[twitter-to-sqlite]: https://github.com/dogsheep/twitter-to-sqlite
[python-us]: https://github.com/unitedstates/python-us#cli
[census-data-downloader]: https://github.com/datadesk/census-data-downloader
[nws-wwa]: https://github.com/datadesk/nws-wwa



## The virtues of automation

The use of command line tools (and code in general) has a number of virtues. It allows us to **automate** often time-consuming workflows and create **reproducible data pipelines.** This lets us more easily update projects in the future and serves as a form of "self-documentation" on our process.

Workflows captured in code enable us to **share our work** with teammates -- a boon for improving accuracy and mindshare on projects.

Further, encoding a data pipeline allows us to more easily share work with the public. Such **transparency** can help increase trust in the journalistic process and enable others to build on our work.