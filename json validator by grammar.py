import json
import re
try:
    with open(r'yourpath\yourfile.json',encoding="utf-8") as f:
        a=f.read()
        json.JSONDecoder().decode(a)
except Exception as e:
    print("错误信息:",e)
    msg=str(e)
    l=re.findall(r"\d+.?\d*",msg)
    line=int(l[0])
    char1=int(l[1])-6
    char2=int(l[1])+4
    #find line
    with open(r'yourpath\yourfile.json',encoding="utf-8") as f:
        i = f.readline()
        count = 1
        while i:
            if count >= line:
                break
            i = f.readline()
            count += 1
    #find char
    print(i[char1:char2])
