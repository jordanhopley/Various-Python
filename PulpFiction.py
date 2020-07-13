import urllib2

def get_word_count(xList):
    word_count = dict()
    for x in set(xList):
        word_count.update({x:xList.count(x)})
    words = sorted(word_count, key = word_count.get)
    values = sorted(word_count.values())
    i = len(words)-1
    while i > -1:
        print words[i], values[i]
        i -= 1

def get_list_of_words(html):
    xList = list()
    for x in html.splitlines():
        if x.startswith("                         ") and x.count("             ") == 1:
            x = x.replace("-", " ").replace("'", "").replace(".", "")\
            .replace(",", "").replace("?", "").replace("!", "")\
            .replace(":", "").replace("\"", "").lower()
            xList += x.strip().split()
    get_word_count(xList)

def get_script(host):
    response = urllib2.urlopen(host)
    html = response.read().decode('utf8', 'ignore').encode('utf8')
    get_list_of_words(html)

def get_movie(movie):
    host_site = 'http://www.dailyscript.com/scripts/' + movie + '.html'
    get_script(host_site)

get_movie('pulp_fiction')
