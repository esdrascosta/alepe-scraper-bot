# Simple Data crawler from Alepe - Assembleia Legislativa do Estado de Pernambuco

## Related law:
http://legis.alepe.pe.gov.br/arquivoTexto.aspx?tiponorma=15&numero=566&complemento=0&ano=2005

## Install the dependencies
`pip install -r requirements.txt`

## Execute the following command:
`scrapy crawl alepe -o alepe_data.csv`

## Limit data
`scrapy crawl alepe -o alepe_data.csv -a yearFrom=2016 -a yearTo=2017 -a monthFrom=6 -a monthTo=12`
