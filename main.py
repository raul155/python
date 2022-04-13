import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

with open ("test", "r") as f: #Importamos un fichero
	lines = f.read().splitlines()  # Aqui le decimos que lea por linea y haga los saltos de URL

PROTO = ['https://', 'http://']


TLD = ['.site', '.xyz', '.online']  #  lista  '.com' '.es'

for dominio in lines:
	for tlds in TLD: #Bucle anidado
		for protos in PROTO:

			#print(protos + dominio + tlds)
			try:
				result = requests.get(protos + dominio + tlds, verify=False)

				if result.status_code == 200:
					print("Dominio activo: " + protos + dominio + tlds) # wtf string tras string sin concatenar? 

			except:
				pass
				#print("Dominio inactivo:" + protos + dominio + tlds)
				continue #Le decimos que vuelva a recorrer
