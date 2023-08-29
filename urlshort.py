import pyshorteners
url = input('plz enter url :')

def shortenurl(url):
    s= pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortenurl(url)