from bs4 import BeautifulSoup
import requests
import pprint


# had to get this idea dowen on paper first refactoring coming soon
all_data = [] 
more_pages =True
per_page = 200
last_page = 20200

u_input = input('Enter exact Product number ex: Form W-2, Form 1095-C \n')
u_input =  u_input.split(', ')

def seacrh_irs_forms(forms_list):
    forms_list = u_input
    page = 0
    while more_pages:
        
        r = requests.get(f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow={page}&sortColumn=sortOrder&resultsPerPage={per_page}&isDescending=false').text
        soup = BeautifulSoup(r, 'lxml')
        
        for w_2_even in soup.find_all('tr', class_='even'):
            if(w_2_even.find('a').text in forms_list):
                results={
                    'product_number' : str(w_2_even.find('a').text),
                    'form_title' : str(w_2_even.find('td', class_='MiddleCellSpacer').text).strip(),
                    'min_year' : int(w_2_even.find('td', class_='EndCellSpacer').text),
                    'max_year' : 2021
                    }
                all_data.append(results) 
        for w_2_odd in soup.find_all('tr', class_='odd'):
            if(w_2_odd.find('a').text in forms_list):
                results={
                    'product_number' : str(w_2_odd.find('a').text), 
                    'form_title' : str(w_2_odd.find('td', class_='MiddleCellSpacer').text).strip(),
                    'min_year' : int(w_2_odd.find('td', class_='EndCellSpacer').text),
                    'max_year' : 2021
                    }
                all_data.append(results)
                    
        next_page = requests.get(f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?indexOfFirstRow={page}&sortColumn=sortOrder&resultsPerPage={per_page}&isDescending=false').text
        print(page)
        if page == last_page:
            return pprint.pprint(all_data)
            break
        page += 200
seacrh_irs_forms(u_input)