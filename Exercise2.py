# Installing the OpenAI API
!pip install openai==0.28.1

# Importing the library
import openai
print(openai.__version__)

# Getting the API key
from google.colab import files
from getpass import getpass

chave_api = getpass()

# Setting the API key
openai.api_key = chave_api

# Request

import requests
from bs4 import BeautifulSoup

# Accessing the link of chapter 11
response = requests.get('https://brasileiraspln.com/livro-pln/1a-edicao/parte6/cap11/cap11.html')

# Creating a Beautiful Soup object to parse the HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Storing the paragraphs (main text body)
conteudo = soup.find('div', {'id': 'quarto-content'})

paragrafos = conteudo.find_all('p')

# First part of the text
texto_1 = ''

for p in paragrafos[0:70]:
   texto_1 = texto_1 + p.getText() + '\n'

print(texto_1)

# Extracting the content of the unordered list and addint it to the text
lista_ul = conteudo.find_all('ul')
ul = []

for item in lista_ul:
  ul.append(item.getText())

ul = ul[len(ul)-1]
texto_1 = texto_1 + ul
print(texto_1)

# Extracting the text between the ul and the ol
texto_2 = ''

for p in paragrafos[70:86]:
   texto_2 = texto_2 + p.getText() + '\n'

print(texto_2)

# Extracting the content of the ordered list
lista_ol = conteudo.find_all('ol')
ol = []

for item in lista_ol:
   ol.append(item.getText())

ol = ''.join(map(str, ol[0:len(ol)-1]))
print(ol)

# Extracting the last two paragraphs
texto_3 = ''

for p in paragrafos[86:88]:
   texto_3 = texto_3 + p.getText() + '\n'

print(texto_3)

# Joining the text
texto = texto_1 + texto_2 + ol + texto_3
print(texto)

