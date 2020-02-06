# Web Scraping for News

- [Overview](#overview)
- [Scraping in Python](#scraping-in-python)
- [Further reading](#further-reading)
- [Choose your own scraping adventure](#choose-your-own-scraping-adventure)

## Overview

Web scraping is the act of automating the acquisition of data or files
(images, videos, documents, etc.) from the web. The data may live on one
or more pages of a website, or perhaps many different websites. The
basic high-level concept is that you're mimicking the actions a human
might take to manually visit the site(s) and extract information.

Why is web scraping a valuable tool for the news? Oftentimes,
journalistically valuable information is locked up on a website that
lacks easier methods for data acquisition (e.g. through downloadable
CSVs, an API or by public records request). Or the website reflects the most
up-to-date or widest scope of information, whereas other resources only
offer outdated or more limited subsets of information.

In such scenarios, web scraping can help capture information that helps
you tell the most accurate and timely story.

ProPublica's [Dollars for Docs](https://projects.propublica.org/docdollars) website is a
great example. Here's a write-up on the [scraping aspect](https://www.propublica.org/nerds/scraping-websites) of the work.

At a technical level, web scraping typically involves extracting
information from the HTML of a website and/or files linked to by the
website, which may in turn be downstream web pages. This process can be
automated by understanding the anatomy of a site -- how pages are
structured, URL patterns, etc. -- and then creating an automated script
that visits the page(s) and extracts target information.

Scraping can be more or less difficult depending on the nature of the
site. A simple site with no dynamic content and predictable URL patterns
could be a quick job, compared to one that uses web forms, randomized
URLs, cookies or sessions, dynamically generated content, password-based
logins, etc.

By definition, web scraping is a brittle activity. Websites move, URL
and page structures evolve, and interactivity gets added or removed.
Further, websites often do *not* reflect the most recent or most
accurate information. Be prepared for your shiny new web scraper to break in the days, months and years ahead. *For these reasons, scraping should be treated as
an option of last resort, after you've evaluated all other options that
might work for your use case*.

Finally, you should always try to scrape "ethically." This means
respecting a site's terms of use, identifying yourself clearly, taking care not to overwhelm a site with large volumes of requests , and a
number of other considerations. [This article](https://dailydatanews.com/2018/01/17/web-scraping/)
lists many of those considerations. Keep in mind that opinions vary
about what is or is not “ethical” -- or legal -- when it comes to
scraping. It's an issue that [has been tested in the courts](https://www.eff.org/deeplinks/2019/09/victory-ruling-hiq-v-linkedin-protects-scraping-public-data)
and will continue to be fought over. *Be mindful of your legal
responsibilities and potential liability when scraping the web.*

## Scraping in Python

The [requests][] and [BeautifulSoup][] are workhorses for basic web scraping.

[requests]: https://2.python-requests.org/en/master/
[BeautifulSoup]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

```
pip install requests bs4
```

A super duper simple scraping example:

```
import bs4, requests
url = "http://www.example.com"
html = requests.get(url).text
soup = BeautifulSoup(html)
soup.find('h1')
```
