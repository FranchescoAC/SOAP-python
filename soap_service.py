from flask import Flask, request, Response
from zeep import Client
from lxml import etree

app = Flask(__name__)

# Servicio SOAP simple
@app.route('/soap', methods=['POST'])
def soap():
    # El cuerpo de la solicitud XML se obtiene de la solicitud POST
    xml_request = request.data

    # Aquí puedes agregar lógica para procesar el XML recibido, en este caso simplemente lo devolvemos
    # En este ejemplo solo devolvemos un saludo, como si fuera una respuesta SOAP.
    
    # Creamos un mensaje de respuesta SOAP
    response_xml = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
                      xmlns:web="http://www.example.com/webservice">
       <soapenv:Header/>
       <soapenv:Body>
          <web:HelloWorldResponse>
             <web:message>Hello, World!</web:message>
          </web:HelloWorldResponse>
       </soapenv:Body>
    </soapenv:Envelope>
    """

    # Devolver la respuesta con el tipo de contenido XML
    return Response(response_xml, content_type='text/xml')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
