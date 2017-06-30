from pymongo import MongoClient
from virus_total_apis import ApiError, PublicApi
import json
import pprint
# MongoDB URI Format
#client = MongoClient('mongodb://localhost:27017/')
# MongoDB host, port format
client = MongoClient('localhost', 27017)

# Get DataBase
db = client.PyVirusTotal
print(db)
# Get Collections
print(db['gura'])

API_KEY = '2539516d471d7beb6b28a720d7a25024edc0f7590d345fc747418645002ac47b'

EICAR = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*".encode('utf-8')
vt = PublicApi(API_KEY)
data = vt.get_file_report('44cda81782dc2a346abd7b2285530c5f')
data2 = vt.scan_file('C:\\Users\\YES24\\Desktop\\자료정리\\분류전\\cmd.exe')
#pprint.pprint(data)
print(type(data))
data['chuka'] = "c:\\users\\fuckyou.exe"
print(db.scan_result.insert(data))
print(db.scan_result.insert(data2))