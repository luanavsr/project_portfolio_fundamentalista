import numpy as np
import pandas as pd
import string
import requests
import lxml

# Importando dados fundamentalistas
url_fund =('https://www.fundamentus.com.br/resultado.php')

header = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"  
 }

request_fund = requests.get(url, headers=header)

fundamentos = pd.read_html(r.text,  decimal=',', thousands='.')[0]


# Empresas participantes do IBOV
url_b3 = ('http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraQuadrimestre.aspx?Indice=IBOV&idioma=pt-br')
request_b3 = requests.get(url_b3, headers=header)

ibov =  pd.read_html(request_b3.text,  decimal=',', thousands='.')[0]
ibov['Código']

