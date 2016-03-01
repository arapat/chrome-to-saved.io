import requests
url = 'http://devapi.saved.io/v1/bookmarks'
apikey = '<your_key>'
token = {'token': apikey}

r = requests.get(url, params = token)
bookmarks = eval(r.text)
lists = {}
for b in bookmarks:
    lname, title, url = b['list_name'], b['title'], b['url']
    title = title.replace('\/', '/')
    url = url.replace('\/', '/')
    if lname not in lists:
        lists[lname] = []
    lists[lname].append((title, url))

for a, b in lists.items():
    print('%s' % a)
    print('======')
    for t, u in b:
        print('* [%s](%s)' % (t, u))
    print()
