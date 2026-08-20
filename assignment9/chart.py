"""
Assignment 9 — Task 1: An Interactive Plotly Chart

See the Week 9 assignment page for full instructions. All tasks use Plotly's
built-in gapminder dataset, so no data files are needed.
"""

import plotly.express as px

df = px.data.gapminder()   # columns: country, continent, year, lifeExp, pop, gdpPercap

# 1. Filter the data to a single year (for example, 2007).
# 2. Make an interactive scatter plot of gdpPercap (x) vs lifeExp (y),
#    colored by continent, with the country name in the hover data. Add a title.
# 3. Save it with fig.write_html("gapminder.html", auto_open=True) and confirm
#    it is interactive (hover, zoom).
