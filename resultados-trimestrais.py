from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from datetime import datetime

def is_good_response(response):
    content_type = response.headers['Content-Type'].lower()
    return (response.status_code == 200 and content_type is not None and content_type.find('html') > -1)

def get_data(url):
    with closing(get(url, stream=False)) as response:
        if is_good_response(response):
            return response.content
        else:
            return None

def get_calendar_data():
    raw_html = get_data('https://www.acionista.com.br/agenda/agenda-e-resultados-das-cias.html')
    html = BeautifulSoup(raw_html, 'html.parser')
    return html.select('table', {'class': 'table ', 'id': 'fevereiro'})

print(datetime.now().isoformat() + ' - START')
fileData = open("resultados-trimestrais.html","w")
fileData.write(str(get_calendar_data()))
print(datetime.now().isoformat() + ' - END')