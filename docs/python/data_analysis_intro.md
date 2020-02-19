#  Data Analysis with Jupyter and pandas

- [Jupyter Notebooks](#jupyter-notebooks)
- [Jupyter use cases](#jupyter-use-cases)
- [pandas](#pandas)
- [First Python Notebook](#first-python-notebook)

## Jupyter Notebooks 

The [Jupyter](https://jupyter.org/) notebook is an interactive coding environment especially well-suited for data analysis. It provides a browser-based interface that is much more user-friendly than the Python interactive interpreter.

The ability to blend narrative with code and visualizations has made Jupyter notebooks an increasingly popular tool among data journalists. With Jupyter, it's a cinch to create readable, reproducible data analyses that can be shared with fellow reporters, editors or the public.

Jupyter typically runs on a local web server, although a number of platforms and services allow you to view notebooks online and even work with Jupyter without having to install anything.

* [Binder](https://mybinder.org/)
* [Github](https://help.github.com/en/github/managing-files-in-a-repository/working-with-jupyter-notebook-files-on-github)
* [Google Colab](https://colab.research.google.com/)
* [Kaggle](https://www.kaggle.com/docs/kernels#notebooks)
* [nbviewer](https://nbviewer.jupyter.org/)


A growing number of newsrooms use Jupyter notebooks to collaborate internally, as well as share their work with the public. The Los Angeles Times Data Desk uses Jupyter to tell data-driven stories such as this [analysis of California homes within fire zones][].

Better yet, LAT journalists [share their analyses](https://github.com/datadesk/notebooks) with the world, as does [BuzzFeed News](https://github.com/BuzzFeedNews?language=jupyter+notebook).

[analysis of California homes within fire zones]: https://www.latimes.com/projects/la-me-california-buildings-in-fire-zones/

## Jupyter use cases

Jupyter is often used for all steps in a data project, from data acquisition through analysis and visualization.

A Jupyter-only workflow can be especially helpful on projects with relatively small data sets. By performing all data work in Jupyter, you can minimize context switching and technical overhead.

However, complex or time-consuming data acquisition processes are not always a great fit for Jupyter. For example, a traditional Python script or [data pipeline](data_pipelines_with_modules.md) is arguably more appropriate for a complex web scraper that runs hourly and feeds an "evergreen" database. Of course, the data produced by such a script is always accessible to a Jupyter notebook.

It's worth noting that it *is* possible to run heavy web scrapes in a Jupyter notebook. It's even possible to [run a Jupyter notebook on the command line](https://nbconvert.readthedocs.io/en/latest/usage.html#convert-notebook), similar to a standard Python script.

For this course, however, we'll decouple "expensive" data acquisition steps from Jupyter in order to keep notebooks light-weight and focused on data wrangling and analysis.

## pandas

The [pandas][] library is the workhorse of data wrangling and analysis in Python. It provides a wide range of functionality for common data tasks such as filtering, joining, and aggregating data.

pandas is a big library and its [official documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html#user-guide) can be a bit intimidating for beginners.

Below are a few resources that can help level up on [pandas][]:

- [First Python Notebook](#first-python-notebook)
- [Kaggle pandas tutorial](https://www.kaggle.com/learn/pandas)
- [10 Minutes to pandas](http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)
- Pandas cheat sheets (print these\! They're awesome\!)
   -  [basics cheat sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PandasPythonForDataScience.pdf)
    -  [data wrangling](https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf)

## First Python Notebook

The [First Python Notebook](http://www.firstpythonnotebook.org/) tutorial, created by data journalist Ben Welsh of The Los Angeles Times, is an excellent gentle introduction to Jupyter and pandas. In addition to introducing key features of Jupyter, it walks through basic pandas skills using California campaign finance data.

It's worth taking the time to work through the entire tutorial.

Below are links to key sections in case you've moved on to your own project and need a quick refresher on particular skills.

  - [Reading data](http://www.firstpythonnotebook.org/dataframe/index.html#creating-a-dataframe)
  - [DataFrame helpers](http://www.firstpythonnotebook.org/dataframe/index.html) (head, info, etc.)
  - [Columns](http://www.firstpythonnotebook.org/value_counts/index.html#)
  - [Filtering](http://www.firstpythonnotebook.org/filter/index.html)
  - [Merging](http://www.firstpythonnotebook.org/merge/index.html)
  -  [Summing](http://www.firstpythonnotebook.org/totals/index.html) and [descriptive
     stats](http://www.firstpythonnotebook.org/pandas/index.html#conduct-a-simple-data-analysis)
     (min, max, median, describe, etc.)
  - [Sorting](http://www.firstpythonnotebook.org/sort_values/index.html)
  - [Groupby](http://www.firstpythonnotebook.org/groupby/index.html)
  - [Charts](http://www.firstpythonnotebook.org/charts/index.html)
  - [Narrative](http://www.firstpythonnotebook.org/markdown/index.html)
    (markdown)


[pandas]: https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html#user-guide


