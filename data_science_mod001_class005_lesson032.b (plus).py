## parte_001
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

#print get_page('http://xkcd.com/353')
## ----------

## parte_002
def get_next_target(page):
    start_link = page.find('<a href=')

    if start_link == -1:
        return None, 0

    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]

    return url, end_quote
## ----------

## parte_003
def print_all_links (page):
    while True: #to keep the looping (forever) on going till break
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break #break the on going looping
## ----------

print print_all_links(get_page('http://xkcd.com/353'))

print print_all_links(' \
     link <a href="www.python.com"> \
     link <a href="www.c++.com"> \
     link <a href="www.c#.com"> \
     link <a href="www.java.com">')
