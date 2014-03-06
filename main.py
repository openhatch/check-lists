import urllib2
import lxml.html
import sys

def getLivePage(name): # mailman or fancy
    if name == "mailman":
        return urllib2.urlopen('http://lists.openhatch.org/mailman/admin').read()
    if name == "fancy":
        return urllib2.urlopen('http://jeweledplatypus.org/listinfo.html').read()

def getCachedPage(name):  # mailman or fancy
    return open(name).read()

def pageToListNames(content):
    raw_string = lxml.html.fromstring(content)
    raw_html = raw_string.xpath("//table//td/a/@href")
    return [x.rsplit("/",1)[1] for x in raw_html]

def callAThing():
    mailman = pageToListNames(getLivePage("mailman"))
    fancy = pageToListNames(getLivePage("fancy"))
    if set(mailman) == set(fancy):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    callAThing()
