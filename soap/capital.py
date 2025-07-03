import requests

# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# XML estruturado
payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
					<CapitalCity xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
						<sCountryISOCode>BR</sCountryISOCode>
					</CapitalCity>
				</soap:Body>
			</soap:Envelope>"""
# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
# request POST
response = requests.request("POST", url, headers=headers, data=payload)

# imprime a resposta
dom = parseString(response.text)
print(response)
print(dom.documentElement.getElementsByTagName("m:CapitalCityResult")[0].firstChild.nodeValue)