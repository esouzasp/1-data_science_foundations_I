## PSEUDO-CODIGO

#start with tocrawl = [seed]
#crawled = []
#while there are more pages tocrawl:
#    pick a page from tocrawl
#    add that page to crawled
#    add all the link targets on this page to tocrawl
#return crawled

## Answer: avoid circular hyperlinks

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
             
