# python_homework

This repository holds the local assignments for **Python for Data Analysis**. Most of the course runs in Kaggle notebooks, but a few weeks run Python on your own computer and are submitted from here as pull requests:

* **Week 1** — Advanced Python and Regex (`assignment1/`)
* **Week 6** — Web Scraping with Selenium (`assignment6/`)
* **Week 9** — Interactive Visualization and Dashboards (`assignment9/`)

## Setup

Set this up once, in Week 1.

1. Clone the repository to your computer (your CIL will point you to the exact repository and fork/clone steps).
2. From inside the project folder, create and activate a virtual environment, then install the packages:

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   # .venv\Scripts\activate       # Windows

   pip install -r requirements.txt
   ```

The packages in `requirements.txt` (Pandas, Plotly, Streamlit, Selenium, WebDriver Manager) cover every local week, so you only install once.

## Working on an assignment

For each assignment, create a branch, do your work in that week's folder, and open a pull request:

```bash
git checkout -b assignment1        # or assignment6, assignment9
# ...do your work...
git add .
git commit -m "describe what you did"
git push origin assignment1
```

Then open a pull request on GitHub and submit its link. Commit in small steps as you go.

## Folder guide

| Folder | Week | What it holds |
|---|---|---|
| `assignment1/` | 1 | `assignment1.py` — regex, file paths, and parsing |
| `assignment6/` | 6 | your Selenium scraping mini-project (scraper, cleaned data, README) |
| `assignment9/` | 9 | `streamlit_app.py` and `chart.py` — a Plotly chart and a Streamlit dashboard |

Each folder contains a starter file with the tasks outlined in comments. See the assignment page for each week for full instructions.
