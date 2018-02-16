# <name> = <expression>
# <name_001>, <name_001>, ... = <expression_001>, <expression_002>, ...

def get_next_target (page):
    start_link = page.find('<a href=')
    start_quote = page.find ('"', star_link)
    end_quote = page.find ('"', start_quote)
    url = page[start_quote + 1 : end_quote]
    return url, end_quote #will give two diff values

url, endpos = get_next_target(page)
