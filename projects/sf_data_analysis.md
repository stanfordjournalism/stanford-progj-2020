# SF Data Analysis

- [Overview](#overview)
- [Deadline](#deadline)
- [Develop a story idea](#develop-a-story-idea)
- [Notebook details](#notebook-details)
- [Project phases](#project-phases)
- [Code setup](#code-setup)
- [Reference materials](#reference-materials)
- [Submission](#submission)

## Overview

For this project, you will [develop a news story idea](#develop-a-story-idea) and execute a related Jupyter Notebook analysis using data from the San Francisco open data portal: [DataSF.org][].

The story idea and analysis can be developed individually or as a group (no more than 4 people per group). Each group will be responsible for presenting a completed analysis during the final week of class.

We encourage group collaboration, but note that each student in a group must submit her/his own copy of the Jupyter notebook. One group member should take lead on the presentation, but all group members should be prepared to answer questions about the project.

[DataSF.org]: https://datasf.org/

## Deadline

**Submissions are due by start of our first class in week 10.** 

**Late submissions for this assignment will not be accepted** since we will spend the final week of class presenting and discussing the analyses. Therefore it's critical you get started on this assignment early and ask for feedback over the course of the next few weeks.

## Develop a story idea

This project requires locating a data set that can help explore a clearly articulated, journalistically interesting question.

**A well-formed question is one that can be answered quantitatively,** especially by exploring trends and outliers.

> Have response times of fire emergency personnel gone up or down in the last five years? 
 
> Are reports of [human feces](https://www.npr.org/2018/08/01/634626538/san-francisco-squalor-city-streets-strewn-with-trash-needles-and-human-feces) increasing in the city?

> What areas of the city have seen the most housing growth in recent years?

The best story ideas often originate on beats, so we encourage you to find data that helps explore your own pre-existing ideas. The only requirement is that you must use one (or more) data sets from [DataSF.org][].

If you're hard-pressed to come up with a story idea, it's fine to explore [DataSF.org][], individually or as a group, to pinpoint data sets of potential interest. 

Don't worry if the news or acedemia have already covered a story idea. For this project, we're less focused on breaking original ground than on formulating a question and executing a news analysis to explore that question. 

Previous reporting is a great source of inspiration, and it's fine to build on ground tread by others.

If you can't find a story idea/data of your own, here are a few suggestions that are worth exploring:

- [311 calls](https://data.sfgov.org/City-Infrastructure/311-Cases/vw6y-z8j6)
- [Fire incidents](https://data.sfgov.org/Public-Safety/Fire-Incidents/wr8u-xric)
- [Eviction notices](https://data.sfgov.org/Housing-and-Buildings/Eviction-Notices/5cei-gny5)
- [Restaurant scores](https://data.sfgov.org/Health-and-Social-Services/Restaurant-Scores-LIVES-Standard/pyih-qa8i)

## Notebook details

Before starting this assignment, please carefully review this [example Jupyter notebook](../code/sfgov/sfpd-incidents.ipynb). It demonstrates the expected style, format and content of this assignment and contains a sprinkling of advice on working with data and technical tips.  Below are resources that are also worth reviewing:

- [Analyzing AZ Traffic Stops](https://github.com/newshackaz/az_stops/blob/master/completed_analysis.ipynb) offers a solid walk-through of the process of data quality assessment, analysis and viz
- [LAT DataDesk Notebooks](https://github.com/datadesk/notebooks) - many great examples of notebook analysis

The Jupyter notebook you create for this assignment must blend narrative explanation with code. It must contain the following elements:

- **A narrative summary** at top *briefly* describing the story idea and highlighting important background information about the data. This should include a description of the key fields used in your analysis, along with any significant data anomalies or issues and an explanation of how you worked around these issues.   

- **At least 2 "Findings".** These should be summarized in narrative -- e.g. "Arrests were highest in September" -- and demonstrated clearly using code and/or visualization.

- The use of **at least two data visualizations** as part of the data vetting and analysis process. Simply printing a table does *not* count as a visualization.
 
- **Data vetting for each of the key fields** you mention in the summary. At minimum, you must demonstrate in code and related narrative:
  - how you checked for missing data or malformed/unexpected values for the key fields in your analysis
  - how you addressed such issues (e.g. "The subset of records I was focusing on did not include any malformed data.").

## Project phases

### Generate an idea

Form into groups of up to 4 students (it's also fine to work individually).

As a group, discuss and identify a **well-formed** [story question](#develop-a-story-idea) that can be explored using data from [DataSF.org][]. Remember, a well-focused question is **quantifiable.**

### Assess and plan

The goals for this phase are to:

* Identify and assess the usability of the overall data set and key data fields, i.e. fields from the data set identified in [Phase 0](#phase-0) that will help address the story question.
* Get a rough sense of any potential technical roadblocks.
* Lay out a plan of attack for the analysis/visualization.

Assessing the data entails working with the provided documentation for a data set, as well as some preliminary exploration in Jupyter.

Some key questions to consider are below.

**Are there any potential issues with the overall data set or target fields, such as missing or incorrect values? Can these issues be worked around?**

For example, if a dataset contains only partial data for the most recent year, you'll want to exclude this partial year of data for a multi-year analysis. 

Or perhaps a small portion of dates are malformed or "future"-dated -- a potential clerical mistake. You must determine how many such records are malformed and decide if it's "safe" to exclude them (e.g. it would likely be fine to exclude a handful of malformed records from a data set with 100,000+ rows).

> Make sure to carefully review the data documentation for potential issues!!

**Will you need to create fields/columns to answer the question?**

For example, perhaps you need to extract a new `year` field from a "datetime" field to perform a yearly analysis.

**Do you need to merge in other data set(s) to address the question or create a visualization?**

For example, you may need to join your data to a [map of San Francisco neighborhoods](https://data.sfgov.org/Geographic-Locations-and-Boundaries/Analysis-Neighborhoods/p5b7-5n3h). Or maybe you need to merge Census socio-economic data to provide key data points for analysis.

### Present story idea

Each group will give a roughly 5 minute presentation on their story idea, the data set(s) they picked, and their plan of attack for executing the project. This is an opportunity to get constructive feedback from classmates and instructors. Be sure to mention potential technical challenges, additional data sets you're trying to hunt down, etc.

### Perform analysis

Manually download the target data set(s) from [DataSF.org][] and save it in your project's `data/raw` directory.

Create a Jupyter notebook in your project's `notebooks/` directory.

Use `pandas` and any other Python libraries necessary to read the data, assess data quality, and perform the analysis addressing your story idea. For example, run descriptive stats on the data, groupby, etc. 

Write narrative in the notebook using [Markdown cells](http://www.firstpythonnotebook.org/markdown/index.html) to explain each code step, why you’re performing it, and the findings.

As mentioned in [notebook details](#notebook-details), you must include at least two data visualizations that explore some facet of the data (simply printing a table does *not* count as a visualization).


### Final presentations

One person from each group presents the story idea and Jupyter notebook analysis. This should include:

- An overview of the story idea
- The data set you chose
- Key findings
- Technical challenges and how you addressed them
- What other analysis you might have performed (given more time)

Group members should all be prepared to answer questions.

## Code setup

Create a [DataKit](../docs/datakit.md) project called `sf-data-project`:

```
cd ~/Desktop/code
$ datakit project create
Creating project from template: /Users/tumgoren/.cookiecutters/cookiecutter-stanford-progj
Select repo_type:
1 - Assignment
2 - Exercise
3 - Project
Choose from 1, 2, 3 (1, 2, 3) [1]: 3
project_number_or_shortname []: SF Data Project
project_name [COMM 177P Project SF Data Project]: SF Data Project
project_short_description [TK]: SF Data Project
repo_root [sf-data-project]:

etc. 
etc.
```

As always, be sure to install dependencies, then save and push your code to GitHub:

```
# Install libraries
cd sf-data-project
pipenv install

# Activate virtual env and push code
pipenv shell
invoke code.push
```

## Reference materials

Check out the [pandas](../docs/python/data_analysis_intro.md#pandas) and [First Python Notebook](../docs/python/data_analysis_intro.md#first-python-notebook) sections of our [data analysis intro](../docs/python/data_analysis_intro.md) class notes for links to documentation, tutorials and cheatsheets than can help along the way (I find it's especially helpful to keep a cheatsheet handy when working with *pandas*).


## Submission

As always, submission is a two-step process.


1. Push your code to GitHub
```
cd ~/Desktop/code/sf-data-project
pipenv shell
invoke code.push
```

1. Submit the GitHub URL for your project via Canvas.
