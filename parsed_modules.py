import re
import os
import requests

      
def create_pdf(pdf, url):
    for chunk in url.iter_content():
        """
        writing chunk of pdf to file
        """
        if chunk:
            pdf.write(chunk)
            

def user_prompt():
    search_input = input('Enter exact Product number and years ex: Form W-2, 2000, 2020 \n' ).split(', ')
    return search_input

def parse_page(data_parser, form_name,start_year, end_year):
    '''
    Parses pages for form name in range start year and end year and downloads PDF 
    file in new directory when search returns true
    '''
    
    for odd_num in data_parser.find_all('tr', class_='odd'):
        parsed_form = str(odd_num.find('a').text)
        parsed_year = int(odd_num.find('td', class_='EndCellSpacer').text)
        if form_name == parsed_form and parsed_year in range(start_year, end_year+1):
            pdf = odd_num.find('a')
            kwargs = parsed_form.split(" ")
            first = kwargs[0][0].lower()
            second = kwargs[1]
            second = re.sub('[\W_]+', '', second).lower()
            pdf_file = f'https://www.irs.gov/pub/irs-prior/{first}{second}--{parsed_year}.pdf'
            url = requests.get(pdf_file, stream = True)
            path = f"/Users/dross/Desktop/sei/sandbox/pinwheel/{parsed_form}" 
            if not os.path.exists(path):
                os.mkdir(path)
            with open(os.path.join(path, f"{parsed_form} - {parsed_year}.pdf"), 'wb') as pdf:
                create_pdf(pdf,url)
    for w_2_even in data_parser.find_all('tr', class_='even'):
        parsed_form = str(w_2_even.find('a').text)
        parsed_year = int(w_2_even.find('td', class_='EndCellSpacer').text)
        if form_name == parsed_form and parsed_year in range(start_year, end_year+1):
            pdf = w_2_even.find('a')
            kwargs = parsed_form.split(" ")
            first = kwargs[0][0].lower()
            second = kwargs[1]
            second = re.sub('[\W_]+', '', second).lower()
            pdf_file = f'https://www.irs.gov/pub/irs-prior/{first}{second}--{parsed_year}.pdf'
            url = requests.get(pdf_file, stream = True)
            path = f"/Users/dross/Desktop/sei/sandbox/pinwheel/{parsed_form}" # must use your working directory before the variable
            if not os.path.exists(path):
                os.mkdir(path)
            with open(os.path.join(path, f"{parsed_form} - {parsed_year}.pdf"), 'wb') as pdf:
                # download all files
                create_pdf(pdf=pdf, url=url) 
                
            