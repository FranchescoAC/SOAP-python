import requests
from zeep import Client

# URL del servicio SOAP
url = 'http://localhost:5000/soap'

# Enviar solicitud SOAP con XML
headers = {
    'Content-Type': 'text/xml;charset=UTF-8',
}

# Crear un mensaje SOAP
soap_message = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
                  xmlns:web="http://www.example.com/webservice">
   <soapenv:Header/>
   <soapenv:Body>
      <web:HelloWorld/>
   </soapenv:Body>
</soapenv:Envelope>
"""

# Realizar la solicitud POST
response = requests.post(url, data=soap_message, headers=headers)

# Imprimir la respuesta del servicio
print(response.text)
