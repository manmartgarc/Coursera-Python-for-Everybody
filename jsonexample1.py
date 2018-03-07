import json
data = '''{
    "name" : "Chuck",
    "phone" : {
            "type" : "intl",
            "number" : "+1 734 303 4456"
            },
    "email" : {
            "hide" : "yes"
            }
    }'''

info = json.loads(data)
for k,v in info.items():
    print(k,v)