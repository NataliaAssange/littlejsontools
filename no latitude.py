import json
with open(r'C:\Users\CN0CHHG\Downloads\case_test.json',encoding="utf-8") as f:
    data=json.load(f)
    for i in data:
        a=i.get('_source').get('LATITUDE')
        if a is None:
            b=i.get('_source').get('ADDR_DETL').get('CASE_ADDRESS')
            c=i.get('_source').get('STD_ADDRESS')
            d=i.get('_source').get('ADDR_DETL').get('caseAddress')            
            if c is None:
                if b is not None:
                    i['check_address']=b
                elif d is not None:
                    i['check_address']=d
                else:
                    e=i.get('_source').get('ADDR_DETL').get('police').get('org_name')
                    if e is not None:
                        i['check_address']=e
            else:
                i['check_address']=c
            #把check——address丢进api里得到经纬度
            lat=120
            lon=30 #占位
            list_data = i['_source']
            dict_value = list_data['LATITUDE']=lat
            dict_value = list_data['LONGITUDE']=lon
            last_value = {'_source':f"{list_data}"}
            i.update(last_value)
            print(type(i))
           