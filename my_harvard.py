from api_key import apikey
import urllib3

http = urllib3.PoolManager()
url_base = 'https://api.harvardartmuseums.org/'
url_extensions = ['object', 'culture']
harvard_url = url_base + url_extensions[1]





fields = {'apikey':apikey, 'fields':'objectnumber,title,dated'}

r = http.request('GET', harvard_url, fields = fields )

print("*"*20)
print("STATUS")
print("*"*20)
print(r.status)
print("*"*20)
print("DATA")
print("*"*20)
print(r.data)


# Example: Get Indonesian Culture:
cultures = {'Indonesian':"37527705"}
request_url = harvard_url+'/'+cultures['Indonesian']
fields = {'apikey':apikey}
Indonesian_culture =http.request('GET', request_url, fields = fields).data
print(Indonesian_culture)


# Example: Get Classifications
url = url_base + 'classification'
fields = {'apikey':apikey}
classifications = http.request('GET', url, fields = fields).data
