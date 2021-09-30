## Usage
- created tools to take user input and return tax docs for the user input 
- user can search mutiple different forms in one request
- user can search forms in a range of year ex: 2010 -2020 inclusive
- user seacrh will return a pdf verison of the form requested is a sub- directory of current directory

## Tech used
- Python 3.9.6
- Beautifulsoup for web-scraping

## pip insatll -r requirements.txt

- Run scripts calling "python utility1.py" "python utility2.py"
- Both scripts take users input via the CLI you'll be prompted on how to input search parameter 

-script "utility1.py" outputs JSON to the CLI

- for lines 37 and 60 in "utility2.py" you must use you current working path before {parsed_form}
run pwd in you command line to print working path
ex: /Users/dross/Desktop/sei/sandbox/pinwheel/
Author: Deshawn Ross

