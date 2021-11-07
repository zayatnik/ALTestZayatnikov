import os.path
l = [0.0, 0.0]

def word_is_bilingual(s):   #функция, определяющая, содержит ли строка буквы обоих алфавитов одновременно (предназначена только для работы с заглавными буквами)
    fle = False
    flr = False
    for i in s:
        if char_is_big_eng_letter(i):
            fle = True
            break
    for i in s:
        if char_is_big_rus_letter(i):
            flr = True
            break
    return fle and flr

def quantity_of_letters_in_text(s):   #функция, определяющая количество заглавных букв обоих алфавитов в строке
    count = 0
    for i in s:
        if char_is_big_letter(i):
            count = count + 1
    return count

def char_is_big_eng_letter(c):   #функция, определяющая, является ли символ заглавной буквой английского алфавита
    if c >= 'A' and c <= 'Z':
        return True
    else:
        return False

def char_is_big_rus_letter(c):   #функция, определяющая, является ли символ заглавной буквой русского алфавита
    if c >= 'А' and c <= 'Я' or c =='Ё':
        return True
    else:
        return False

def char_is_big_letter(c):   #функция, определяющая, является ли символ заглавной буквой одного из двух алфавитов
    if char_is_big_eng_letter(c) or char_is_big_rus_letter(c):
        return True
    else:
        return False

def is_text(s):   #функция, определяющая, содержит ли строка текст (текст определяем как нечто, отличное от пробелов и отступов строк)
    for i in s:
        if i != ' ' and i != '\n':
            return True
    return False

def text_stat(filename):                              #функция, рассчитывающая статистику текстового файла: доля спользования данной буквы среди всех букв файла, доля слов с буквой, количество слов в тексте, количество абзацев в тексте, количество слов с использованием букв обоих алфавитов
    if type(filename) != str:                         #если аргуметом является не строка, возвращаем ошибку
        return {'error': 'Аргументом должна быть строка - название файла'}
    if os.path.exists(filename) == False:             #если файл с заданным именем не находится - тоже ошибка
        return {'error': 'Файла с таким именем не существует в данном директории'}
    with open('file.txt', encoding = 'utf-8') as f:   #открываем файл и записываем его содержимое в строку
        s = f.read()
    res = \
        {'A': l, 'B': l, 'C': l, 'D': l, 'E': l, 'F': l, 'G': l, 'H': l, 'I': l, 'J': l, 'K': l, 'L': l, 'M': l, 'N': l,
         'O': l, 'P': l, 'Q': l, 'R': l, 'S': l, 'T': l, 'U': l, 'V': l, 'W': l, 'X': l, 'Y': l, 'Z': l, 'А': l, 'Б': l,
         'В': l, 'Г': l, 'Д': l, 'Е': l, 'Ё': l, 'Ж': l, 'З': l, 'И': l, 'Й': l, 'К': l, 'Л': l, 'М': l, 'Н': l, 'О': l,
         'П': l, 'Р': l, 'С': l, 'Т': l, 'У': l, 'Ф': l, 'Х': l, 'Ц': l, 'Ч': l, 'Ш': l, 'Щ': l, 'Ъ': l, 'Ы': l, 'Ь': l,
         'Э': l, 'Ю': l, 'Я': l, 'word_amount': 0, 'paragraph_amount': 0, 'bilingual_amount': 0}   #словарь, в который будет записан результат работы функции
    if is_text(s) == 0:                  #если содержимое строки не является текстом, возвращаем словарь с нулевыми значениями
        for i in res:
            if res[i] == l:
                res[i] = (0, 0)
        return res
    s = s.upper()                        #будем работать с буквами в заглавном регистре - так будет удобнее
    fl1 = False                          #вспомогательные флаги для подсчёта слов и абзацев
    fl2 = False
    word = ''                            #здесь будем хранить "текущее" слово
    for i in s:                          #проходим по строке и "собираем" нужную нам информацию
        if i != ' ' and i != '\n':       #проверка условия для подсчёта слов
            word = word + i
            if fl1 == False:
                res['word_amount'] = res['word_amount'] + 1
                fl1 = True
        if i == ' ' or i == '\n':        #проверка условий для подсчёта "двуязычных" слов и колчества слов, содержащих ту или иную букву
            if len(word):
                if word_is_bilingual(word):
                    res['bilingual_amount'] = res['bilingual_amount'] + 1
                for i in res:
                    if word.find(i) != -1:
                        res[i] = [res[i][0], res[i][1] + 1.0]
            word = ''
            fl1 = False
        if i != '\n' and fl2 == False:   #проверка условий для подсчёта абзацев
            res['paragraph_amount'] = res['paragraph_amount'] + 1
            fl2 = True
        if i == '\n':
            fl2 = False
        if char_is_big_letter(i):        #подсчёт букв
            res[i] = [res[i][0] + 1.0, res[i][1]]
    if len(word):                        #поправим статистику с учётом последнего слова, т.к. его мы ещё не учитывали
        if word_is_bilingual(word):
            res['bilingual_amount'] = res['bilingual_amount'] + 1
        for i in res:
            if word.find(i) != -1:
                res[i] = [res[i][0], res[i][1] + 1.0]
    for i in res:                         #преобразуем статистику для букв: из количества переведём в процентную долю, поделив на общее колчество
        if char_is_big_letter(i):         #итоговые результаты сохраним в кортежи
            res[i] = (res[i][0] / float(quantity_of_letters_in_text(s)), res[i][1] / float(res['word_amount']))
    return res                          #возвращаем получившийся словарь