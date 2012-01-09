from djangorestframework.resources import ModelResource, BaseResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from djangorestframework.views import View

from text.models import Text
from text.tasks import add_language_to_paste


class TextResource(BaseResource):
  model = Text
  include = ('content', 'title')
  ordering = ('created')


class ListTexts(View):
  def get(self, request):
    constraints = {}

    if 'title' in request.GET:
      constraints['title'] = request.GET['title']

    if 'language' in request.GET:
      constraints['language'] = request.GET['language'] or 'unknown'

      if constraints['language'] == 'unknown':
        constraints['language'] = None

    if 'upload_day' not in request.GET:
      texts = Text.objects.all().filter(**constraints)
    else:
      texts = [t for t in Text.objects.all().filter(**constraints) if t.upload_date.date() == request.GET['day']]

    if 'update_day' not in request.GET:
      texts = Text.objects.all().filter(**constraints)
    else:
      texts = [t for t in Text.objects.all().filter(**constraints) if t.upload_date.date() == request.GET['day']]

    return [{"id": t.id, "title": t.title, "upload_day": t.upload_date.date(), "update_day": t.update_date.date(), "language": (t.language or 'unknown')} for t in texts]

  def post(self, request):
    if 'content' in request.POST and 'title' in request.POST:
      content = request.POST['content']    
      title = request.POST['title']    

      text = Text(content=content, title=title)

      if request.user.is_authenticated:
        if request.user.id:
          text.user_id = self.request.user.id;

      add_language_to_paste.delay(text)
      text.save()
      response = { 'id': text.id }
    else:
      response = { 'error': 'malformed request'}
    
    return response


class ShowText(View):
  def get(self, request, key):
    print "show text", key
    text = Text.objects.get(id=key)
    return {"id": text.id, "title": text.title,
            "content": text.content, "upload_day": text.upload_date.date(),
            "upload_time": text.upload_date.time(), "update_day": text.update_date.date(),
            "update_time": text.update_date.time(), "language": (text.language or 'unknown')} 

  def post(self, request, key):
    response = { 'error': 'malformed request' }

    if 'content' in request.POST and 'id' in request.POST:
      response = { 'error': 'authorization denied' }

      content = request.POST['content']    
      id = request.POST['id']    

      text = Text.objects.get(id=id)

      if request.user.is_authenticated:
        if text.user_id:
          if request.user.id == text.user_id:
            text.save()
            add_language_to_paste.delay(text)
            response = { 'id': text.id }
    
    return response


