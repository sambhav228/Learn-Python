import urllib.request

url = "https://media-exp1.licdn.com/dms/image/C5103AQEOvLxUaTtKNg/profile-displayphoto-shrink_200_200/0?e=1591228800&v=beta&t=tKVop73vfOaLV-_m1Mge4twscQlgZz43RBUhTUS1Jow"

urllib.request.urlretrieve(url, "mypythonimg.jpg")