import pandas as pd
import requests
import json
import string
import time
import os



def extract_info(CPA="A1425EZG"):
    contenido = (requests.get("https://codigo-postal.co/argentina/cpa/{}/".format(CPA))).text
    text_breaker = "El CPA {} pertenece".format(CPA)
    if text_breaker in contenido:
        result = text_breaker+contenido.split(text_breaker)[1].split("</p>")[0]
    else:
        result = ""
    return result

def outer_product(list1, list2):
    result_list = [str1+str2 for str2 in list2 for str1 in list1]
    return result_list

with open("data/statesCode.json", "r") as o_file:
    states_codes = json.load(o_file)
states_codes = {key.title(): val for key, val in states_codes.items()}
del states_codes['Ciudad Autonoma De Buenos Aires']
states_codes['Capital Federal'] = 'C'
states_codes = pd.DataFrame(states_codes.items(), columns=['Provincia', 'Letra'])

with open("data/localities.csv", "r") as o_file:
    localidades = pd.read_csv(o_file)
CPs = localidades[['CP', 'Provincia']].drop_duplicates()#.unique()#.tolist()

merged_info = pd.merge(CPs, states_codes,
         how = 'inner', on = 'Provincia')
merged_info['CPA_inicial']= merged_info.apply(lambda row: row['Letra']+str(row['CP']), axis=1)
CPA_inicial= merged_info['CPA_inicial'].drop_duplicates().to_list()

alphabet = list(string.ascii_uppercase)

print("Construyendo todos los posibles CPAs")

CPA_final = outer_product(outer_product(alphabet,alphabet), alphabet)

CPAs = outer_product(CPA_inicial,CPA_final)

os.remove('resultado.csv')
results = open('resultado.csv', 'a')

inicial = time.time()
n=1

n_limite = input("Cantidad de consultas que desea realizar: ")
while True:
    try:
        n_limite = int(n_limite)
        if n_limite > 0:
            break
        else:
            print("Necesitamos un número > 0.")
    except ValueError:
        print("Debe insertar un número")




for CPA in CPAs:
    text = extract_info(CPA)
    if text != '':
        results.write(text+"\n")

    print("consulta: ", n)
    n += 1
    if n>n_limite:
        break

results.close()
final = time.time()
print("Tiempo total: ", final-inicial, "segundos.")

