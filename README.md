# 2026S-SSW564-07

SQLite -> Python -> LaTeX Longtable Pipeline
Python Version: 3.x (uses only standard library)

FILES
- init_db.py
  Creates data.db, creates tables (research_data, requirements), seeds sample data.
- db_queries.py
  Contains fetch_data() (research_data) and fetch_requirements() (requirements).
  Also prints results when run directly.
- generate_requirements_longtable.py
  Queries requirements and writes requirements_longtable.tex (LaTeX longtable).
- data.db
  SQLite database (created after running init_db.py).
- requirements_longtable.tex
  Generated LaTeX longtable output.

HOW TO RUN (from this folder)
1) Initialize database:
   python init_db.py

2) Query data (prints tuples):
   python db_queries.py

3) Generate LaTeX longtable:
   python generate_requirements_longtable.py

LaTeX Usage:
- Add to your LaTeX preamble:
  \usepackage{longtable}

- Put requirements_longtable.tex in the same LaTeX project folder as your main .tex
- Where you want the table:
  \input{requirements_longtable.tex}