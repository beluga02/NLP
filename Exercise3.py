# Grammar correction

# Configuring the endpoint chat completions of API

import requests
endpoint = "https://api.openai.com/v1/chat/completions"

mensagem_sistema = 'Você deverá identificar um caracter de espaço empregado incorretamente no trecho abaixo e retornar o texto corrigido.'
mensagem_usuario = "proposta por Cristea; Ide; Romary (1998) , que sugere o estabelecimento de domínios referenciais de acessibilidade para cada unidade discursiva"

parametros = {
   "model": "gpt-3.5-turbo-0613",
   "messages": [
      {"role": "system", "content": mensagem_sistema},
      {"role": "user", "content": mensagem_usuario}],
  "max_tokens": 100
}

headers = {
   "Content-Type": "application/json",
   "Authorization": f"Bearer {openai.api_key}"
}

resposta = requests.post(endpoint, json=parametros, headers=headers)
print(resposta.json()["choices"][0]["message"]["content"])

mensagem_sistema = 'Você deverá identificar um trecho do texto abaixo em que está faltando um caracter de espaço e retornar o texto corrigido.'
mensagem_usuario = """Percebe-se que as escolhas dos participantes podem variar desde a seleção da estrutura sintática (como em (4d) e (5d)
que usam estruturas diferentes para tratar sobre o fato de a loja estar fechada)em até a escolha de expressões referenciais (como o uso de “a loja”, em (4b) e “esta” em (5b) ao tratar do mesmo referente)."""

parametros = {
   "model": "gpt-3.5-turbo-0613",
   "messages": [
      {"role": "system", "content": mensagem_sistema},
      {"role": "user", "content": mensagem_usuario}],
  "max_tokens": 100
}

headers = {
   "Content-Type": "application/json",
   "Authorization": f"Bearer {openai.api_key}"
}

resposta = requests.post(endpoint, json=parametros, headers=headers)
print(resposta.json()["choices"][0]["message"]["content"])

mensagem_sistema = 'Você deverá identificar erros de ortografia no texto abaixo e retornar o texto corrigido.'
mensagem_usuario = "ou ainda caracterizar o discuso como um processo"

parametros = {
   "model": "gpt-3.5-turbo-0613",
   "messages": [
      {"role": "system", "content": mensagem_sistema},
      {"role": "user", "content": mensagem_usuario}],
  "max_tokens": 100
}

headers = {
   "Content-Type": "application/json",
   "Authorization": f"Bearer {openai.api_key}"
}

resposta = requests.post(endpoint, json=parametros, headers=headers)
print(resposta.json()["choices"][0]["message"]["content"])

# Recognizing Named Entities

mensagem_sistema = 'Você receberá uma frase e deverá identificar as entidades nomeadas presentes nela. Para cada entidade nomeada, identifique se é um nome comum ou um nome próprio.'

# Example from the book
mensagem_usuario = "João foi a sua loja de música favorita para comprar um piano."

parametros = {
   "model": "gpt-3.5-turbo-0613",
   "messages": [
      {"role": "system", "content": mensagem_sistema},
      {"role": "user", "content": mensagem_usuario}],
  "max_tokens": 100
}

headers = {
   "Content-Type": "application/json",
   "Authorization": f"Bearer {openai.api_key}"
}

resposta = requests.post(endpoint, json=parametros, headers=headers)
print(resposta.json()["choices"][0]["message"]["content"])

mensagem_usuario = """A empresa Produtos Pirata Indústria e Comércio Ltda., de Contagem (na região metropolitana de Belo Horizonte),
deverá registrar este ano um crescimento de produtividade nas suas áreas comercial e industrial de 11% e 17%, respectivamente."""

parametros = {
   "model": "gpt-3.5-turbo-0613",
   "messages": [
      {"role": "system", "content": mensagem_sistema},
      {"role": "user", "content": mensagem_usuario}],
  "max_tokens": 100
}

headers = {
   "Content-Type": "application/json",
   "Authorization": f"Bearer {openai.api_key}"
}

resposta = requests.post(endpoint, json=parametros, headers=headers)
print(resposta.json()["choices"][0]["message"]["content"])

mensagem_usuario = "Todos morreram quando o avião, prejudicado pelo mau tempo, não conseguiu chegar à pista de aterrissagem e caiu numa floresta a 15 Km do aeroporto de Bukavu."

parametros = {
   "model": "gpt-3.5-turbo-0613",
   "messages": [
      {"role": "system", "content": mensagem_sistema},
      {"role": "user", "content": mensagem_usuario}],
  "max_tokens": 100
}

headers = {
   "Content-Type": "application/json",
   "Authorization": f"Bearer {openai.api_key}"
}

resposta = requests.post(endpoint, json=parametros, headers=headers)
print(resposta.json()["choices"][0]["message"]["content"])

