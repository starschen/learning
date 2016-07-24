import json
data='''{
    "name":"Chunck",
    "phone":{
     "type":"int1",
     "number":"+17343034456"
    },
    "email":{
     "hide":"yes"
    }
}'''

info=json.loads(data)
print 'Name:',info["name"]
print 'Hide:',info["email"]["hide"]
