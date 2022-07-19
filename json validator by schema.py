import json
import jsonschema
with open('your file path here','r',encoding='utf-8') as f :
   json_data=json.load(f)
   #input your schema here. If you don't have one, you can check my "get schema.py"
json_schema = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'pm10': {
                'type': 'number',
        },
        'city': {
            'type': 'string',
            'enum': ['珠海', '深圳']
            },
            'time': {
                'type': 'string'
            }
        }
    }
}
try:
    jsonschema.validate(json_data, json_schema)
except jsonschema.ValidationError as ex:
    msg = ex
    print(ex)