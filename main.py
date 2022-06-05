import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

with open ("palabras.txt", "r") as f: #Importamos un fichero
	lines = f.read().splitlines()  # Aqui le decimos que lea por linea y haga los saltos

PROTO = ['https://'] #, 'http://']
TLD = ['.web.app', '.firebaseapp.com']  #  lista '.site', '.xyz', '.online', 
PATH =  ['/ingreso']

for dominio in lines:
	for dominio1 in lines:
			for tlds in TLD: #Bucle anidadaro
				for path in PATH:
					for protos in PROTO:
						#print(protos + dominio + tlds)
						try:
							result = requests.get(protos + dominio + '-' + dominio1 + tlds + path, verify=False)							
		
							if result.status_code == 200:
								sourceFile = open('dominioactivo1.txt', 'w')
								print("Dominio activo:" + protos + dominio + '-' + dominio1 + tlds + path, file = sourceFile)
								sourceFile.close()
							else:
								print("Dominio inactivo:" + protos + dominio + '-' + dominio1 + tlds + path)

						except:
							#print("Dominio inactivo:" + protos + dominio + '-' + dominio1 + tlds + path)
							pass
							continue
