# ThriftCart Net Sales Scraper

## What is it?

It logs into Thriftcart, generates a sales report for the previous month, scrapes the net sales value, then appends it into a CSV file with the date

## Why?

I wanted the organization I work for to have easy access to our monthly sales figures as well as have an ongoing record of them. I wanted this done automatically.

## How to use this

- Install Python3
- Install mechanicalsoup `pip install mechanicalsoup`
- Add your Thriftcart URL, a username, and a password to `main.py`
  - I would suggest creating a username specifically for the script to use, and only give that username access to reports
- Redirect your sales file to a preferred directory.
- Use your favorite job scheduler to schedule `main.py` to run every month. I use anacron.
  - Alternatively, you can run `main.py` daily (maybe at startup). It will check to make sure it doesn't pull duplicate information, and it won't log into thriftcart if it doesn't need to do so.
