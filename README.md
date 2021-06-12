# Web scraping a job-search website

This project automates the task of searching for a job on web portals like **indeed.com** and **linkedin.com** by extracting a list of the companies from the web portal of your choice, based on a specified job title at specified location. The script ```search.py``` displays the extracted list of Companies names directly on your terminal and with the script ```indeed_email.py``` you can send an email to your own GMail account that contains the list of companies having job openings.
To run this program, ensure you have python & pip installed on your system.
Clone this repository using following commands on your terminal/Command prompt:
```
git clone https://github.com/shouryaveer/webscraping-project.git
```
Create a virtual environment in the repository & Install the required packages by running the following commands:
```
cd webscraping-project
python -m venv python_env
source python_env/bin/activate (If on MacOS & Linux)
python_env\Scripts\activate (If on Windows)
pip install -r requirements.txt
```
Now you can either run ```python3 search.py``` which will prompt the user to input a *job title* and *location* & would output a list of companies directly on your terminal. OR You can choose to run ```python3 indeed_email.py``` which will prompt you to sign in to your Gmail account to send an email to yourself after entering the job title & location
