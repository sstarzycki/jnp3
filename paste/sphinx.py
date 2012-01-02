from django.core.management import setup_environ

import settings

setup_environ(settings)

from text.models import Text

def paste_to_xml(p):
    print "<sphinx:document id=\"" + str(p.id) + "\">"
    print "<user>",
    print p.user.username,
    print "</user>"
    print "<content>",
    print p.content,
    print "</content>"
    print "<description>",
    print p.description,
    print "</description>"
    print "<uploadDate>",
    print p.upload_date,
    print "</uploadDate>"
    print "</sphinx:document>"

print "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
print "<sphinx:docset>"

for p in Text.objects.all():
    paste_to_xml(p)

print "</sphinx:docset>"
    


