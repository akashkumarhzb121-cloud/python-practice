# Python Data Science Learning

A personal workspace for learning Python and building toward data science. It contains small exercises and examples that can grow as I learn new topics.

## Setup on Windows

Create a virtual environment and install the project dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Using `python -m pip` through the virtual environment works even when `pip` is not available as a standalone PowerShell command.

In VS Code, select `.venv\Scripts\python.exe` as the Python interpreter.

## Data science toolkit

The starter dependencies include:

- **NumPy** for numerical arrays and calculations
- **pandas** for working with tables and datasets
- **Matplotlib** and **Seaborn** for data visualization
- **SciPy** and **Statsmodels** for scientific and statistical methods
- **scikit-learn** for machine learning
- **openpyxl** for reading and writing Excel files
- **JupyterLab** and **ipykernel** for interactive notebooks

## Run an exercise

Run a script from the project root with the virtual environment's Python:

```powershell
.\.venv\Scripts\python.exe .\Array\array.py
```

To start JupyterLab:

```powershell
.\.venv\Scripts\jupyter.exe lab
```

## Learning plan

This repository will evolve with my learning. Topics may include:

- Python fundamentals, functions, and modules
- NumPy and pandas
- Data cleaning, exploration, and visualization
- Statistics and introductory machine learning
- Practice projects and notes

Exercises and projects are added as I work through each topic. Add any new third-party packages to `requirements.txt` so they can be reinstalled with the setup command above.
