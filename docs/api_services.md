# API Services

So far we've learned how to use the web as a data source by querying
APIs and scraping websites. Many sites also offer a myriad of *services* via API, which can help us extract or transform information from a
variety of sources such as text, images, audio and video.

A few examples of API-based services:

- [Geocoding](https://developers.google.com/maps/documentation/geocoding/intro)

- [Speech-to-Text transcription](https://cloud.google.com/speech-to-text/)

- [OCR and image detection](https://cloud.google.com/vision/docs/reference/rest/)

- [Entity Extraction/Linking/Concept identification](https://www.refinitiv.com/en/products/intelligent-tagging-text-analytics)

- [Infrastructure](https://docs.aws.amazon.com/index.html#lang/en_us)
     (e.g. spinning up machines in the cloud for data processing or
     storing files)

Such tools are critical for the day-to-day work of journalism. For
example, [DocumentCloud](https://www.documentcloud.org/) uses the [OpenCalais API](http://www.opencalais.com/opencalais-api/) to extract
discrete data -- or entities -- about people, places and organizations
found in uploaded documents. OpenCalais also attempts to [link those entities](https://en.wikipedia.org/wiki/Entity_linking) to canonical records and provide related [concepts or topics for a document](https://en.wikipedia.org/wiki/Concept_mining).

Here's an excerpt from their documentation about the socialTag
information provided by the API:

 *"A Social Tag is an association of the submitted text to related
 Wikipedia categories, or articles. Social tags attempt to emulate how
 a person would tag a specific piece of content. For example, if you
 submit a story about Barak Obama and a piece of legislation, at least
 one reasonable tag would be “U.S. Legislation….The SocialTag function
 does not identify individual items within the text, but rather
 attempts to provide common sense tags for the piece of content as a
 whole. Social tags are derived from the Wikipedia folksonomy. They are
 periodically updated to keep them current."*

Social tags and topics could be used in a document analysis or news app
project to link and discover documents that might otherwise not share
common words or phrases.

## Relevant Reading/Resources

-  [OpenCalais API](https://www.refinitiv.com/en/products/intelligent-tagging-text-analytics) with links
     to demo and API registration

-  [A Practical Approach to Understanding TRIT](https://developers.thomsonreuters.com/article/practical-approach-understanding-and-ingesting-trit-output-your-use-case)


-  [OpenCalais API example](../code/calais_example)
