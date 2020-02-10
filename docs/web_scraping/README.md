# Web Scraping for the News

- [Overview](#overview)
- [Value of scraping](#value-of-scraping)
- [Scraping mechanics and challenges](#scraping-mechanics-and-challenges)
- [The option of last resort](#the-option-of-last-resort)
- [Ethical scraping](#ethical-scraping)
- [Python example](#python-example)
- [More resources](#more-resources)

## Overview

Web scraping is the act of automating the acquisition of data or files
(images, videos, documents, etc.) from the web. The data may live on one or more pages of a website, or perhaps many different websites. At root, web scraping involves writing code to mimic the actions a human
might take to visit a site in a web browser and manually extract information.

## Value of scraping

Why is web scraping a valuable tool for the news? 

Often, journalistically valuable information is locked up on a website that lacks easier methods for data acquisition. Not all government agencies, for example, offer downloadable CSVs or APIs. Nor do they always respond to public records requests in a timely or helpful manner.

Web scraping allows journalists to acquire information in the face of technical or bureaucratic hurdles.

Scraping is also useful in scenarios where a website offers the most up-to-date or widest scope of information. In such cases, web scraping can help journalists tell a more accurate and timely story.

Here are a few examples where web scraping helped produce news:

* [Accidential shootings involving kids often go unpunished](https://apnews.com/068e01df18184c9a89cd525331020c91), by The Associated Press, relied on data scraped from the [Gun Violence Archive](https://www.gunviolencearchive.org/).
* [Amazon Says It Puts Customers First. But Its Pricing Algorithm Doesn't](https://www.propublica.org/article/amazon-says-it-puts-customers-first-but-its-pricing-algorithm-doesnt), by ProPublica. Here's the [behind-the-scenes look](https://www.propublica.org/article/how-we-analyzed-amazons-shopping-algorithm) at how they scraped and analyzed Amazon data.
* [Dollars for Docs](https://projects.propublica.org/docdollars), a searchable news app by ProPublica. Here's a write-up on the [scraping aspect](https://www.propublica.org/nerds/scraping-websites) of the work.


## Scraping mechanics and challenges

On a technical level, web scraping typically involves extracting
information from the HTML of a website and/or files linked to by the
website, which may in turn be downstream web pages. This process can be
automated by [understanding the anatomy of a site](101.md#dissecting-a-web-site) -- how pages are
structured, URL patterns, etc. -- and then creating a script
that retrieves (or visits) web pages and extracts the target information.

Scraping can be more or less difficult depending on the nature of the
site. A simple site with no dynamic content and predictable URL patterns could be a quick job, compared to one that uses web forms, randomized URLs, cookies or sessions, dynamically generated content, password-based logins, etc. Sites often use a combination of these strategies, so it's important to spend time learning how a site works and choose an appropriate [scraping strategy](101.md#scraping-strategies).

## The option of last resort

Web scraping is a brittle activity. Sites move, URL
and page structures evolve, interactivity gets added or removed.

Shiny new web scrapers inevitably break in the days, months and years after they were written.

Further, websites often do *not* reflect the most recent or most
accurate information. 

For these reasons, scraping should be treated as an option of last resort. When a government website does not offer easy methods for obtaining data, journalists typically reach out to the agency and possibly file public records requests to obtain structured data or digital files. They seek to exhaust easier options before turning to their scraping toolkit. 

## Ethical scraping

Scraping ethically implies a number of best practices. To mention a few:

* Respecting a site's terms of use
* Identifying yourself clearly
* Taking care not to overwhelm a site with large volumes of requests

Here are a few articles that lay out ethical concerns in more detail:

* [On the Ethics of Web Scraping and Data Journalism](https://gijn.org/2015/08/12/on-the-ethics-of-web-scraping-and-data-journalism/)
* [Ethics in Web Scraping](https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01)

Keep in mind that opinions vary about what is or is not "ethical" -- or legal -- when it comes to scraping. It's an issue that [has been tested in the courts](https://www.eff.org/deeplinks/2019/09/victory-ruling-hiq-v-linkedin-protects-scraping-public-data) and will continue to be fought over.

*Be mindful of your legal responsibilities and potential liability when scraping the web.*

## Python example

The [requests][] and [BeautifulSoup][] libraries are workhorses of basic web scraping in Python.

[requests]: https://2.python-requests.org/en/master/
[BeautifulSoup]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

```
pip install requests bs4
```

A super simple scraping example that extracts the text of the `h1` HTML tag on <http://example.com>.

```
import bs4, requests
url = "http://www.example.com"
html = requests.get(url).text
soup = bs4.BeautifulSoup(html)
h1 = soup.find('h1')
print(h1.text)
```

## More resources

- [Web scraping exercises](exercises.md) - A few sites to challenge your scraping skills.
- [Web scraping resources](resources.md) - Tutorials, key concepts, code libraries for scraping, etc.