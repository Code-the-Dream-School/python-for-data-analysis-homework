"""
Assignment 6 — Web Scraping Mini-Project

Build a small, complete scraping project. See the Week 6 assignment page for full
instructions. If you don't have a site in mind, use the recommended practice site:
http://books.toscrape.com/

Steps (each is described on the assignment page):
  1. Choose a site and confirm robots.txt and terms of service permit scraping
     (document this in a README.md in this folder).
  2. Inspect the page to find the elements holding your target fields.
  3. Scrape at least 50 records into a list of dicts. Handle missing fields with
     try/except, and sleep() between pages so you scrape responsibly.
  4. Clean the data with pandas (types, missing values, duplicates).
  5. Save the cleaned data to CSV and to a SQLite database.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

# Your scraper goes here.
