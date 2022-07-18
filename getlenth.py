import json
with open(r'C:\Users\CN0CHHG\Downloads\person_info.json',encoding="utf-8") as f:
    data=json.load(f)
    n=0
    for i in data:
        a=i.get('_source').get('LABS')
        try:
            if len(a)>n:
                n=len(a)
            else:
                n=n
        except:
            n=n
l=(n+1)/9
print(l)



