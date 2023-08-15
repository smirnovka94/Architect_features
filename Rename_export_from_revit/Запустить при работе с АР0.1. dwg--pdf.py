import os, re, pathlib, datetime, time, copy
import sys

def read_dir(name_dir: str) -> list:
    """
    Считывает файлы из папки 
    """
    list_files = []
    for file in os.listdir(name_dir):
        filename = ''.join(c for c in file if c.isprintable())
        try:
            os.rename(file, filename)
        except FileNotFoundError:
            pass
        list_files.append(file)
    return list_files

def data_file(filename):
    """
    Функция даты файлов
    """
    ti_m = os.path.getmtime(filename)
    m_ti = time.ctime(ti_m)
    t_obj = time.strptime(m_ti)
    T_stamp = time.strftime("%Y.%m.%d", t_obj)
    return T_stamp

def pattern_(file: str):
    """Файл PDFный???"""
    pdf_ = re.fullmatch(r'.*.pdf', file)
    dwg_ = re.fullmatch(r'.*.dwg', file)
    exe_ = re.fullmatch(r'.*.exe', file)
    png_ = re.fullmatch(r'.*.png', file)
    jpg_ = re.fullmatch(r'.*.jpg', file)
    tiff_ =re.fullmatch(r'.*.tiff', file)
    if pdf_ or exe_ :
        return True
    
def pattern_all(file: str):
    """Файл PDFный???"""
    pdf_ = re.fullmatch(r'.*.pdf', file)
    dwg_ = re.fullmatch(r'.*.dwg', file)
    exe_ = re.fullmatch(r'.*.exe', file)
    png_ = re.fullmatch(r'.*.png', file)
    jpg_ = re.fullmatch(r'.*.jpg', file)
    tiff_ =re.fullmatch(r'.*.tiff', file)
    if dwg_ or pdf_ or exe_ or png_ or jpg_ or tiff_:
        return True

dict_name = {
            "209.18-Р-АР0.1-00-Титул": [r".*_00.\w{3}", r'.*Лист.*Титул.*'],
            "209.18-Р-АР0.1-01-Общие данные": [r".*_01.\w{3}", r'.*Лист.*Общие данные.*'],
            "209.18-Р-АР0.1-02-Разбивочный план осей": [r".*_02.\w{3}", r'.*Лист.*Разбивочный план осей.*'],
            "209.18-Р-АР0.1-03-Компоновочный план подземного гаража на отм. -5.410 Фрагмент 1": [r".*_03.\w{3}", r'.*Лист.*Компоновочный план подземного гаража на отм. -5.410 Фрагмент 1.*'],
            "209.18-Р-АР0.1-04-Компоновочный план подземного гаража на отм. -5.410 Фрагмент 2": [r".*_04.\w{3}", r'.*Лист.*Компоновочный план подземного гаража на отм. -5.410 Фрагмент 2.*'],
            "209.18-Р-АР0.1-05-Компоновочный план подземного гаража на отм. -5.410 Фрагмент 3": [r".*_05.\w{3}", r'.*Лист.*Компоновочный план подземного гаража на отм. -5.410 Фрагмент 3.*'],
            "209.18-Р-АР0.1-06-Компоновочный план подземного гаража на отм. -5.410 Фрагмент 4": [r".*_06.\w{3}", r'.*Лист.*Компоновочный план подземного гаража на отм. -5.410 Фрагмент 4.*'],
            "209.18-Р-АР0.1-07-Компоновочный план подземного гаража на отм. -5.410 Фрагмент 5": [r".*_07.\w{3}", r'.*Лист.*Компоновочный план подземного гаража на отм. -5.410 Фрагмент 5.*'],
            "209.18-Р-АР0.1-08-Компоновочный план подземного гаража на отм. -5.410 Фрагмент 6": [r".*_08.\w{3}", r'.*Лист.*Компоновочный план подземного гаража на отм. -5.410 Фрагмент 6.*'],
            "209.18-Р-АР0.1-09-План подземного гаража на отм. -5.410 Фрагмент 1": [r".*_09.\w{3}", r'.*Лист.*План подземного гаража на отм. -5.410 Фрагмент 1.*'],
            "209.18-Р-АР0.1-10-План подземного гаража на отм. -5.410 Фрагмент 2": [r".*_10.\w{3}", r'.*Лист.*План подземного гаража на отм. -5.410 Фрагмент 2.*'],
            "209.18-Р-АР0.1-11-План подземного гаража на отм. -5.410 Фрагмент 3": [r".*_11.\w{3}", r'.*Лист.*План подземного гаража на отм. -5.410 Фрагмент 3.*'],
            "209.18-Р-АР0.1-12-План подземного гаража на отм. -5.410 Фрагмент 4": [r".*_12.\w{3}", r'.*Лист.*План подземного гаража на отм. -5.410 Фрагмент 4.*'],
            "209.18-Р-АР0.1-13-План подземного гаража на отм. -5.410 Фрагмент 5": [r".*_13\w{3}", r'.*Лист.*План подземного гаража на отм. -5.410 Фрагмент 5.*'],
            "209.18-Р-АР0.1-14-План подземного гаража на отм. -5.410 Фрагмент 6": [r".*_14.\w{3}", r'.*Лист.*План подземного гаража на отм. -5.410 Фрагмент 6.*'],
            "209.18-Р-АР0.1-15-План гидроизоляции": [r".*_15.\w{3}", r'.*Лист.*План гидроизоляции.*'],
            "209.18-Р-АР0.1-16-Планы рампы на отм.-5,400 и 0,000, план кровли рампы. Разрезы А-А, Б-Б и В-В": [r".*_16.\w{3}", r'.*Лист.*Планы рампы на отм.-5,400 и 0,000, план кровли рампы. Разрезы А-А, Б-Б и В-В.*'],
            "209.18-Р-АР0.1-17-Разрез 1-1, Разрез 2-2": [r".*_17.\w{3}", r'.*Лист.*Разрез 1-1, Разрез 2-2.*'],
            "209.18-Р-АР0.1-18-Типы наружных стен. Типы внутренних многослойных перегородок": [r".*_18.\w{3}", r'.*Лист.*Типы наружных стен. Типы внутренних многослойных перегородок.*'],
            "209.18-Р-АР0.1-19-Типы полов. Типы потолков. Типы кровель": [r".*_19.\w{3}", r'.*Лист.*Типы полов. Типы потолков. Типы кровель.*'],
            "209.18-Р-АР0.1-20-Ведомости и спецификации (заполнение проемов, перемычки )": [r".*_20.\w{3}", r'.*Лист.*Ведомости и спецификации (заполнение проемов, перемычки ).*'],
            "209.18-Р-АР0.1-21-Ведомость отделки помещений. (Начало)": [r".*_21.\w{3}", r'.*Лист.*Ведомость отделки помещений. (Начало).*'],
            "209.18-Р-АР0.1-21.1-Ведомость отделки помещений. (Конец)": [r".*_21.1.\w{3}", r'.*Лист.*Ведомость отделки помещений. (Конец).*'],
            "209.18-Р-АР0.1-22-Фрагменты планов лестниц. Сечения по лестницам Г-Г, Д-Д, Е-Е": [r".*_22.\w{3}", r'.*Лист.*Фрагменты планов лестниц. Сечения по лестницам Г-Г, Д-Д, Е-Е.*'],
            "209.18-Р-АР0.1-23-Фрагменты планов лестниц. Сечения по лестницам Ж-Ж, И-И, К-К": [r".*_23.\w{3}", r'.*Лист.*Фрагменты планов лестниц. Сечения по лестницам Ж-Ж, И-И, К-К.*'],
            "209.18-Р-АР0.1-24-Фрагменты планов лестниц. Сечения по лестницам Л-Л, М-М": [r".*_24.\w{3}", r'.*Лист.*Фрагменты планов лестниц. Сечения по лестницам Л-Л, М-М.*'],
            "209.18-Р-АР0.1-25-Мероприятия по обеспечению доступа инвалидов": [r".*_25.\w{3}", r'.*Лист.*Мероприятия по обеспечению доступа инвалидов.*'],
            }

