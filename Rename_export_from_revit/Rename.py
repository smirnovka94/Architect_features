import os, re, time

def simple_list_files(directory=os.path.abspath(os.getcwd())):
    """
    Выдает список всех файлов из текущей или указанной папки
    os.path.abspath(os.getcwd())
    :return: list
    """
    return os.listdir(directory)

def ignore(name):
    if re.fullmatch(r'.*.py',name):
        return False
    elif re.fullmatch(r'\d\d\d\d.\d\d.\d+_.*',name):
        return False
    else:
        return True

def data_name(name, version=0):
    ti_m = os.path.getmtime(name)
    m_ti = time.ctime(ti_m)
    t_obj = time.strptime(m_ti)
    T_stamp = time.strftime("%Y.%m.%d", t_obj)
    if version == 0:
        new_name = f"{T_stamp}_{str(file)}"
    else:
        new_name = f"{T_stamp}_ver{version}_{str(file)}"
    return new_name

def version_num(name):
    result = re.findall(r'ver\d+', name)
    result = ''.join(result)
    result = str(result[3:])
    if result == '':
        return 0
    else:
        return int(result)
    
def get_version(el, lst):
    list_ = []
    #Ищем эл. с одинаковыми названиями
    for i, el_lst in enumerate(lst):
        if el in el_lst:
            #вычленяем версию из названия файла
            ver = version_num(lst[i])
            list_.append(ver)
    if max(list_) == 0:
        return 1
    return max(list_)
    
        
def print_rename(file1, file2):
    #print(f"{i} ----------- {file1}")
    #print(f"{i} новое имя-- {file2}")
    print(f"{file1} --> {file2}")
    os.rename(file1, file2)
    
files = simple_list_files()

for i, file in enumerate(files):
    old_name = file
    if data_name(file) in files:
        version = get_version(file, files) + 1
        naw_name = data_name(file,version)
        print_rename(old_name, naw_name)
        
    elif ignore(file):
        naw_name = data_name(file)
        print_rename(old_name, naw_name)



