import json

with open('result.json', encoding="utf-8") as f:
    templates = json.load(f)
    
v = open("1.Вавилова.txt", "w")
i = open("2.Иркутский.txt", "w")
k = open("3.Комс.txt", "w")
l = open("4.Ленина.txt", "w")
u = open("5.Учебная.txt", "w")

for fields in templates['messages']:
    if fields['from_id'] == 'user2014981178':  # 10 ВАВИЛОВА
        v.write(fields['text'] + '\n')       
    if fields['from_id'] == 'user2018139303':  # 194 ИРКУТСКИЙ
        i.write(fields['text'] + '\n')        
    if fields['from_id'] == 'user2013105521':  # 77 Комсомольский
        k.write(fields['text'] + '\n')
    if fields['from_id'] == 'user2042351667':  # 41 ЛЕНИНА
        l.write(fields['text'] + '\n')        
    if fields['from_id'] == 'user2036866154':  # 46 УЧЕБНАЯ
        u.write(fields['text'] + '\n')
        
v.close
i.close
k.close
l.close
u.close

     


