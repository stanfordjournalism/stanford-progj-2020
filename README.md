# Stanford ~ Programming in Journalism

Sundry notes and code bits for Stanford's Programming in Journalism class (winter quarter 2020).

## Important links

* [Syllabus][]
* [Assignments](assignments/README.md)
* [Bookshelf](docs/bookshelf.md) - recommended books, tutorials, cheatsheets, etc.
* [Code solutions](https://github.com/zstumgoren/stanford-progj-2020-solutions) - A private repo containing solutions to class exercises.
* [Datakit](docs/datakit.md) - overview and details on install and usage
* [Getting Help](docs/getting_help.md) - Resources and strategies for finding help.
* [Glossary](docs/glossary.md) - technical terms used in class
* [Python](docs/python/README.md) - overview, tutorials, etc.
* [Technical setup](docs/tech_setup.md) and [FAQ](docs/tech_faq.md) - recommended and required software (all free)
* [Workflow advice](docs/workflow_advice.md) - working on the command line, etc.

[Syllabus]: https://canvas.stanford.edu/courses/111874/assignments/syllabus

## Class notes

### Week 1

#### Day 1 - Course Intro

* Overview of the course and syllabus.
* Discuss the [history](docs/history.md) of code and data analysis in journalism. 
* Dip our toes into Bash. 
* Software install party (w00t!!)
* [Assignment 0](assignments/0.md) - Tech setup; Unix practice and reading (**Due: Mon. Jan 13th**)

#### Day 2 - The Owl, Problem Solving, and the Unix Workbench

* [The Owl, Problem Solving, and the Unix Workbench](docs/owl_probs_unix.md)
* Group problem-solving exercise: Program your way to the Oval
* Hands-on bash practice with [CLI murder mystery][] and [bashcrawl][]
* [Software installs](docs/tech_setup.md), part deux (ssh keys and Python)
* [Assignment 0](assignments/0.md) - Tech setup; Unix practice and reading (**Due: Mon. Jan 13th**)

[CLI murder mystery]: https://github.com/veltman/clmystery
[bashcrawl]: https://gitlab.com/slackermedia/bashcrawl

### Week 2

#### Day 3 - Power Tools for Data Wrangling

* [Power Tools for Data Wrangling](docs/power_tools_for_data_wrangling.md)

#### Day 4 - Power Tools cont.'d and Intro to DataKit

* [Bash drill](exercises/bash_dril.md)
* Wrap up csvkit exercise from [Power Tools for Data Wrangling](docs/power_tools_for_data_wrangling.md)
* [Automating workflows](docs/automating_workflows.md) and [DataKit install](docs/datakit.md)
* **[Assignment 1](assignments/1.md)** - Python ramp-up and Failed Banks shell script (**Due: Wed. Jan. 22nd**)

### Week 3

#### Day 5 - MLK Day

No class.

#### Day 6 - Failed Banks and Python

* [Workflow Advice](docs/workflow_advice.md) - In particular, working in the shell and with a code editor.
* [Getting Help](docs/getting_help.md) - How to ask G.O.O.D. questions and other advice/resources on getting help when programming.
* [DataKit](docs/datakit.md) overview, including details on virtual environments, the benefits of git/GitHub, and daily workflow with DataKit.
* Submit [Assignment 1](assignments/1.md) using DataKit.
* **[Assignment 2](assignments/2.md)** - DataKit reading and Python lists and dicts (**Due: Mon. Jan. 27th @ 1:30pm**)

### Week 4

#### Day 7 - Python intro and practical skills


* Python intro and applying the basics
  * [Python overview and coding contexts](docs/python/overview.md)
  * The (i)Python interactive interpreter: `pip install ipython`
  * [Embracing errors](docs/python/embracing_errors.md)
  * [Counting and filtering](docs/python/count_filter.md)
  * [Reading and writing text files](docs/python/file_io.md)
  * **[Assignment 3](assignments/3.md)** - Python strings and Awesome Animals coding exercise (**Due: Wed. Jan. 29th @ 1:30pm**)
  * Review [Assignment 1](assignments/1.md) solutions, assuming everyone has submitted and time allows

#### Day 8 - Libraries, CSVs and remote files in Python
  
  * [Working with libraries](docs/python/libraries.md) - standard library and 3rd-party libraries
  * [Reading and writing CSVs](docs/python/csv.md)
  * [Downloading files](docs/python/remote_files.md)
  * **[Assignment 4](assignments/4.md)** - Python functions and failed banks Python script (**Due: Mon. Feb. 3rd @ 1:30pm**)

### Week 5

#### Day 9 - APIs and the News

* [APIs and the News](docs/apis_and_the_news.md) overview and [presentation](https://tinyurl.com/apis-and-the-news)
* [Working with APIs](docs/python/working_with_apis.md)
* [Portable (file) paths in Python](docs/python/portable_paths.md)
* **[Assignment 5](assignments/5.md)** - Python sorting, portable paths and register for ProPublica API key (**Due: Mon. Feb. 5th @ 1:30pm**)

#### Day 10 - Art of Functions and Senate Impeachment Script

* [The Art of Writing Functions](docs/python/art_of_functions.md)
* **[Assignment 6](assignments/6.md)** - Web basics (**Due: Mon. Feb. 10th @ 1:30pm**)
* **[Assignment 7](assignments/7.md)** - Breaking ranks on impeachment Python script (**Due: Wed. Feb. 12th @ 1:30pm**)


### Week 6

#### Day 11 - Web scraping for the news

* [Web scraping for the news](docs/web_scraping/README.md) - a high-level overview of web scraping in a news context.
* [Web scraping 101](docs/web_scraping/101.md) - how to dissect a website, various obstacles to scraping and strategies for overcoming them
* [Web scraping exercises](docs/web_scraping/exercises.md) - some websites to challenge your newfound scraping skills
* [Web scraping resources](docs/web_scraping/resources.md) - tutorials, etc.
* **[Assignment 8](assignments/8.md)** - Web Scraping Ramp-up (**Due: Wed. Feb. 12th @ 1:30pm**)


#### Day 12 - API Services and Data Pipelines with Modules

* [API Services](docs/api_services.md)
* [OpenCalais Entity Extraction](code/calais_example/README.md)
* [Data Pipelines with Modules](docs/python/data_pipelines_with_modules.md)
* **[Project: FDA Recall Entities](projects/fda_recall_entities.md)** - Scrape FDA recalls and extract entities using OpenCalais API (**Due: Wed. Feb. 19th @ 1:30pm**)

### Week 7

#### Day 13 - President's Day; no class

#### Day 14 - Data Journalism Overview and Intro to Jupyter

* [Data Journalism - A Very Brief Tour](https://docs.google.com/presentation/d/1OPVDw_5toenId-RehkBwuvvV5lJMrHb7579U4Uj1eCg/edit?usp=sharing)
* [Whirlwind Tour of the Data Journalism Process](https://docs.google.com/presentation/d/1cEoPLJpZ6FVNLtW5f3jtWhgEeIhPv6eqWae85LAFPcs/edit?usp=sharing)
* [Data Analysis with Jupyter and pandas](docs/python/data_analysis_intro.md)
* **[Assignment 9 - First Python Notebook](assignments/9.md)**

### Week 8

#### Day 15 - Final Project

* **[Final Project - SF Data Analysis](projects/sf_data_analysis.md)** - Overview of final project and begin working on story ideas and data sleuthing/vetting.
 * **Story idea presentations** are **due Wed. Feb. 26th @ 1:30pm**
 * **Final project presentations** and related Jupyter notebooks are **due Mon. March 9th @ 1:30pm**.

#### Day 16 - Story idea presentations

 * Groups will present story ideas for the [final project](projects/sf_data_analysis.md).
 * Work on project analysis, with opportunity for one-on-one help (time permitting).

### Week 9

#### Day 17 - Data Workshop

Work on **[Final Project - SF Data Analysis](projects/sf_data_analysis.md)**.

#### Day 18 - class cancelled

No class due to NICAR 2020 conference.

### Week 10

#### Day 19 - Final Project Presentations

Present and discuss **[Final Project - SF Data Analysis](projects/sf_data_analysis.md)**.

#### Day 20 - Presentations and course wrap-up

Wrap up final project presentations, followed by
course review and reflection.
