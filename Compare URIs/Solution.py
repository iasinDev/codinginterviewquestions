import sys
from urllib.parse import urlparse
from urllib.parse import unquote

def compare_urls(line):
    urls = line.strip().split(";")
    url0 = urlparse(urls[0])
    url1 = urlparse(urls[1])
    if url0.scheme != url1.scheme:
        return False
    if url0.username != url1.username:
        return False
    if url0.password != url1.password:
        return False
    if url0.hostname != url1.hostname:
        return False
    port0 = 80 if url0.port == None else url0.port
    port1 = 80 if url1.port == None else url1.port
    if port0 != port1:
        return False
    path0 = unquote(url0.path)
    path1 = unquote(url1.path)
    if path0 != path1:
        return False
    query0 = unquote(url0.query)
    query1 = unquote(url1.query)
    if query0 != query1:
        return False
    fragment0 = unquote(url0.fragment)
    fragment1 = unquote(url1.fragment)
    if fragment0 != fragment1:
        return False
    return True

# print(compare_urls("http://abc.com:80//~smith/home.html;http://ABC.com/%2F%7Esmith/home.html")==True)
# print(compare_urls("http://abc.com:80/~smith/home.html;http://ABC.com/%7Esmith/home.html")==True)
print(compare_urls("HTTP://abc.com:80/~smith/home.html?1=2&2=4~#anchor+1~;http://ABC.com/%7Esmith/home.html?1=2&2=4%7E#anchor+1%7E")==True)
# print(compare_urls("HTTP://abc.com:80/~smith/home.html?1=2&2=4~#anchor+1~;http://ABC.com/%7Esmith/home.html?1=2&2=4%7E#anchor+1%7E")==True)
# print(compare_urls("HTTP://abc.com:80/~smith/home.html?1=2&2=4~#anchor+1%40~;http://ABC.com/%7Esmith/home.html?1=2&2=4%7E#anchor+1@%7E")==True)
# print(compare_urls("HTTP://abc.com:80/~smith/hOme.html?1=2&2=4~#anchor+1%40~;http://ABC.com/%7Esmith/home.html?1=2&2=4%7E#anchor+1@%7E")==False)
# print(compare_urls("HTTPS://abc.com:8080/path/index*!^(~|>`^|<{`{>.html;HTTP://EXAMPLE.com:8081//index{~.html")==False)