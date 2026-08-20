"""
Assignment 1 — Advanced Python and Regex

Complete each task below. See the Week 1 assignment page for full instructions.
Mark each task with a comment (as shown), and print your results.
"""

import re
from pathlib import Path


# --- Task 1: Regular Expressions ---
# 1. From "Order 1234 shipped, invoice 56789, ref 42", use re.findall to extract
#    all the numbers as a list.
# 2. From "(212) 555-1234", use re.sub to remove every non-digit character.
# 3. From "Date: 2021-05-01", use a pattern with capture groups and re.search to
#    extract the year, month, and day separately, and print all three.


# --- Task 2: File Paths ---
# 1. Build a path to data/sales.csv with the / operator and print its
#    .name, .stem, .suffix, and .parent.
# 2. Create two text files (data/a.txt and data/b.txt), then use glob to list
#    every .txt file in the data folder and print each file's name.


# --- Task 3: Parsing Messy Data ---
raw = """
Alice, 30, New York
Bob, 25, Los Angeles
--- corrupted line ---
Carlos, 41, Chicago
"""
# 1. Using a regular expression, parse each VALID line into a dict with keys
#    name, age (as an int), and city. Collect them in a list. Skip malformed
#    lines, printing a message for each one you skip.
# 2. Build a dict comprehension mapping each name to its city.
# 3. Use sorted() with a lambda to order the records from oldest to youngest.
# 4. Print the list of records, the name-to-city dict, and the sorted records.
