# APIs and the News

> *An application programming interface (API) is an interface or communication protocol between different parts of a computer program intended to simplify the implementation and maintenance of software. An API may be for a web-based system, operating system, database system, computer hardware, or software library.* ~ [Wikipedia](https://en.wikipedia.org/wiki/Application_programming_interface)

Put simply, an API provides a way for machines to "speak" to each other. Unlike humans, machines do not fare well with ambiguity. APIs allow machines to communicate in a clear, standardized way.

Below is an example of a software API provided by the Python [requests](https://2.python-requests.org/en/master/) library. The [requests.get](https://github.com/psf/requests/blob/master/requests/api.py#L64) function is an API that allows other code (and of course the human writing the code) to easily obtain a file on the Web by supplying a URL.

```python
import requests
requests.get("http://example.com")
```

These days, we most often hear about APIs in a web context. [Government](https://www.data.gov/developers/apis) [agencies](http://datasf.org/opendata/developers/), [social](https://developers.facebook.com/docs/apis-and-sdks) [media](https://developers.facebook.com/docs/instagram-basic-display-api/) [sites](https://developers.tiktok.com/), [corporations](https://www.lyft.com/developers/products/concierge-api), [news](https://www.propublica.org/datastore/apis) [organizations](https://developer.nytimes.com/docs/articlesearch-product/1/overview) and countless others provide APIs for working with their data and platforms.

Web APIs require machines to exchange information over the Internet. These APIs allow us to ["like" a Tweet](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-favorites-create), [stash data in the cloud](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html), and download [campaign finance information](https://api.open.fec.gov/developers) for a presidential campaign.

APIs are an invaluable resource for newsrooms. These [slides](https://docs.google.com/presentation/d/e/2PACX-1vRol4DL3Rta4xpn2ltzHtQhlgrmlXSnFiewdmA0azxyFS2nPVJ8a-Xxxs5-3MvIGDre0IHygFwlZXYf/pub?start=false&loop=false&delayms=3000) offer some more background on APIs and their relevance to journalism.

<a href="https://docs.google.com/presentation/d/e/2PACX-1vRol4DL3Rta4xpn2ltzHtQhlgrmlXSnFiewdmA0azxyFS2nPVJ8a-Xxxs5-3MvIGDre0IHygFwlZXYf/pub?start=false&loop=false&delayms=3000"><img src="../static/apis_and_news.png" alt="apis and news first slide"></a>
