import os
from django.utils.encoding import smart_str
from django.conf import settings

languages_list = ['polish', 'english', 'spanish', 'french', 'german']
language_file_path = 'media/language_patterns/'

def measure_size(filename):
    os.system('zip %s %s.txt' % (filename, filename))
    result = os.path.getsize(filename + '.zip')
    os.system('rm %s.zip' % filename)
    return result

def lang_diff(lang, text):
    os.system('cp %s.txt temp.txt' % lang)
    init_size = measure_size('temp')
    lang_file = open('temp.txt', 'a')
    lang_file.write(smart_str(text))
    lang_file.close()
    after_size = measure_size('temp')
    os.system('rm temp.txt')
    return after_size - init_size

def detect_language(text):
    os.chdir(settings.ABS_DIR(language_file_path))
    return sorted([(language, lang_diff(language, text)) for language in languages_list],
            key = lambda x: x[1])[0][0]


