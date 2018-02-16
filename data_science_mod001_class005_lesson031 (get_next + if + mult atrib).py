#method_001
def get_next_target(page):
    start_link = page.find('<a href=')

    if start_link == -1:
        url = None
        end_quote = 0

    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]

    return url, end_quote
# ----------

#method_002
def get_next_target(page):
    start_link = page.find('<a href=')

    if start_link == -1:
        return None, 0

    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]

    return url, end_quote
# ----------

print get_next_target('abc dfg juk xxx yyy <a ref="www.python.com"')
print get_next_target('abc dfg juk xxx yyy <a href="www.python.com"')

url, endpos = get_next_target('abc dfg juk xxx yyy <a href="www.python.com"')
print url
print endpos
