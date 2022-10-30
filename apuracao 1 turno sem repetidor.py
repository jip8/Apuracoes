
import requests
import json
import pandas as pd

data = requests.get(
    'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json'
)
json_data=json.loads(data.content)

candidato = []
pertido = []
votos = []
porcentagem = []
for informacoes in json_data['cand']:

    if informacoes['seq'] == '1' or informacoes['seq'] == '2' or informacoes['seq'] == '3' or informacoes['seq'] == '4' or informacoes['seq'] == '5' or informacoes['seq'] == '6' or informacoes['seq'] == '7' or informacoes['seq'] == '8' or informacoes['seq'] == '9' or informacoes['seq'] == '10' or informacoes['seq'] == '11':
        candidato.append(informacoes['nm'])
        votos.append(informacoes['vap'])
        porcentagem.append(informacoes['pvap'])

df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=[
    'Candidato', 'N° Votos', 'Porcentagem'])
print(df_eleicao)