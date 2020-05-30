import urllib.request

try:
    url = urllib.request.urlopen("https://github.com/AnubhavMadhav/Learn-Python")
    content = url.read()
    url.close()
except urllib.error.HTTPError:          # In case if there is no web page for the given link/url
    print("Page Not Found")
    exit()

f = open("MyPythonUrlFile.html",'wb')
f.write(content)
f.close()


# comment added