# Web scraping a job-search website

This project automates the task of searching for a job on the website **indeed.com** by extracting a list of the companies that offer a specified job at specified location.
To run this program, ensure you have python & pip installed and then run the following commands in your terminal:
```
git clone https://github.com/shouryaveer/webscraping-project.git
cd webscraping-project
python -m venv python_env
source python_env/bin/activate (If on MacOS & Linux)
python_env\Scripts\activate (If on Windows)
pip install -r requirements.txt
python indeed.py
```
After running the python file 'indeed.py' user will be prompted to input a *job title* and *location* favourable job and with that user input the program would output a list of companies that currently offer the specified job at the specified location.
