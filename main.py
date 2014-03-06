import urllib2
import lxml.html

def getLivePage():
    return urllib2.urlopen('http://lists.openhatch.org/mailman/admin').read()

def getCachedPage():
    return open('admin').read()

def pageToListNames(content):
    raw_string = lxml.html.fromstring(content)
    raw_html = raw_string.xpath("//table//td/a/@href")
    return [x.replace('admin/', '') for x in raw_html]

