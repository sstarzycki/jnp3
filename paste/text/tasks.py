from celery.decorators import task
from text.language_detector import detect_language

@task()
def add_language_to_paste(text):
    try:
        text.language = detect_language(text.content)
        text.save()
    except:
        print('adding language failed')