def replace_file(full_filename_now,full_filename_new):
    """
    Функция переноса файлов
    """
    file = os.path.basename(full_filename_now)
    time_ =  datetime.datetime.now().replace(microsecond=0)
    dir_now = os.path.basename(os.path.dirname(full_filename_now))
    dir_new = os.path.basename(os.path.dirname(full_filename_new))
    print(f"Перенесли файл из {dir_now}:{file[:5]}...{file[-30:]} --> в папку {dir_new}. Время: {time_}")
    os.replace(full_filename_now, full_filename_new)
    
def dict_right_filename(find_name):
    """Подбирает к неправильному имени правильное"""
    strip_name, file_extension = os.path.splitext(find_name)
    if pattern_all(find_name):
        for keys, values in dict_name.items():
            bool_rename = re.fullmatch(values[1], find_name)
            if bool_rename == None:
                bool_rename = re.fullmatch(values[0], find_name)
            if bool_rename:
                right_filename = keys + file_extension
                #print(f"Переименовали фаил {find_name} --> {right_filename}")
                return right_filename

           
def main():
    directory = os.path.abspath(os.getcwd())
    directory_dwg = os.path.join(directory, "DWG")
    directory_pdf = os.path.join(directory, "PDF")
    #list_dir = [directory_pdf, directory_dwg, directory]

    from_PDF = read_dir(directory_pdf) #Файлы из папки PDF
    from_DWG = read_dir(directory_dwg) #Файлы из папки DWG
    
    for file in from_DWG:
        on_rename = dict_right_filename(file)
        full_file = os.path.join(directory_dwg, file)
        if on_rename != None:
            full_on_rename = os.path.join(directory_dwg, on_rename)
            if on_rename in from_DWG:
                print(f"Удален {on_rename}")
                os.remove(full_on_rename)
        
            
    for file in from_DWG:
        on_rename = dict_right_filename(file)
        full_file = os.path.join(directory_dwg, file)
        if on_rename != None:
            full_on_rename = os.path.join(directory_dwg, on_rename)
            print(f"Переименовали фаил {file} --> {on_rename[:25]}...{on_rename[-30:]}") 
            os.rename(full_file, full_on_rename)
  
    for file in from_DWG:
        full_name = os.path.join(directory_dwg, file)
        full_name_new = os.path.join(directory_pdf, file)
        #Ищем НЕ PDF файлы, после чего запускаем удаление/перемещение
     
        if pattern_(file):
            try:
                replace_file(full_name, full_name_new)
            except FileNotFoundError:
                continue


while(True):
    try:
        main()
    except PermissionError:
        time.sleep(30)
    time.sleep(10)
    
