import urllib2
import lxml.html
import sys

def getLivePage():
    return urllib2.urlopen('http://lists.openhatch.org/mailman/admin').read()

def getCachedPage(name):  # 
    return open(name).read()

def pageToListNames(content):
    raw_string = lxml.html.fromstring(content)
    raw_html = raw_string.xpath("//table//td/a/@href")
    return [x.rsplit("/",1)[1] for x in raw_html]

def callAThing():
    mailman = pageToListNames(getPage(mailman, "live"))
    fancy = pageToListNames(getPage(fancy, "live"))
    if set(mailman) == set(fancy):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    callAThing()
