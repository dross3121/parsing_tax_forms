from bs4 import BeautifulSoup
import urllib
import requests
from parsed_modules import parse_page, user_prompt, create_pdf, next_page
import re
import os


more_pages =True
per_page = 200
last_page = 20200



def search_by_name_date(search):
    page = 0
    current_form = search[0]
    start_year= int(search[1])
    end_year = int(search[2])
    while more_pages:
        # code refactored into modules
        r = requests.get(f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow={page}&sortColumn=sortOrder&resultsPerPage={per_page}&isDescending=false').text
        soup = BeautifulSoup(r, 'lxml')
        parse_page(data_parser=soup, form_name=current_form, start_year=start_year, end_year=end_year)
        next_page = requests.get(f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow={page}&sortColumn=sortOrder&resultsPerPage={per_page}&isDescending=false').text
        if page == last_page:
            break
        page += 200
        # need to findout when i have reach the last page
search_by_name_date(user_prompt())
