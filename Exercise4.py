# Questions and Answers

mensagem_sistema = """Você é um professor de PLN e está elaborando questões para uma prova a partir de um livro sobre a disciplina.
Com base em cada trecho dado, retorne três perguntas e suas respectivas respostas."""
mensagem_usuario = """A teoria de Grosz; Sidner (1986), conhecida como GSDT (Grosz and Sidner Discourse Theory),
visa modelar o aspecto intencional do discurso. Parte-se da ideia de que o autor de um texto possui uma ou mais
intenções e estrutura seu conteúdo de forma a satisfazê-las. Identificar as intenções do autor é crucial para
compreender a mensagem pretendida. Como as intenções potenciais em um discurso são praticamente ilimitadas,
a GSDT organiza-o usando relações de contribuição e satisfação entre as intenções. Essas relações são em número
finito e limitadas a dois tipos: a intenção primária do discurso e as intenções subjacentes aos segmentos do discurso.
Define-se, nesta teoria, as seguintes relações: Dominance, Satisfaction-Precedence, Supports e Generates.
A relação Dominance ocorre quando a intenção subjacente a um segmento A contribui para a intenção subjacente de um
segmento B, isto é, A dominates B, representado por (DOM(A,B)). A relação Satisfaction-Precedence ocorre quando a
intenção subjacente a um segmento A deve ser satisfeita antes da intenção subjacente a um segmento B, isto é, SP(A,B).
As relações Supports e Generates ocorrem entre o conteúdo dos segmentos. A primeira acontece se a aceitação de um segmento B
fornece subsídios para a aceitação do segmento A, então se diz que o conteúdo de B supports A (SUP(A,B)). A segunda ocorre
se a ação descrita em B contribui para a ação descrita em um segmento A (GEN(B,A))."""

parametros = {
   "model": "gpt-3.5-turbo-0613",
   "messages": [
      {"role": "system", "content": mensagem_sistema},
      {"role": "user", "content": mensagem_usuario}]
}

headers = {
   "Content-Type": "application/json",
   "Authorization": f"Bearer {openai.api_key}"
}

resposta = requests.post(endpoint, json=parametros, headers=headers)
print(resposta.json()["choices"][0]["message"]["content"])

mensagem_usuario = """A Teoria de Centering (Grosz; Joshi; Weinstein, 1995), foca nas relações existentes entre anáforas e
visa estabelecer a coerência nos segmentos discursivos adjacentes ao direcionar a atenção para a escolha de uma expressão
referencial (discurso local). O principal objetivo da teoria é prever qual entidade discursiva tem maior importância em
determinados segmentos, definindo um conjunto de regras e restrições que ditam as escolhas feitas pelos participantes
do discurso, em que a Teoria de Centering fornece meios para tratar essas diferenças."""

parametros = {
   "model": "gpt-3.5-turbo-0613",
   "messages": [
      {"role": "system", "content": mensagem_sistema},
      {"role": "user", "content": mensagem_usuario}]
}

headers = {
   "Content-Type": "application/json",
   "Authorization": f"Bearer {openai.api_key}"
}

resposta = requests.post(endpoint, json=parametros, headers=headers)
print(resposta.json()["choices"][0]["message"]["content"])

mensagem_usuario = """A Rhetorical Structure Theory (RST) é uma teoria linguístico-descritiva que trata da organização do texto utilizando
relações retóricas (também nomeadas relações de coerência ou discurso) que existem entre os segmentos discursivos, formando uma estrutura
discursiva totalmente conectada, geralmente na forma de árvore (Mann; Thompson, 1988). A RST explica a coerência postulando uma estrutura
hierárquica e conectada, na qual cada parte de um texto tem uma função a cumprir, com relação às outras partes do texto.
Cada proposição é associada a um núcleo (informação principal) ou satélite (informação adicional) de uma relação retórica.
Em casos padrões, as relações se estabelecem entre duas proposições, expressas por segmentos adjacentes no texto. Quando a
relação conecta um núcleo e um satélite, ela é chamada de mononuclear. Por outro lado, se a relação conectar somente núcleos,
ela é chamada de multinuclear."""

parametros = {
   "model": "gpt-3.5-turbo-0613",
   "messages": [
      {"role": "system", "content": mensagem_sistema},
      {"role": "user", "content": mensagem_usuario}]
}

headers = {
   "Content-Type": "application/json",
   "Authorization": f"Bearer {openai.api_key}"
}

resposta = requests.post(endpoint, json=parametros, headers=headers)
print(resposta.json()["choices"][0]["message"]["content"])

# Summarizing

mensagem_sistema = """Resuma com suas próprias palavras as principais ideias do texto abaixo em quatro frases."""
mensagem_usuario = """Sabe-se que o desenvolvimento de tecnologias sofisticadas tem substituído a reflexão e supervisão linguísticas por
modelos estatísticos, com métodos não compreensíveis para os seres humanos. No entanto, conforme aponta Freitas (2022),
o conhecimento linguístico para o PLN não ficará obsoleto por diversos motivos, entre os quais a autora destaca quatro:
i. nem todo conhecimento em PLN é voltado para aplicações da indústria, portanto, há pesquisas linguísticas que dependem desse c
onhecimento para o desenvolvimento de aplicações linguísticas (materiais lexicográficos, didáticos, corretores gramaticais etc.);
ii. continua sendo necessária ao menos uma amostra do conhecimento humano para as tarefas em PLN, como na construção de datasets, em
versões iniciais de sistemas e na avaliação do desempenho da máquina;
iii. é elevado o custo (computacional, financeiro e ambiental) das atividades desenvolvidas com base nos métodos estatísticos, por isso,
informações linguísticas possibilitam a economia no processamento em comparação com o uso de dados brutos; e
iv. desde uma perspectiva filosófica, haver apenas a eficácia – sem compreensão, nem explicação – dos sistemas não é o suficiente,
pois a ciência se baseia no paradigma da verdade."""

parametros = {
   "model": "gpt-3.5-turbo-0613",
   "messages": [
      {"role": "system", "content": mensagem_sistema},
      {"role": "user", "content": mensagem_usuario}]
}

headers = {
   "Content-Type": "application/json",
   "Authorization": f"Bearer {openai.api_key}"
}

resposta = requests.post(endpoint, json=parametros, headers=headers)
print(resposta.json()["choices"][0]["message"]["content"])

frases = resposta.json()["choices"][0]["message"]["content"].split(".")

for frase in frases[:-1]:
  print(f'{frase}.')
