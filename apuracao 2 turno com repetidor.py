import requests 
import time

url = "https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json"

while 1>0:
    resp = requests.get(url)
    resp = resp.json()

    cand = resp['cand']

    print(f"\n URNAS APURADAS: {resp['pst']} \n")

    print("{:20} {:10} {:10}".format("NOME","VOTOS","VOTOS TOTAL"))

    for candidato in cand:

        print("{:20} {:10} {:10}".format(candidato['nm'],candidato['pvap'],candidato['vap']))

    time.sleep(2)