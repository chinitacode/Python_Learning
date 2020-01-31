import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

# json.loads = 'load from string', turning a json string object accordingly into a python object
# because there's only one dictionary in the data string, so type(info) ==> <class 'dict'>
info = json.loads(data)
print('Name: ',info['name'])
print('Phone: ',info['phone']['number'])
print('Hide email: ', info['email']['hide'])

'''
Name:  Chuck
Phone:  +1 734 303 4456
Hide email:  yes


# 还原成json格式：
>>> d = json.dumps(info)
>>> print(d)
{"name": "Chuck", "phone": {"type": "intl", "number": "+1 734 303 4456"}, "email": {"hide": "yes"}}
>>>

# 加上缩进：
>>> d = json.dumps(info,indent=4)
>>> d
'{\n    "name": "Chuck",\n    "phone": {\n        "type": "intl",\n        "number": "+1 734 303 4456"\n    },\n    "email": {\n        "hide": "yes"\n    }\n}'
>>> print(d)
{
    "name": "Chuck",
    "phone": {
        "type": "intl",
        "number": "+1 734 303 4456"
    },
    "email": {
        "hide": "yes"
    }
}


'''
