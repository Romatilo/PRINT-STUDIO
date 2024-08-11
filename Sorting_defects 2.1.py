import json
import re
import os

def sorting_strings (i):
    ''' Модуль сортировки строк по критериям '''
    inner_file_list['num_%s' % i].write(fields['text'] + '\n')               
    chunks = re.split(", -|\n", fields['text'])
    for string in chunks:
        if (a4_in_string(string.lower())
             and not color_in_string(string.lower())
             and not glossy_in_string(string.lower())
             and not mat_in_string(string.lower())):
            inner_file_list['num_%s' % (i+1)].write(string + '\n')
        elif a4_in_string(string.lower()) and color_in_string(string.lower()):
            inner_file_list['num_%s' % (i+2)].write(string + '\n')
        elif a4_in_string(string.lower()) and glossy_in_string(string.lower()):
            inner_file_list['num_%s' % (i+3)].write(string + '\n')
        elif a4_in_string(string.lower()) and mat_in_string(string.lower()):
            inner_file_list['num_%s' % (i+4)].write(string + '\n')
        elif a6_in_string(string.lower()) and glossy_in_string(string.lower()):
            inner_file_list['num_%s' % (i+5)].write(string + '\n')
        elif a6_in_string(string.lower()) and mat_in_string(string.lower()):
            inner_file_list['num_%s' % (i+6)].write(string + '\n')
        elif b6_in_string(string.lower()):
            inner_file_list['num_%s' % (i+7)].write(string + '\n')
        elif check_in_string(string.lower()):
            inner_file_list['num_%s' % (i+8)].write(string + '\n')
        else:
            inner_file_list['num_%s' % (i+9)].write(string + '\n')                 


def create_file_names (income_folders, files_to_sort):
    ''' Задаем имена файлов для каждого филиала '''
    file_list = dict()
    i = 0
    for branch in income_folders:
        for name in file_names:
            file_list['num_%s' % i] = (branch+'_'+name)
            i += 1
    return file_list

def create_folders(income_folders, parent_dir):
    ''' Создаем папки '''
    for branch in income_folders:
        path = os.path.join(parent_dir, branch)
        if not os.path.exists(branch):
            os.makedirs(path)
            print ("Folder " + branch + " created")

def create_inner_file_list_names(files_amount):
    ''' Создадим список имен для внутренних файлов '''
    inner_file_list = dict()
    for i in range (0, files_amount):
        inner_file_list['num_%s' % i] = ('f' + str(i))
    return inner_file_list

def open_all_files(parent_dir, folders, file_names, file_list):
    ''' Открываем все файлы '''
    index = 0
    for branch in folders:
        current_dir = parent_dir + "\\" + branch
        for i in range (0, len(file_names)):
            file_list['num_%s' % index] = open(current_dir + "\\" + file_list['num_%s' % index] + ".txt", "w")
            index +=1
    return file_list
        
def a4_in_string(income_string):
    '''Проверка наличия A4 в строке'''
    substring = "[aа]4|ач[^а-я]|листа? офис|[^а-я]ч[/]?б"
    if re.search(substring, income_string, re.I):
        return True

def a6_in_string(income_string):
    '''Проверка наличия A6 (10x15) в строке'''
    substring = "[aа]6|10[хx\*\s\/\\\]1[456]|10\s?на\s?1[456]"
    if re.search(substring, income_string, re.I):
        return True

def b6_in_string(income_string):
    '''Проверка наличия B6 (13x18) в строке'''
    substring = "[bв]6|1[234][хx\*\s\/\\\]1[789]|1[234]\s?на\s?1[789]"
    if re.search(substring, income_string, re.I):
        return True

def glossy_in_string(income_string):
    '''Проверка наличия глянцевой фотобумаги в строке'''
    substring = "[^а-я]гл"
    if re.search(substring, income_string, re.I):
        return True

def mat_in_string(income_string):
    '''Проверка наличия матовой фотобумаги в строке'''
    substring = "[^а-я]мат"
    if re.search(substring, income_string, re.I):
        return True

def check_in_string(income_string):
    '''Проверка наличия чековой ленты в строке'''
    substring = "[^а-я]чек|[^а-я]лент"
    if re.search(substring, income_string, re.I):
        return True
    
def color_in_string(income_string):
    '''Проверка наличия цветной печати или струйной в строке'''
    substring = "[^а-я]цв|п[/]ц|струй"
    if re.search(substring, income_string, re.I):
        return True


parent_dir = os.path.dirname(os.path.abspath(__file__))  # Получаем путь к папке
files_in_program = ["v", "i" ,"k", "l", "u"]
folders = ["Вавилова", "Иркутский", "Комс", "Ленина", "Учебная"]
file_names = ["общий", "А4_ЧБ", "А4_ЦВЕТ", "А4_ГЛЯНЕЦ", "А4_МАТ", "А6_ГЛЯНЕЦ", "А6_МАТ", "B6", "Чековая", "Unsorted"]
total_files_amount = len(files_in_program)*len(file_names)
with open('result.json',"r", encoding="utf-8") as f:
    templates = json.load(f)

file_list = create_file_names(folders, file_names)
create_folders(folders, parent_dir)
inner_file_list = create_inner_file_list_names(total_files_amount)
inner_file_list = open_all_files(parent_dir, folders, file_names, file_list)

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
    

