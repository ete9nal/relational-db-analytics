# Web Scraping & NoSQL (MongoDB) Sandbox

This repository serves as an integration sandbox to demonstrate web scraping and NoSQL database management using Python.

---

## 📁 Project Components

* **`parsing.py`** — A web scraper built using `requests` and `BeautifulSoup` (with the `lxml` parser). It navigates through the pages of [quotes.toscrape.com](http://quotes.toscrape.com/), extracts quotes, tags, and detailed author biographies, and saves the structured data into `quotes.json` and `authors.json`.
* **`mongodb.py`** — A database management script that connects to a cloud-hosted **MongoDB Atlas** instance using the `pymongo` driver. It demonstrates core CRUD (Create, Read, Update, Delete) operations, including record insertion, advanced document filtering, updating arrays via `$push`, and bulk deletion.

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Web Scraping:** Beautiful Soup 4, Requests, LXML
- **Database:** MongoDB Atlas, PyMongo
- **Data Format:** JSON
