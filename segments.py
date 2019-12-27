from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime

def is_good_response(response):
    content_type = response.headers["Content-Type"].lower()
    return (response.status_code == 200 
            and content_type is not None
            and content_type.find("html") > -1)

def get_data(url):
    with closing(get(url, stream=False)) as response:
        if (is_good_response(response)):
            return response.content
        else:
            return None

class Segment:
    code = None
    name = None
    html = None

def get_segment_data(segment_code):
    raw_html = get_data('http://www.fundamentus.com.br/resultado.php?setor={0}'.format(segment_code))
    html = BeautifulSoup(raw_html, "html.parser")
    return html.find('table', {'id': 'resultado'})

# segment_codes = [42,33,15,16,27,12,20,28,13,26,6,32,9,39,35,17,34,40,24,5,10,7,8,23,2,41,1,38,18,29,4,19,36,11,37,3,21,30,31,14,22,25]
segments = [{'id': 42, 'name': 'Agropecuária', 'html': None },
{'id': 33, 'name': 'Água e Saneamento', 'html': None }, 
{'id': 15, 'name': 'Alimentos', 'html': None }, 
{'id': 16, 'name': 'Bebidas', 'html': None }, 
{'id': 27, 'name': 'Comércio', 'html': None }, 
{'id': 12, 'name': 'Comércio', 'html': None }, 
{'id': 20, 'name': 'Comércio e Distribuição', 'html': None }, 
{'id': 28, 'name': 'Computadores e Equipamentos', 'html': None }, 
{'id': 13, 'name': 'Construção e Engenharia', 'html': None }, 
{'id': 26, 'name': 'Diversos', 'html': None }, 
{'id': 6, 'name': 'Embalagens', 'html': None }, 
{'id': 32, 'name': 'Energia Elétrica', 'html': None }, 
{'id': 9, 'name': 'Equipamentos Elétricos', 'html': None }, 
{'id': 39, 'name': 'Exploração de Imóveis', 'html': None }, 
{'id': 35, 'name': 'Financeiros', 'html': None }, 
{'id': 17, 'name': 'Fumo', 'html': None }, 
{'id': 34, 'name': 'Gás', 'html': None }, 
{'id': 40, 'name': 'Holdings Diversificadas', 'html': None }, 
{'id': 24, 'name': 'Hoteis e Restaurantes', 'html': None }, 
{'id': 5, 'name': 'Madeira e Papel', 'html': None }, 
{'id': 10, 'name': 'Máquinas e Equipamentos', 'html': None }, 
{'id': 7, 'name': 'Materiais Diversos', 'html': None }, 
{'id': 8, 'name': 'Material de Transporte', 'html': None }, 
{'id': 23, 'name': 'Mídia', 'html': None }, 
{'id': 2, 'name': 'Mineração', 'html': None }, 
{'id': 41, 'name': 'Outros', 'html': None }, 
{'id': 1, 'name': 'Petróleo, Gás e Biocombustíveis', 'html': None }, 
{'id': 38, 'name': 'Previdência e Seguros', 'html': None }, 
{'id': 18, 'name': 'Prods. de Uso Pessoal e de Limpeza', 'html': None }, 
{'id': 29, 'name': 'Programas e Serviços', 'html': None }, 
{'id': 4, 'name': 'Químicos ', 'html': None }, 
{'id': 19, 'name': 'Saúde', 'html': None }, 
{'id': 36, 'name': 'Securitizadoras de Recebíveis', 'html': None }, 
{'id': 11, 'name': 'Serviços', 'html': None }, 
{'id': 37, 'name': 'Serviços Financeiros Diversos', 'html': None }, 
{'id': 3, 'name': 'Siderurgia e Metalurgia', 'html': None }, 
{'id': 21, 'name': 'Tecidos, Vestuário e Calçados', 'html': None }, 
{'id': 30, 'name': 'Telefonia Fixa', 'html': None }, 
{'id': 31, 'name': 'Telefonia Móvel', 'html': None }, 
{'id': 14, 'name': 'Transporte', 'html': None }, 
{'id': 22, 'name': 'Utilidades Domésticas', 'html': None }, 
{'id': 25, 'name': 'Viagens e Lazer', 'html': None }]

fileData = open("fundamentus-setores.html","w")

for segment in segments:
    sleep(4)
    print('setor: ' + str(segment['name']))

    segment['html'] = get_segment_data(segment['id'])
    # fileData.write(str(segment['name']) + str(segment['id']))
    data = str(segment['html'])
    data = data.replace("</tr>", "<td>" + segment['name'] + "</td></tr>")
    fileData.write(data)    

fileData.close()
    

    