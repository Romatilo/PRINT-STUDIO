import json
import re
import os

def sorting_strings (i):
    inner_file_list['num_%s' % i].write(fields['text'] + '\n')               
    chunks = re.split(", -|\n", fields['text'])
    for string in chunks:
        if (any(item in string.lower() for item in a4)
             and not any(item in string.lower() for item in color)
             and not glossy in string.lower()
             and not mat in string.lower()):
            inner_file_list['num_%s' % (i+1)].write(string + '\n')
        elif (any(item in string.lower() for item in a4) and any(item in string.lower() for item in color)):
            inner_file_list['num_%s' % (i+2)].write(string + '\n')
        elif (any(item in string.lower() for item in a4) and glossy in string.lower()):
            inner_file_list['num_%s' % (i+3)].write(string + '\n')
        elif (any(item in string.lower() for item in a4) and mat in string.lower()):
            inner_file_list['num_%s' % (i+4)].write(string + '\n')
        elif (any(item in string.lower() for item in a6) and glossy in string.lower()):
            inner_file_list['num_%s' % (i+5)].write(string + '\n')
        elif (any(item in string.lower() for item in a6) and mat in string.lower()):
            inner_file_list['num_%s' % (i+6)].write(string + '\n')
        elif (any(item in string.lower() for item in b6)):
            inner_file_list['num_%s' % (i+7)].write(string + '\n')
        elif (any(item in string.lower() for item in check)):
            inner_file_list['num_%s' % (i+8)].write(string + '\n')
        else:
            inner_file_list['num_%s' % (i+9)].write(string + '\n')                 


parent_dir = os.path.dirname(os.path.abspath(__file__))  # Получаем путь к папке
files_in_program = ["v", "i" ,"k", "l", "u"]
folders = ["Вавилова", "Иркутский", "Комс", "Ленина", "Учебная"]
file_names = ["общий", "А4_ЧБ", "А4_ЦВЕТ", "А4_ГЛЯНЕЦ", "А4_МАТ", "А6_ГЛЯНЕЦ", "А6_МАТ", "B6", "Чековая", "Unsorted"]
total_files_amount = len(files_in_program)*len(file_names)

### Задаем имена файлов для каждого филиала###
file_list = dict()
i = 0
for branch in folders:
    for name in file_names:
        file_list['num_%s' % i] = (branch+'_'+name)
        i += 1

### Создаем папки ###
for branch in folders:
    path = os.path.join(parent_dir, branch)
    if not os.path.exists(branch):
        os.makedirs(path)
        print ("Folder " + branch + " created")

### Создадим список имен для внутренних файлов ###
inner_file_list = dict()
for i in range (0, total_files_amount):
    inner_file_list['num_%s' % i] = ('f' + str(i))
    
### Открываем все файлы ###
index = 0
for branch in folders:
    current_dir = parent_dir + "\\" + branch
    for i in range (0, len(file_names)):
        inner_file_list['num_%s' % index] = open(current_dir + "\\" + file_list['num_%s' % index] + ".txt", "w")
        index +=1
        

a4 = ["a4", "а4", "ач ", "ач-", "лист офис", "листf офис"]
a6 = ["a6", "а6" , "10x15" , "10х15", "10 x 15", "10 х 15", "10*15", "10/15", "10\\5", "10 на 15", "10на15"]
b6 = ["13x18" , "13х18", "13 x 18", "13 х 18", "13*18", "13/18", "13\18", "13 на 18", "13на18"]
mat = "мат"
glossy = "гл"
color = ["цв", "п/ц"]
black = ["чб", "ч/б"]
check = ["чек", "лент"]

with open('result.json',"r", encoding="utf-8") as f:
    templates = json.load(f)


for fields in templates['messages']:
    try:
        if fields['from_id'] == 'user2014981178':  # 10 ВАВИЛОВА
            sorting_strings (0)           
        if fields['from_id'] == 'user2018139303':  # 194 ИРКУТСКИЙ
            sorting_strings (10)   
        if fields['from_id'] == 'user2013105521':  # 77 КОМСОМОЛЬСКИЙ
            sorting_strings (20)    
        if fields['from_id'] == 'user2042351667':  # 41 ЛЕНИНА
            sorting_strings (30)   
        if fields['from_id'] == 'user2036866154':  # 46 УЧЕБНАЯ
            sorting_strings (40)   
    except:
        pass

### Закрываем все файлы ###
 
for i in range (0, total_files_amount):
    inner_file_list['num_%s' % i].close()