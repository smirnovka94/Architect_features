from pypdf import PdfMerger
import os
import re
import time

def main():
    right_files = [
    '03.2 ППТ3-4-Д1-П-АР2_Лист 1_План -3 этажа. Фрагмент 1. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 2_План -3 этажа. Фрагмент 2. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 3_План -3 этажа. Фрагмент 3. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 4_План -3 этажа. Фрагмент 4. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 5_План -3 этажа. Фрагмент 5. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 6_План -3 этажа. Фрагмент 6. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 7_План -3 этажа. Фрагмент 7. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 8_Экспликация помещений -3 этажа (начало).pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 9_Экспликация помещений -3 этажа (окончание).pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 10_План -2 этажа. Фрагмент 1. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 11_План -2 этажа. Фрагмент 2. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 12_План -2 этажа. Фрагмент 3. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 13_План -2 этажа. Фрагмент 4. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 14_План -2 этажа. Фрагмент 5. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 15_План -2 этажа. Фрагмент 6. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 16_План -2 этажа. Фрагмент 7. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 17_Экспликация помещений -2 этажа (начало).pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 18_Экспликация помещений -2 этажа (окончание).pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 19_План -1 этажа. Фрагмент 1. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 20_План -1 этажа. Фрагмент 2. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 21_План -1 этажа. Фрагмент 3. М 1ː100.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 22_Экспликация помещений -1 этажа.pdf',
    '03.2 ППТ3-4-Д1-П-АР2_Лист 23_Разрез 1-1. Разрез 2-2. Разрез 3-3. М 1ː100.pdf',
    ]

    #auto-py-to-exe

    def join_pdf(files, file_name):
        """Функция сборки ПДФ файла"""
        merger = PdfMerger()
        num = 1
        for pdf in files:
            merger.append(pdf)
            print(f"Лист {num} - {pdf}")
            num +=1

        merger.write(file_name)
        merger.close()

    # Директория существующего файла
    directory_now = os.getcwd()

    #Параметры ПДФ файла
    name_base = "Объединенный" + ".pdf"
    directory_up = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
    # print(directory_up)
    full_name_pdf = os.path.join(directory_up, name_base)

    # Файлы текущей  директории
    files_pdf = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    num = 0

    #Паттерны поиска
    regex_pattern1 = re.compile('Лист \d+')
    regex_pattern2 = re.compile('АР\d-\d+')
    regex_pattern3 = re.compile('ОДИ-\d+')
    list_patterns = [regex_pattern1, regex_pattern2, regex_pattern3]
    dict_ = {}
    dict_dict = {}

    #Проверка валидности файлов правильному списку
    for file in files:
        if file.endswith(".pdf"):
            full_file_pdf = os.path.join(directory_now, file)
            files_pdf.append(full_file_pdf)
            if file in right_files:
                #Счетчик валидности файлов
                num += 1
            #ищем номер листа
            for pattern in list_patterns:
                try:
                    find_pattern = pattern.search(file)
                    dict_[full_file_pdf] = int(find_pattern[0][4:])
                except TypeError:
                    break#continue
                except ValueError:
                    continue

            dict_dict[full_file_pdf] = file

    if len(right_files) == num:
        print("Нэйминг файлов валидный")
        join_pdf(right_files, full_name_pdf)
        os.startfile(full_name_pdf)
        print("\nФайл сохранен папкой выше")
        time.sleep(120)

    elif len(dict_)==len(files_pdf):

        #Сортируем словарь по значениям
        dict_s = sorted(dict_.items(), key=lambda x: x[1])
        merger = PdfMerger()
        num = 1
        for pdf, v in dict_s:
            print(f"Лист {num} - {pdf}")
            num +=1
            merger.append(pdf)

        merger.write(full_name_pdf)
        merger.close()
        os.startfile(full_name_pdf)
        print("\nФайл сохранен папкой выше")
        time.sleep(120)

    elif len(dict_dict) == len(files_pdf):
        dict_s = sorted(dict_dict.items(), key=lambda x: x[1])
        print("Нэйминг файлов вне шаблона сортировки, порядок листов такой:")
        merger = PdfMerger()
        num = 1
        for pdf, v in dict_s:
            print(f"Лист {num} - {pdf}")
            num +=1
            merger.append(pdf)

        merger.write(full_name_pdf)
        merger.close()
        os.startfile(full_name_pdf)
        print("\nФайл сохранен папкой выше")
        time.sleep(120)

    else:
        print("Ошибка сортировки обратиться к https://t.me/s_kirill94")
        time.sleep(120)

if __name__ == '__main__':
    main()
    time.sleep(120)
