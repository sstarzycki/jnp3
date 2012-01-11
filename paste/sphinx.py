from django.core.management import setup_environ

import settings

setup_environ(settings)

from text.models import Text
from django.utils.html import escape
from mongoengine import *
from django.utils.encoding import smart_str, smart_unicode
import sys
connect('paste')

i = 1
def paste_to_xml(p):
    global i
    i += 1
    print "<sphinx:document id=\"" + str(i) + "\">"
    sys.stdout.write("<id>")
    sys.stdout.write(str(p.id))
    sys.stdout.write("</id>")
    #print "<user>",,
    #print p.user.username,,
    #print "</user>",
    print "<content>"
    #print p.content,
    print smart_str(escape(p.content))
    #u = p.content
    #print u.encode( "utf-8" ,
    print "</content>",
    print "<title>",
    print smart_str(escape((p.title)))
    print "</title>"
    print "<uploaddate>"
    print str(p.upload_date)
    print "</uploaddate>"
    print "</sphinx:document>"

print "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
print "<sphinx:docset>"

for p in Text.objects.all():
    paste_to_xml(p)

print "</sphinx:docset>"
    


