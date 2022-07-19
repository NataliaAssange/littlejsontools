import json
import logging
import jsonschema
class JsonToScheam:

    @classmethod
    def get_object_data(cls, dict_data):
        schema_data = {}
        for dict_data_k in dict_data.keys():
            if type(dict_data[dict_data_k]) in (str, int, bool, float, list):
                if type(dict_data[dict_data_k]) is str:
                    schema_data[dict_data_k] = {"type": "string"}
                    continue
                if type(dict_data[dict_data_k]) is int:
                    schema_data[dict_data_k] = {"type": "integer"}
                    continue
                if type(dict_data[dict_data_k]) is bool:
                    schema_data[dict_data_k] = {"type": "boolean"}
                    continue
                if type(dict_data[dict_data_k]) is float:
                    schema_data[dict_data_k] = {"type": "number"}
                    continue
 
                if type(dict_data[dict_data_k]) is list:
                    schema_data[dict_data_k] = {"type": "array"}
                    continue
            if dict_data[dict_data_k] is None:
                schema_data[dict_data_k] = {"type": "null"}
                continue
            elif type(dict_data[dict_data_k]) == dict:
                schema_temp = {"type": "object", 'properties': cls.get_object_data(dict_data[dict_data_k])}
                schema_data[dict_data_k] = schema_temp
 
            else:
                print(dict_data[dict_data_k] == None)
        return schema_data
 
    def get_schema(self, data):
        return {'type': "object", 'properties': JsonToScheam.get_object_data(data)}
 
 
if __name__ == '__main__':
# note:this sample file should contain ONLY ONE line! Please select carefully the longest one you want, and make sure it is correct in grammar
    with open(r'C:\Users\CN0CHHG\Documents\New\case_clean.json', encoding="utf-8") as f:
        schema = JsonToScheam().get_schema(json.load(f))
    print(schema)



