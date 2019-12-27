# YouuuuRL - A URL Shortener

The goal of this is to be able to map a long sequence of characters (long url) into a short, 6-digit url.
Furthermore, we should be able to derive the long sequence (original url) from the shortened one.

Thus, a `bijective` function is needed to be able to go both ways.

## Candidate Solutions

* Hashing
* Base Conversion

My first thoughts were to attempt to use hashing to map each lengthy URL to a shorter URL. However, upon a little more thought, I realized that because there are so many URLs that could be cached into the system, it would be possible for collisions to occur, rendering this project completely useless. After performing a quick dive into the logic of most URL-compressors, I discovered that a very good approach to this would be to use Base Conversion.

### Base Conversion (Base 62)

Instead of using a bijective function to map between the shortened URL and the original, lengthy URL, a better alternative would be to first save the URL inside of a database with a certain unique number associated with it. This could be the row number (if using a relational database with tables), or just a randomly-generated UUID for non-relational databases. Using the row number, one would be able to quickly access the URL corresponding to it.

So on one hand, we have the **domain**, consisting of a random `n-digit` number. The codomain, on the other hand, would be the code converted into base 62. Here are some of the reasons why this base was chosen:

* There are 62 symbols that could be in the shortened code (numbers from 0-9, lower-case letters from a-z, and upper-case letters from A-Z). Thus, we can map each numerical value 0 to 61 to one of these symbols.
* This allows for several URLs to be stored. Since the code will be 6-digits and each digit will have 62 different possibilities, then we have a total of 62^6 possibilities AKA 62^6 possible URLs to be stored.

## Implementation

Here are some brief details describing the implementation of this project.

### Tech Stack

* Language: A LOT of Python and some SQL.
* Framework: Flask, a lightweight server-side framework for Python.
* Server-side: NGINX and UWSGI to follow proper server-side architecture.
* Containerization: Docker-compose to orchestrate several Docker containers together.
* Database: PostgreSQL, a common relational database.

### System Design/Architecture

[INSERT IMAGE HERE]

### Data Flow




## Endpoints

### Shorten URL

`/v1/shorten`

### Lengthen URL

`/v1/lengthen`

